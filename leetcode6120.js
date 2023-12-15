/*
* auther yeling
* 
* 
*/

var numberOfPairs = function(nums) {
    let count = 0;
    let cache = new Map();
    for(let i = 0; i < nums.length; i++) {
        if(cache.get(nums[i]) != null) {
            cache.delete(nums[i]);
            count++;
        } else {
            cache.set(nums[i],true);
        }
        
    }
    return [count,cache.size];
};

nums = [1,3,2,1,3,2,2]
console.log(numberOfPairs(nums));

