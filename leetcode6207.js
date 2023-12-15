/*
* auther yeling
* 2444. 统计定界子数组的数目
* 
*/
/**
 * @param {number[]} nums
 * @param {number} minK
 * @param {number} maxK
 * @return {number}
 */
//35 / 48 个通过测试用例 TLE
var countSubarrays2 = function(nums, minK, maxK) {
    let h = new Array(nums.length).fill(0);
    let m = new Array(nums.length).fill(0);
    let lowbit = (x) => {
        return x & -x;
    }

    //在求区间最值的算法中，h[x]储存的是[x，x-lowbit(x)+1]中每个数的最大值。
    let updateMax = (i, a, h) => {
        while (i <= a.length) {
            h[i] = a[i - 1];
            for (let j = 1; j < lowbit(i); j <<= 1) {
                h[i] = Math.max(h[i], h[i - j]);
            }
            i += lowbit(i);
            // console.log(i);
            // console.log(h);
        }
    }

    let queryMax = (i, j, a, h) => {
        let ret = 0;
        while (i <= j) {
            ret = Math.max(ret, a[j - 1]);
            j--;
            for (; j - lowbit(j) >= i; j = j - lowbit(j)) {
                ret = Math.max(ret, h[j]);
            }
        }
        return ret;
    }

    let updateMin = (i, a, h) => {
        while (i <= a.length) {
            h[i] = a[i - 1];
            for (let j = 1; j < lowbit(i); j <<= 1) {
                h[i] = Math.min(h[i], h[i - j]);
            }
            i += lowbit(i);
            // console.log(i);
            // console.log(h);
        }
    }

    let queryMin = (i, j, a, h) => {
        let ret = Number.MAX_SAFE_INTEGER;
        while (i <= j) {
            ret = Math.min(ret, a[j - 1]);
            j--;
            for (; j - lowbit(j) >= i; j = j - lowbit(j)) {
                ret = Math.min(ret, h[j]);
            }
        }
        return ret;
    }

    for (let i = 0; i < nums.length; i++) {
        updateMax(i + 1, nums, h);
        updateMin(i + 1, nums, m);
    }

    let sum = 0;
    for (let i = 0; i < nums.length; i++) {
        for (let j = i; j < nums.length; j++) {
            let max = queryMax(i + 1, j + 1, nums, h);
            let min = queryMin(i + 1, j + 1, nums, m);
            //console.log(`${i} ${j} ${min} ${max}`);
            if(min == minK && max == maxK) {
                sum++;
            }
        }
    }
    return sum;

}

var countSubarrays = function(nums, minK, maxK) {
    let sum = 0; 
    let l = -1, minI = -1, maxI = -1;
    for(let i = 0; i < nums.length; i++) {
        if(nums[i] > maxK || nums[i] < minK) {
            l = i;
        }
        if(nums[i] == minK) {
            minI = i;
        }
        if(nums[i] == maxK) {
            maxI = i;
        }
        sum += Math.max(0, Math.min(minI, maxI) - l);
    }
    return sum;
}
nums = [1,3,5,2,7,5], minK = 1, maxK = 5
nums = [1,1,1,1], minK = 1, maxK = 1
// console.log(countSubarrays2(nums,minK,maxK));
console.log(countSubarrays(nums,minK,maxK));
