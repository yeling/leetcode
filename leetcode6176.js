/*
* auther yeling
* 
* 
*/
/**
 * @param {number[]} nums
 * @return {number}
 */
var mostFrequentEven = function(nums) {
    let cache = new Map();
    for(let i = 0; i < nums.length; i++) {
        if(nums[i]%2 == 0) {
            let curr = cache.get(nums[i]);
            if(curr == null) {
                curr = 1;
            } else {
                curr ++;
            }
            cache.set(nums[i],curr);
        }
    }
    let maxCount = 0 ;
    let maxNum = -1;
    cache.forEach((value,key) => {
        if(maxCount < value) {
            maxCount = value;
            maxNum = key;
        } else if(maxCount == value && maxNum > key) {
            maxNum = key;
        }
    })
    return maxNum;
};

nums = [0,1,2,2,4,4,1]
console.log(mostFrequentEven(nums));
