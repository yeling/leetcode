/*
* auther yeling
* 6109. 知道秘密的人数
* dp问题，dp[i],表示第i天刚知道该秘密的人数
*/
let MOD = 1000000007;
var peopleAwareOfSecret = function (n, delay, forget) {
    let dp = new Array(n + forget - delay);
    dp.fill(0);
    dp[0] = 1;
    for (let i = 0; i < n - delay ; i++) {
        for (let  j = i + delay; j < i + forget; j++) {
            dp[j] = (dp[j] + dp[i])%MOD;
        }
    }
    let res = 0;
    for (let  j = n - forget; j < n; j++) {
        res = (res +  dp[j])%MOD;
    }
    //console.log(dp);
    return res;
};

let n = 6, delay = 2, forget = 4;
n = 4, delay = 1, forget = 3;
console.log(peopleAwareOfSecret(n, delay, forget));