/*
* auther yeling
* 
* 
*/
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
//TLE
//82 / 86 个通过测试用例
var lengthOfLIS = function(nums, k) {
    let n = nums.length;
    let max = 0;
    let dp = new Array(n).fill(0);
    for (let i = n - 1; i >= 0; i--) {
        dp[i] = 1;
        for (let j = i + 1; j < n; j++) {
            if(nums[j] - nums[i] <= k && nums[j]  > nums[i]) {
                dp[i] = Math.max(dp[i], dp[j] + 1);
            }
        }
        max = Math.max(max,dp[i]);
        console.log('mm')
        console.log(dp);
    }
    return max;
};

var lengthOfLIS2 = function(nums, k) {
    let n = nums.length;
    let max = 0;
    let dp = new Array(n).fill(0);
    for (let i = n - 1; i >= 0; i--) {
        dp[i] = 1;
        for (let j = i + 1; j < n; j++) {
            if(nums[j] - nums[i] <= k && nums[j]  > nums[i]) {
                dp[i] = Math.max(dp[i], dp[j] + 1);
            }
        }
        max = Math.max(max,dp[i]);
        // console.log('mm')
        // console.log(dp);
    }
    return max;
};


nums = [4,2,1,4,3,4,5,8,15], k = 3
nums = [13376,78205,90579,27044,64868,8097,97103,45093,4025,83275,76070,17810,84854,61167,24334,40210,2764,92411,30050,27921,65174,12317,71595,39190,58477,55830,56413,60635,60155,23920,67158,91372,5094,67596,51745,38796,75131,26319,92835,91491,93404,71351,35308,68934,15065,79779,73246,81660,37000,59836,69993,48861,58080,91743,89821,42466,17482,20974,3926,67372,83004,37598,44041,26663,85888,74498,54418,29502,87177,59136,12309,58536,25107,70924,22069,37965,84172,24072,14841,18081,49519,81325,67005,80504,19014,60038,14290,36987,29132,40963,50031,50293,97494,99059,13334,93653,80372,58100,72638,76442,23225,59536,54596,13421,4661,22725,73178,86605,31522,67473,39371,32213,55161,90925,75105,66932,17181,76782,43770,73892,60676,11639,16867,76690,81138,12667,41130,36579,42083,4363,59180,69680,84177,11396,53512,49306,98493,9917,11992,90520,1515,70445,1601,56235,7638,92955,30075,60937,47675,50719,51585,35116,72048,97000,41429,1514,5751,25900,26908,50599,24744,9750,80270,97242,27679,28052,85,71504,77207,97841,92208,53863,40455,28268,33733,9301,90771,31982,27371,69506,62339,72812,30804,79347,49176,24708,30723,68165,26951,50043,66443,37285,216,41866,54413,96520,37341,86444,77644,53078,37156,56187,18563,33395,67626,5740,57682,64403,35788,1893,18496,33350,50532,16854,51486,95145,78881,97365,23817,46206,4325,83886]
k = 95566;
console.log(nums.length);
// nums = [4,5,8], k = 3
console.time('lengthOfLIS')
console.log(lengthOfLIS2(nums,k));
console.timeEnd('lengthOfLIS');