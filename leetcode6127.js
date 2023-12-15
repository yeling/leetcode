/*
* auther yeling
* 6127. 优质数对的数目
* 
*/
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var countExcellentPairs = function (nums, k) {
    let n = nums.length;
    let cache = new Array(k + 2).fill(0);
    let numSet  = new Set();

    for (let i = 0; i < n; i++) {
        let temp = nums[i];
        if(numSet.has(nums[i])) {
            continue;
        } else {
            numSet.add(nums[i]);
        }
        let count = 0;
        while (temp > 0) {
            count += temp & 0x1;
            temp = temp >> 1;
        }
        if (count > k) {
            cache[k + 1]++;
        } else {
            cache[count]++;
        }
    }
    console.log(cache);
    let sum = 0;
    let preCache = new Array(k + 2).fill(0);


    for (let i = 1; i <= k + 1; i++) {
        preCache[i] = preCache[i - 1] + cache[i];
    }
    console.log(preCache);

    for (let i = 1; i <= k + 1; i++) {
        console.log(`${cache[i]} ${preCache[k + 1]} ${preCache[k - i - 1]}`);
        let  start = k - i - 1;
        if(start < 0) {
            start = 0;
        }
        sum += cache[i]*(preCache[k + 1] - preCache[start]);
        //console.log(`sum ${sum}`);
    }
    
    return sum;
};


nums = [1, 2, 3, 1], k = 3
nums = [1,2,3,1,536870911], k = 3
console.log(countExcellentPairs(nums, k));

