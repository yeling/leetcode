/*
* auther yeling
* 480. 滑动窗口中位数
* 
*/

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
//暴力一下，居然给过了
var medianSlidingWindow2 = function(nums, k) {
    let res = [];
    for(let i = 0; i <= nums.length - k; i++) {
        let temp = nums.slice(i,i+k);
        temp.sort((a,b) => a - b);
        if(k%2 == 0) {
            res.push((temp[k/2] + temp[k/2 -1])/2);
        } else {
            res.push(temp[Math.floor(k/2)]);
        }
        //console.log(nums[i]);
    }
    return res; 
};

//冒泡排序 O(n^2)的时间复杂度，超时。默认sort是 n(logn)
var medianSlidingWindow3 = function(nums, k) {
    let res = [];
    for(let i = 0; i <= nums.length - k; i++) {
        let temp = nums.slice(i,i+k);
        //temp.sort((a,b) => a - b);
        for(let si = 0; si <= Math.floor(k/2); si++) {
            for(let sj = 0; sj < k - 1 - si; sj++ ) {
                if(temp[sj] < temp[sj+1]) {
                    swap(temp,sj,sj+1)
                }
            }
        }
        if(k%2 == 0) {
            res.push((temp[k/2] + temp[k/2 -1])/2);
        } else {
            res.push(temp[Math.floor(k/2)]);
        }
    }
    return res; 
};

var medianSlidingWindow = function(nums, k) {
    let res = [];
    for(let i = 0; i <= nums.length - k; i++) {
        let temp = nums.slice(i,i+k);
        //temp.sort((a,b) => a - b);
        for(let si = 0; si <= Math.floor(k/2); si++) {
            for(let sj = 0; sj < k - 1 - si; sj++ ) {
                if(temp[sj] < temp[sj+1]) {
                    swap(temp,sj,sj+1)
                }
            }
        }
        if(k%2 == 0) {
            res.push((temp[k/2] + temp[k/2 -1])/2);
        } else {
            res.push(temp[Math.floor(k/2)]);
        }
    }
    return res; 
};

function swap(arr, i, j) {
    var temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
}


nums = [1,3,-1,-3,5,3,6,7]
nums = [1,4,2,3]
k = 4
nums = [1]
k = 1

console.log(medianSlidingWindow(nums,k));
console.log(medianSlidingWindow2(nums,k));