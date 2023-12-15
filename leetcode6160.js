/*
* auther yeling
* 
* 
*/

/**
 * @param {number[]} nums
 * @param {number[]} queries
 * @return {number[]}
 */
var answerQueries = function(nums, queries) {
    nums.sort((a,b) => a - b);
    let n = nums.length;
    let m = queries.length;
    let preSum = new Array(n + 1).fill(0);
    for(let i = 0; i < n; i++) {
        preSum[i+1] = preSum[i] + nums[i];
    }
    console.log(preSum);

    let res = [];
    for(let i = 0; i < m; i++) {
        let left = 1, right = n;
        let target = queries[i];
        while(left <= right) {
            let mid = left + Math.floor((right - left)/2);
            if(target < preSum[mid]) {
                right = mid - 1;
            } else if(target >= preSum[mid]) {
                left = mid + 1;
            }
        }
        res.push(left - 1);
        console.log(res);

    }

    return res;

};


nums = [4,5,2,1], queries = [3,10,21];
nums = [2,3,4,5], queries = [1]
queries = [0];

console.log(answerQueries(nums,queries));
