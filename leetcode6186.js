/*
* auther yeling
* 
* 
*/

/**
 * @param {number[]} nums
 * @return {number[]}
 */

// TLE 58 / 59 个通过测试用例
var smallestSubarrays = function(nums) {
    let max = 0;
    let n = nums.length;
    for(let i = 0; i < n; i++) {
        max |= nums[i];
    }
    let res = new Array(n).fill(0);
    for(let i = 0; i < n; i++) {
        let temp = 0;
        let max = 0;
        for(let j = i; j < n; j++) {
            max |= nums[j];
        }
        for(let j = i; j < n; j++) {
            temp |= nums[j];
            if(temp == max) {
                res[i] = j - i + 1;
                break;
            }
        }
    }
    //console.log(max);
    return res;

};

var smallestSubarrays2 = function(nums) {
    let max = 0;
    let n = nums.length;
    let res = new Array(n).fill(0);
    for(let i = 0; i < n; i++) {
        let max = 0;
        let cache = new Map();
        for(let j = i; j < n; j++) {
            max |= nums[j];
            if(cache.has(max) == false) {
                cache.set(max, j);
            }
        }
        res[i] = cache.get(max) - i + 1;
    }
    //console.log(max);
    return res;
};


var smallestSubarrays3 = function(nums) {
    let n = nums.length;
    let res = new Array(n).fill(0);
    let pre = new Array(n).fill(0).map(() => new Array(32).fill(0));
    for(let i = 0; i < n; i++) {
        let curr = nums[i];
        let index = 0;
        let numArray = new Array(32).fill(0);
        while(curr > 0) {
            if(curr % 2 == 1) {
                numArray[index] = 1;
            } else {
                numArray[index] = 0;
            }
            curr = (curr >> 1);
            index++;
        }
        
        if(i == 0) {
            pre[i].forEach((value,index) => {
                pre[i][index] =  numArray[index];
            })
        } else {
            pre[i].forEach((value,index) => {
                pre[i][index] = pre[i - 1][index] + numArray[index];
            })
        }
        //console.log(pre[i]);
    }

    for(let i = 0; i < n; i++) {
        let max = 0;
        let maxArray = [];
        if(i == 0) {
            maxArray = pre[n-1];
        } else {
            for(let k = 31; k >= 0; k--) {
                maxArray[k] = pre[n-1][k] - pre[i - 1][k]
            }
        }
        for(let k = 31; k >= 0; k--) {
            if(maxArray[k] >= 1) {
                max |= (1<<k);
            }
        }
        let temp = 0;
        for(let j = i; j < n; j++) {
            temp |= nums[j];
            if(temp == max) {
                res[i] = j - i + 1;
                break;
            }
        }
    }
    //console.log(pre.join('\n'));
    return res;

}

var smallestSubarrays4 = function(nums) {
    
}

nums = [1,0,2,6,4,7];
// nums = [1,2];
// nums = [1,0,2,1,3];


// console.log(smallestSubarrays(nums))
console.log(smallestSubarrays2(nums))
console.log(smallestSubarrays3(nums))