/*
* auther yeling
* 
* 
*/

/**
 * @param {number} n
 * @return {number}
 */
// TLE 51 / 64 个通过测试用例
var distinctSequences2 = function (n) {
    let MOD = 10 ** 9 + 7;
    let dp = new Array(n + 1).fill(0).map(() => new Array(7).fill(0));
    for (let i = 1; i <= n; i++) {
        if (i == 1) {
            dp[i].fill(1);
        } else {
            for (let j = 1; j <= 6; j++) {
                switch (j) {
                    case 1:
                        dp[i][j] = (dp[i][j] + dp[i - 1][2]) % MOD;
                        dp[i][j] = (dp[i][j] + dp[i - 1][3]) % MOD;
                        dp[i][j] = (dp[i][j] + dp[i - 1][4]) % MOD;
                        dp[i][j] = (dp[i][j] + dp[i - 1][5]) % MOD;
                        dp[i][j] = (dp[i][j] + dp[i - 1][6]) % MOD;

                        //for (let k = 2; i - k >= 0; k++) {
                        for (let k = i; k >= 2; k--) {
                            if (k % 2 == 0) {
                                dp[i][j] = (dp[i][j] - dp[i - k][1]) % MOD;
                                dp[i][j] = (dp[i][j] - dp[i - k][1]) % MOD;
                                dp[i][j] = (dp[i][j] - dp[i - k][1]) % MOD;
                                dp[i][j] = (dp[i][j] - dp[i - k][1]) % MOD;
                                dp[i][j] = (dp[i][j] - dp[i - k][1]) % MOD;

                            } else {
                                dp[i][j] = (dp[i][j] + dp[i - k][2]) % MOD;
                                dp[i][j] = (dp[i][j] + dp[i - k][3]) % MOD;
                                dp[i][j] = (dp[i][j] + dp[i - k][4]) % MOD;
                                dp[i][j] = (dp[i][j] + dp[i - k][5]) % MOD;
                                dp[i][j] = (dp[i][j] + dp[i - k][6]) % MOD;
                            }
                        }
                        break;
                    case 2:
                        // dp[i][j] = (dp[i - 1][1] + dp[i - 1][3] + dp[i - 1][5]) % MOD;
                        dp[i][j] = (dp[i][j] + dp[i - 1][1]) % MOD;
                        dp[i][j] = (dp[i][j] + dp[i - 1][3]) % MOD;
                        dp[i][j] = (dp[i][j] + dp[i - 1][5]) % MOD;

                        for (let k = i; k >= 2; k--) {
                            if (k % 2 == 0) {
                                dp[i][j] = (dp[i][j] - dp[i - k][2]) % MOD;
                                dp[i][j] = (dp[i][j] - dp[i - k][2]) % MOD;
                                dp[i][j] = (dp[i][j] - dp[i - k][2]) % MOD;
                            } else {
                                dp[i][j] = (dp[i][j] + dp[i - k][1]) % MOD;
                                dp[i][j] = (dp[i][j] + dp[i - k][3]) % MOD;
                                dp[i][j] = (dp[i][j] + dp[i - k][5]) % MOD;
                            }
                        }
                        break;
                    case 3:
                        //dp[i][j] = (dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][4] + dp[i - 1][5]) % MOD;
                        dp[i][j] = (dp[i][j] + dp[i - 1][1]) % MOD;
                        dp[i][j] = (dp[i][j] + dp[i - 1][2]) % MOD;
                        dp[i][j] = (dp[i][j] + dp[i - 1][4]) % MOD;
                        dp[i][j] = (dp[i][j] + dp[i - 1][5]) % MOD;

                        for (let k = i; k >= 2; k--) {
                            if (k % 2 == 0) {
                                dp[i][j] = (dp[i][j] - dp[i - k][3]) % MOD;
                                dp[i][j] = (dp[i][j] - dp[i - k][3]) % MOD;
                                dp[i][j] = (dp[i][j] - dp[i - k][3]) % MOD;
                                dp[i][j] = (dp[i][j] - dp[i - k][3]) % MOD;
                            } else {
                                dp[i][j] = (dp[i][j] + dp[i - k][1]) % MOD;
                                dp[i][j] = (dp[i][j] + dp[i - k][2]) % MOD;
                                dp[i][j] = (dp[i][j] + dp[i - k][4]) % MOD;
                                dp[i][j] = (dp[i][j] + dp[i - k][5]) % MOD;

                            }
                        }
                        break;
                    case 4:
                        //dp[i][j] = (dp[i - 1][1] + dp[i - 1][3] + dp[i - 1][5]) % MOD;
                        dp[i][j] = (dp[i][j] + dp[i - 1][1]) % MOD;
                        dp[i][j] = (dp[i][j] + dp[i - 1][3]) % MOD;
                        dp[i][j] = (dp[i][j] + dp[i - 1][5]) % MOD;
                        for (let k = i; k >= 2; k--) {
                            if (k % 2 == 0) {
                                dp[i][j] = (dp[i][j] - dp[i - k][4]) % MOD;
                                dp[i][j] = (dp[i][j] - dp[i - k][4]) % MOD;
                                dp[i][j] = (dp[i][j] - dp[i - k][4]) % MOD;
                            } else {
                                dp[i][j] = (dp[i][j] + dp[i - k][1]) % MOD;
                                dp[i][j] = (dp[i][j] + dp[i - k][3]) % MOD;
                                dp[i][j] = (dp[i][j] + dp[i - k][5]) % MOD;
                            }
                        }
                        break;
                    case 5:
                        //dp[i][j] = (dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][3] + dp[i - 1][4] + dp[i - 1][6]) % MOD;
                        dp[i][j] = (dp[i][j] + dp[i - 1][1]) % MOD;
                        dp[i][j] = (dp[i][j] + dp[i - 1][2]) % MOD;
                        dp[i][j] = (dp[i][j] + dp[i - 1][3]) % MOD;
                        dp[i][j] = (dp[i][j] + dp[i - 1][4]) % MOD;
                        dp[i][j] = (dp[i][j] + dp[i - 1][6]) % MOD;

                        for (let k = i; k >= 2; k--) {
                            if (k % 2 == 0) {
                                dp[i][j] = (dp[i][j] - dp[i - k][5]) % MOD;
                                dp[i][j] = (dp[i][j] - dp[i - k][5]) % MOD;
                                dp[i][j] = (dp[i][j] - dp[i - k][5]) % MOD;
                                dp[i][j] = (dp[i][j] - dp[i - k][5]) % MOD;
                                dp[i][j] = (dp[i][j] - dp[i - k][5]) % MOD;
                            } else {
                                dp[i][j] = (dp[i][j] + dp[i - k][1]) % MOD;
                                dp[i][j] = (dp[i][j] + dp[i - k][2]) % MOD;
                                dp[i][j] = (dp[i][j] + dp[i - k][3]) % MOD;
                                dp[i][j] = (dp[i][j] + dp[i - k][4]) % MOD;
                                dp[i][j] = (dp[i][j] + dp[i - k][6]) % MOD;
                            }
                        }
                        break;
                    case 6:
                        //dp[i][j] = (dp[i - 1][1] + dp[i - 1][5]) % MOD;
                        dp[i][j] = (dp[i][j] + dp[i - 1][1]) % MOD;
                        dp[i][j] = (dp[i][j] + dp[i - 1][5]) % MOD;
                        for (let k = i; k >= 2; k--) {
                            if (k % 2 == 0) {
                                dp[i][j] = (dp[i][j] - dp[i - k][6]) % MOD;
                                dp[i][j] = (dp[i][j] - dp[i - k][6]) % MOD;
                            } else {
                                dp[i][j] = (dp[i][j] + dp[i - k][1]) % MOD;
                                dp[i][j] = (dp[i][j] + dp[i - k][5]) % MOD;

                            }
                        }
                        break;
                }
            }
        }
        // console.log(`i = ${i}`);
        // console.log(dp.join('\n'));

    }
    let sum = 0;
    console.log(dp[n]);
    for (let j = 1; j <= 6; j++) {
        sum = ((sum + dp[n][j]) % MOD + MOD)% MOD;
    }
    return sum;
}

// TLE 54 / 64 个通过测试用例
var distinctSequences = function (n) {
    let MOD = 10 ** 9 + 7;
    let dp = new Array(n + 1).fill(0).map(() => new Array(7).fill(0));
    let delta1 = new Array(n + 1).fill(0).map(() => new Array(7).fill(0));
    let delta2 = new Array(n + 1).fill(0).map(() => new Array(7).fill(0));
    for (let i = 1; i <= n; i++) {
        if (i == 1) {
            dp[i].fill(1);
        } else {
            for (let j = 1; j <= 6; j++) {
                switch (j) {
                    case 1:
                        dp[i][j] = (dp[i - 1][2] + dp[i - 1][3] + dp[i - 1][4] + dp[i - 1][5] + dp[i - 1][6]) % MOD;
                        //计算上一位的偏移
                        if(i > 2) {
                            delta1[i - 1][j] = delta1[i - 2][j];
                            delta2[i - 1][j] = delta2[i - 2][j];
                        }
                        if((i - 1)%2 == 0) {
                            delta1[i - 1][j] = (delta1[i - 1][j] + dp[i - 1][2] + dp[i - 1][3] + dp[i - 1][4] + dp[i - 1][5] + dp[i - 1][6])%MOD;
                            delta2[i - 1][j] = (delta2[i - 1][j] - (5 * dp[i - 1][1]) % MOD);
                        } else {
                            delta2[i - 1][j] = (delta2[i - 1][j] + dp[i - 1][2] + dp[i - 1][3] + dp[i - 1][4] + dp[i - 1][5] + dp[i - 1][6])%MOD;
                            delta1[i - 1][j] = (delta1[i - 1][j] - (5 * dp[i - 1][1]) % MOD);
                        }
                        if(i%2 == 0) {
                            dp[i][j] = (dp[i][j] + delta2[i - 2][j])%MOD;
                        } else {
                            dp[i][j] = (dp[i][j] + delta1[i - 2][j])%MOD;
                        }
                        break;
                    case 2:
                        dp[i][j] = (dp[i - 1][1] + dp[i - 1][3] + dp[i - 1][5]) % MOD;
                        //计算上一位的偏移
                        if(i > 2) {
                            delta1[i - 1][j] = delta1[i - 2][j];
                            delta2[i - 1][j] = delta2[i - 2][j];
                        }
                        if((i - 1)%2 == 0) {
                            delta1[i - 1][j] = (delta1[i - 1][j] + dp[i - 1][1] + dp[i - 1][3] + dp[i - 1][5])%MOD;
                            delta2[i - 1][j] = (delta2[i - 1][j] - (3 * dp[i - 1][2]) % MOD);
                        } else {
                            delta2[i - 1][j] = (delta2[i - 1][j] + dp[i - 1][1] + dp[i - 1][3] + dp[i - 1][5])%MOD;
                            delta1[i - 1][j] = (delta1[i - 1][j] - (3 * dp[i - 1][2]) % MOD);
                        }
                        if(i%2 == 0) {
                            dp[i][j] = (dp[i][j] + delta2[i - 2][j])%MOD;
                        } else {
                            dp[i][j] = (dp[i][j] + delta1[i - 2][j])%MOD;
                        }
                        break;
                    case 3:
                        dp[i][j] = (dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][4] + dp[i - 1][5]) % MOD;

                        //计算上一位的偏移
                        if(i > 2) {
                            delta1[i - 1][j] = delta1[i - 2][j];
                            delta2[i - 1][j] = delta2[i - 2][j];
                        }
                        if((i - 1)%2 == 0) {
                            delta1[i - 1][j] = (delta1[i - 1][j] + dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][4] + dp[i - 1][5])%MOD;
                            delta2[i - 1][j] = (delta2[i - 1][j] - (4 * dp[i - 1][3]) % MOD);
                        } else {
                            delta2[i - 1][j] = (delta2[i - 1][j] + dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][4] + dp[i - 1][5])%MOD;
                            delta1[i - 1][j] = (delta1[i - 1][j] - (4 * dp[i - 1][3]) % MOD);
                        }
                        if(i%2 == 0) {
                            dp[i][j] = (dp[i][j] + delta2[i - 2][j])%MOD;
                        } else {
                            dp[i][j] = (dp[i][j] + delta1[i - 2][j])%MOD;
                        }
                        break;
                    case 4:
                        dp[i][j] = (dp[i - 1][1] + dp[i - 1][3] + dp[i - 1][5]) % MOD;

                        if(i > 2) {
                            delta1[i - 1][j] = delta1[i - 2][j];
                            delta2[i - 1][j] = delta2[i - 2][j];
                        }
                        if((i - 1)%2 == 0) {
                            delta1[i - 1][j] = (delta1[i - 1][j] + dp[i - 1][1] + dp[i - 1][3] + dp[i - 1][5])%MOD;
                            delta2[i - 1][j] = (delta2[i - 1][j] - (3 * dp[i - 1][4]) % MOD);
                        } else {
                            delta2[i - 1][j] = (delta2[i - 1][j] + dp[i - 1][1] + dp[i - 1][3] + dp[i - 1][5])%MOD;
                            delta1[i - 1][j] = (delta1[i - 1][j] - (3 * dp[i - 1][4]) % MOD);
                        }
                        if(i%2 == 0) {
                            dp[i][j] = (dp[i][j] + delta2[i - 2][j])%MOD;
                        } else {
                            dp[i][j] = (dp[i][j] + delta1[i - 2][j])%MOD;
                        }
                        break;
                    case 5:
                        dp[i][j] = (dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][3] + dp[i - 1][4] + dp[i - 1][6]) % MOD;

                        if(i > 2) {
                            delta1[i - 1][j] = delta1[i - 2][j];
                            delta2[i - 1][j] = delta2[i - 2][j];
                        }
                        if((i - 1)%2 == 0) {
                            delta1[i - 1][j] = (delta1[i - 1][j] + dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][3] + dp[i - 1][4] + dp[i - 1][6])%MOD;
                            delta2[i - 1][j] = (delta2[i - 1][j] - (5 * dp[i - 1][5]) % MOD);
                        } else {
                            delta2[i - 1][j] = (delta2[i - 1][j] + dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][3] + dp[i - 1][4] + dp[i - 1][6])%MOD;
                            delta1[i - 1][j] = (delta1[i - 1][j] - (5 * dp[i - 1][5]) % MOD);
                        }
                        if(i%2 == 0) {
                            dp[i][j] = (dp[i][j] + delta2[i - 2][j])%MOD;
                        } else {
                            dp[i][j] = (dp[i][j] + delta1[i - 2][j])%MOD;
                        }
                        break;
                    case 6:
                        dp[i][j] = (dp[i - 1][1] + dp[i - 1][5]) % MOD;

                        if(i > 2) {
                            delta1[i - 1][j] = delta1[i - 2][j];
                            delta2[i - 1][j] = delta2[i - 2][j];
                        }
                        if((i - 1)%2 == 0) {
                            delta1[i - 1][j] = (delta1[i - 1][j] + dp[i - 1][1] + dp[i - 1][5])%MOD;
                            delta2[i - 1][j] = (delta2[i - 1][j] - (2 * dp[i - 1][6]) % MOD);
                        } else {
                            delta2[i - 1][j] = (delta2[i - 1][j] + dp[i - 1][1] + dp[i - 1][5])%MOD;
                            delta1[i - 1][j] = (delta1[i - 1][j] - (2 * dp[i - 1][6]) % MOD);
                        }
                        if(i%2 == 0) {
                            dp[i][j] = (dp[i][j] + delta2[i - 2][j])%MOD;
                        } else {
                            dp[i][j] = (dp[i][j] + delta1[i - 2][j])%MOD;
                        }
                        break;
                }
            }
        }
        // console.log(`i = ${i}`);
        // console.log(dp.join('\n'));

    }
    let sum = 0;
    //console.log(dp[n]);
    for (let j = 1; j <= 6; j++) {
        sum = ((sum + dp[n][j]) % MOD + MOD)% MOD;
    }
    return sum;
}

n = 3;   //66
n = 4;   //184
n = 10;   //516
n = 210; //433771587
n = 83;  //967602884
n = 7970;
label = 'distinctSequences';
console.time(label);
console.log(distinctSequences2(n));
console.timeLog(label, 'distinctSequences2');
console.log(distinctSequences(n));
console.timeEnd(label);
// console.log(distinctSequences(n));