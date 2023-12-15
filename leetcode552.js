/*
* auther yeling
* 552. 学生出勤记录 II
* 
*/

/**
 * @param {number} n
 * @return {number}
 */
//dfs
var checkRecord2 = function (n) {
    let count = 0;
    let dfs = function (n, depth, res) {
        if (depth == n) {
            //console.log('dfs ' + res)
            count++;
            return;
        }
        if (res.length == 0 || res.find((item) => item == 'A') == null) {
            res.push('A');
            dfs(n, depth + 1, res.slice());
            res.pop();
        }
        if (res.length < 2 || res[res.length - 1] != 'L' || res[res.length - 2] != 'L') {
            res.push('L');
            dfs(n, depth + 1, res.slice());
            res.pop();
        }

        res.push('P');
        dfs(n, depth + 1, res.slice());
        res.pop();
    }
    dfs(n, 0, []);
    return count;
};

//不能有连续A
const MOD = 10 ** 9 + 7;
var checkRecord3 = function (n) {
    let dp = new Array(n + 1).fill(0);
    let dpA = new Array(n + 1).fill(0);
    let dpL = new Array(n + 1).fill(0);
    let dpLL = new Array(n + 1).fill(0);

    dp[0] = 1
    dp[1] = 3;
    dpA[1] = 1;
    dpL[1] = 1;
    for (let i = 2; i <= n; i++) {
        dpA[i] = (dp[i - 1] - dpA[i - 1]);
        if (i == 2) {
            dpLL[i] = 1;
            dpL[i] = dp[i - 1];
        } else {
            dpL[i] = (dp[i - 1] - dpLL[i - 1]);
            dpLL[i] = (dpL[i - 1] - dpLL[i - 1]);
        }
        dp[i] = (dp[i - 1] + dpA[i] + dpL[i]);

        //console.log(`${i} ${dp[i]} dpA ${dpA[i]} dpL ${dpL[i]}`)
    }

    //console.log(`${dp} dpA ${dpA} dpL ${dpL}`)
    return dp[n];
};

//
var checkRecord4 = function (n) {
    let dp = new Array(n + 1).fill(0);
    let dpL = new Array(n + 1).fill(0);
    let dpLL = new Array(n + 1).fill(0);

    dp[0] = 0
    dp[1] = 2;
    dpL[1] = 1;
    for (let i = 2; i <= n; i++) {
        if (i == 2) {
            dpLL[i] = 1;
            dpL[i] = dp[i - 1];
        } else {
            dpL[i] = (dp[i - 1] - dpLL[i - 1]);
            dpLL[i] = (dpL[i - 1] - dpLL[i - 1]);
        }
        dp[i] = (dp[i - 1] + dpL[i]);

        console.log(`${i} ${dp[i]} dpL ${dpL[i]} dpLL ${dpLL[i]}`)
    }

    console.log(`${dp} dpL ${dpL}`)
    return dp[n] + n * dp[n - 1];
};

var checkRecord = function (n) {
    let dp = new Array(n + 1).fill(0);
    let dpA = new Array(n + 1).fill(0);
    let dpL = new Array(n + 1).fill(0);
    let dpLL = new Array(n + 1).fill(0);

    dp[0] = 1
    dp[1] = 3;
    dpA[1] = 1;
    dpL[1] = 1;
    for (let i = 2; i <= n; i++) { 
        if (i == 2) {
            dpLL[i] = 1;
            dpL[i] = dp[i - 1];
        } else {
            dpL[i] = (dp[i - 1] - dpLL[i - 1]);
            dpLL[i] = (dpL[i - 1] - dpLL[i - 1]);
        }
        //L P 
        dp[i] = dp[i - 1] + dpL[i];
        let affect = 0;
        for (let j = 1; j < i; j++) {
            let temp = dpA[j];
            for(let k = 0; k < i - 1 - j; k++) {
                temp = 2 * temp  - dpLL[k]
            }
            affect += temp;
        }
        //A
        dpA[i] = (dp[i - 1] - affect);
        dp[i] += dpA[i]; 

        console.log(`${i} affect ${affect} ${dp[i]} dpA ${dpA[i]} dpL ${dpL[i]} dpLL ${dpLL[i]}`)
    }

    console.log(`${dp} dpA ${dpA} dpL ${dpL}`)
    return dp[n];
};

n = 7;
console.log(checkRecord2(n));
console.log('ch2');
console.log(checkRecord(n));
