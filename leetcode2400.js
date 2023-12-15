/*
* auther yeling
* 
* 
*/

/**
 * @param {number} startPos
 * @param {number} endPos
 * @param {number} k
 * @return {number}
 */
let MOD = 10 ** 9 + 7;

var numberOfWays = function (startPos, endPos, k) {
    if(k < endPos - startPos) {
        return 0;
    }
    if((k + startPos - endPos) % 2 != 0) {
        return 0;
    }

    let begin =  startPos - (k + startPos - endPos) / 2;
    let end = endPos + (k + startPos - endPos) / 2;
    let offset = -begin;
    begin += offset;
    end += offset;
    startPos += offset;
    endPos += offset;
    let dp = new Array(end + 2).fill(0).map(() => new Array(k + 1).fill(0));    
    for(let j = 1; j <= k; j++) {
        for(let i = begin; i <= end; i++) {
            //console.log(`${i} ${j}`)
            if(Math.abs(endPos - i) == j) {
                dp[i][j] = 1;
            } else {
                dp[i][j] = dp[i+1][j-1];
                if(i - 1 >= 0) {
                    dp[i][j] = (dp[i][j]  + dp[i-1][j-1])%MOD;
                }                 
            }
        }
    }
    //console.log(dp.join('\n'));
    return dp[startPos][k];
    
};  

startPos = 1, endPos = 2, k = 3
startPos = 2, endPos = 5, k = 7
console.log(numberOfWays(startPos,endPos, k));