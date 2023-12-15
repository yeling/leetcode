/*
* auther yeling
* 
* 
*/
'use strict';

// process.stdin.resume();
// process.stdin.setEncoding('utf-8');

// let inputString = '';
// let currentLine = 0;

// process.stdin.on('data', inputStdin => {
//     inputString += inputStdin;
// });

// process.stdin.on('end', _ => {
//     inputString = inputString.trim().split('\n').map(string => {
//         return string.trim();
//     });

//     main();
// });

// function readline() {
//     return inputString[currentLine++];
// }
// function print(str) {
//     console.log(str);
// }

const { readline, print, testOutput } = require('@ip-algorithmics/codeforces-io');
main();
testOutput();

function begin(n, lids, vals) {
    //print(n, lids, vals);
    let sum = 0;
    let dp = new Array(n).fill(0).map(() => new Array(2).fill(0));
    //dp[i][0] 表示i位不移动
    //dp[i][1] 表示i位移动

    for(let i = 0; i < n; i++) {
        if(lids[i] == 1) {
            if(i == 0) {
                dp[i][0] = vals[i];
            } else if(lids[i - 1] == 0) {
                let pre = Math.max(dp[i-1][0], dp[i-1][1]);
                dp[i][0] = pre + vals[i];
                dp[i][1] = pre + vals[i-1];
            } else if(lids[i - 1] == 1) {
                dp[i][1] = Math.max(dp[i][1], dp[i-1][1] + vals[i-1]);
                dp[i][0] = Math.max(dp[i][1], dp[i-1][1] + vals[i]);
                dp[i][0] = Math.max(dp[i][0], dp[i-1][0] + vals[i]);
            }
        } else {
            if(i > 0) {
                dp[i][0] = dp[i][1] = Math.max(dp[i-1][0],  dp[i-1][1]);
            }
        }
        
    }
    print(Math.max(dp[n-1][0], dp[n-1][1]));
}

function main() {
    var caseNum = parseInt(readline(), 10);
    for (var i = 0; i < caseNum; i++) {
        var n = parseInt(readline(), 10);
        var lids = readline()
            .trim()
            .split('')
            .map((y) => parseInt(y, 10));
        var vals = readline()
            .trim()
            .split(' ')
            .map((y) => parseInt(y, 10));
        begin(n, lids, vals);
    }
}