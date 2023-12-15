/*
* auther yeling
* 639. 解码方法 II
* 
*/

/**
 * @param {string} s
 * @return {number}
 */
// AC
let MOD = 10 ** 9 + 7;
var numDecodings = function (s) {
    let n = s.length;
    let dp = new Array(n).fill(0);

    let calc = (w) => {
        console.log(`calc ${w}`);
        if (w.length == 1) {
            let ret = 0;
            switch (w) {
                case '0':
                    ret = 0;
                    break;
                case '*':
                    ret = 9;
                    break;
                default:
                    ret = 1;
                    break;
            }
            return ret;
        } else if (w.length == 2) {
            if (isNaN(w)) {
                //含有*
                if (w[0] == '*' && w[1] == '*') {
                    return 15;
                } else if (w[0] == '*') {
                    if (w[1] > '6') {
                        return 1;
                    } else {
                        return 2;
                    }
                } else if (w[1] == '*') {
                    if (w[0] == '0' || w[0] > '2') {
                        return 0;
                    } else if (w[0] == '1') {
                        return 9;
                    } else if (w[0] == '2') {
                        return 6;
                    }
                }
            } else if (Number(w) <= 26 && Number(w) >= 1) {
                return 1;
            } else {
                return 0;
            }

        }
    }
    for (let i = 0; i < n; i++) {
        if (i == 0) {
            dp[i] = calc(s.substring(0, 1));
        } else {
            let curr = calc(s.substring(i, i + 1));
            if (curr != 0) {
                dp[i] = (dp[i] + (dp[i - 1] * curr) % MOD) % MOD;
            }
            //如果后一位为0，只能计算当前位置
            //如果前面一位是0，也只能计算当前位置
            if((i == n - 1 || s.charAt(i + 1) != '0') && (s.charAt(i - 1) != '0') ) {
                let curr2 = calc(s.substring(i - 1, i + 1));
                if (curr2 != 0) {
                    if (i == 1) {
                        dp[i] = (dp[i] + curr2) % MOD;
                    } else {
                        dp[i] = (dp[i] + (dp[i - 2] * curr2) % MOD) % MOD;
                    }
                }
            }
        }
        console.log(s.substring(0,i+1));
        console.log(dp);
    }
    return dp[n - 1];
};

s = "2*"
s = "6*"
s = "11106"
s = "**"
console.log(numDecodings(s));