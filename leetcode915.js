/*
* auther yeling
* 
* 
*/

/**
 * @param {number[]} nums
 * @return {number}
 */
var partitionDisjoint = function(nums) {
    let cache = new Map();
    let sorted = nums.slice().sort((a,b) => a - b);
    for(let i = 0; i < nums.length; i++) {
        //add
        let count = cache.get(nums[i]);
        if(count == null) {
            count = 0;
        }
        count++;
        if(count == 0) {
            cache.delete(nums[i]);
        } else {
            cache.set(nums[i], count);
        }
        
        //remove
        count = cache.get(sorted[i]);
        if(count == null) {
            count = 0;
        }
        count--;
        if(count == 0) {
            cache.delete(sorted[i]);
        } else {
            cache.set(sorted[i], count);
        }

        if(cache.size == 0) {
            return i + 1;
        }
        //console.log(cache);
    }
    return 0;
};

nums = [5,0,3,8,6]

console.log(partitionDisjoint(nums));