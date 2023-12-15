/*
* auther yeling
* 458. 可怜的小猪
* 动态规划
* dp[i + 1] = 2 * i * dp[i]; 
*/

/**
 * @param {number} buckets
 * @param {number} minutesToDie
 * @param {number} minutesToTest
 * @return {number}
 */
//12 / 17
var poorPigs = function (buckets, minutesToDie, minutesToTest) {
    if (buckets == 1) {
        return 0;
    }
    let n = Math.floor(minutesToTest / minutesToDie) + 1;
    let pigs = 1, sum = 2;
    while (sum < buckets) {
        pigs++;
        sum = 2 * pigs * sum;
        console.log(`${sum} ${pigs} ${n}`);
    }
    return pigs;
  
};

var poorPigs2 = function (buckets, minutesToDie, minutesToTest) {
    const states = Math.floor(minutesToTest / minutesToDie) + 1;
    const pigs = Math.ceil(Math.log(buckets) / Math.log(states));
    return pigs;
}

var poorPigs3 = function (buckets, minutesToDie, minutesToTest) {
    if (buckets == 1) {
        return 0;
    }
    let n = Math.floor(minutesToTest / minutesToDie) + 1;
    let pigs = 0, sum = 1;
    while (sum < buckets) {
        pigs++;
        sum = n * sum;
        //console.log(`${sum} ${pigs} ${n}`);
    }
    return pigs;
}

buckets = 1000, minutesToDie = 15, minutesToTest = 60
buckets = 1000, minutesToDie = 12, minutesToTest = 60
// buckets = 4, minutesToDie = 15, minutesToTest = 30
// buckets = 1, minutesToDie = 1, minutesToTest = 1
console.log(poorPigs3(buckets, minutesToDie, minutesToTest));
console.log(poorPigs2(buckets, minutesToDie, minutesToTest));