/*
* auther yeling
* 2364. 统计坏数对的数目
*/

//63 / 65 个通过测试用例 超时
var countBadPairs2 = function(nums) {
    let n = nums.length;
    let sum = 0; 
    for(let i = 0; i < n; i++) {
        for(let j = i + 1; j < n; j++) {
            if(j - i != nums[j] - nums[i]) {
                sum++;
            }
        }
    }
    return sum;
};

var countBadPairs = function(nums) {
    let n = nums.length;
    let cache = new Map();
    let sum = 0; 
    for(let i = 0; i < n; i++) {
        let k = nums[i] - i;
        if(cache.has(k) == false) {
            cache.set(k,1);
        } else {
            cache.set(k,cache.get(k) + 1);
        }
    }
    sum = n * ( n + 1 )/2;
    cache.forEach((value) => {
        sum -= value * (value + 1) / 2;
    });
    return sum;
};



nums = [4,1,3,3]
console.log(countBadPairs2(nums));
console.log(countBadPairs(nums));
