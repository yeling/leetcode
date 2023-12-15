/*
* auther yeling
* 632. 最小区间
* 归并排序，滑动窗口
* 归并排序可以改成优先队列log(n)
*/

/**
 * @param {number[][]} nums
 * @return {number[]}
 */
var smallestRange = function(nums) {
    let allNum = [];
    let allValue = [];
    let n = nums.length;
    let index = new Array(n).fill(0);    
    while(true) {
        let minPos = -1;
        let min = Number.MAX_VALUE;
        for(let i = 0; i < n; i++) {
            if(index[i] < nums[i].length && min > nums[i][index[i]]) {
                min = nums[i][index[i]];
                minPos = i;
            }
        }
        if(minPos == -1) {
            break;
        }
        allNum.push(minPos);    
        allValue.push(nums[minPos][index[minPos]]);        
        index[minPos]++;            
    }
    // console.log(allNum);
    // console.log(allValue);
    let cache = new Map();
    let left = 0, right = 0;
    let result = null;
    while(right <= allNum.length) {
        if(cache.size == n) {
            if(result == null) {
                result = [allValue[left], allValue[right - 1]];
            } else if(allValue[right - 1] - allValue[left] < result[1] - result[0]) {
                result = [allValue[left], allValue[right - 1]];                
            }            
            if(cache.get(allNum[left]) == 1) {
                cache.delete(allNum[left]);
            } else {
                cache.set(allNum[left], cache.get(allNum[left])-1);
            }            
            left++;
        } else {
            // if(right == n) {
            //     break;
            // }
            let dstIndex = allNum[right];
            let dstValue = cache.get(dstIndex);
            if(dstValue == null) {
                dstValue = 1;
            } else {
                dstValue ++;
            }
            cache.set(dstIndex, dstValue);
            right++;
        }      
        console.log(`left ${left} right ${right}`);
        console.log(cache);
        console.log(result);              
    }
    return result;
    
};

nums = [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]];
nums = [[10],[11]];
console.log(smallestRange(nums));