/*
* auther yeling
* 
* 
*/

/**
 * @param {number[]} nums
 * @param {number} space
 * @return {number}
 */
//39 / 44 个通过测试用例
var destroyTargets2 = function(nums, space) {
    let cache = new Array(space).fill(0).map(() => []);
    for(let i = 0; i < nums.length; i++) {
        cache[nums[i]%space].push(nums[i]);
    }
    //console.log(cache.join('\n'));
    let min = Number.MAX_SAFE_INTEGER;
    let maxLen = 0;
    for(let i = 0; i < space; i++) {
        cache[i].sort((a,b) => {
            return a - b;
        })
        if(cache[i].length > maxLen) {
            maxLen = cache[i].length;
            min = cache[i][0];
        } else if(cache[i].length == maxLen) {
            min = Math.min(min, cache[i][0]);
        }
    }
    return min;
};
//MLE
var destroyTargets3 = function(nums, space) {
    //cache[i,2] i,0 存数量， i，1存最小值
    let cache = new Array(space).fill(0).map(() => [0,Number.MAX_SAFE_INTEGER]);
    let maxLen = 0;
    let min = Number.MAX_SAFE_INTEGER;
    for(let i = 0; i < nums.length; i++) {
        let index = nums[i]%space;
        cache[index][0]++;
        if(nums[i] < cache[index][1]) {
            cache[index][1] = nums[i];
        }
        if(cache[index][0] > maxLen) {
            maxLen = cache[index][0];
            min = cache[index][1];
        } else if(cache[index][0] == maxLen) {
            min = Math.min(min, cache[index][1]);
        }
    }
    return min;
};

//MLE
var destroyTargets = function(nums, space) {
    //cache[i,2] i,0 存数量， i，1存最小值
    let cache = new Map();
    let maxLen = 0;
    let min = Number.MAX_SAFE_INTEGER;
    for(let i = 0; i < nums.length; i++) {
        let index = nums[i]%space;
        let curr = cache.get(index);
        if(curr == null) {
            curr = [0,Number.MAX_SAFE_INTEGER];
            cache.set(index, curr);
        }
        curr[0]++;
        if(nums[i] < curr[1]) {
            curr[1] = nums[i];
        }
        if(curr[0] > maxLen) {
            maxLen = curr[0];
            min = curr[1];
        } else if(curr[0] == maxLen) {
            min = Math.min(min, curr[1]);
        }
    }
    return min;
};


nums = [3,7,8,1,1,5], space = 2;
nums = [6,2,5], space = 100;
nums = [1,5,3,2,2], space = 10000;
console.log(destroyTargets2(nums, space));
console.log(destroyTargets(nums, space));

