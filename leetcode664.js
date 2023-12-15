/*
* auther yeling
* 664. 奇怪的打印机
* 
*/

/**
 * @param {string} s
 * @return {number}
 */
// 79 / 200
var strangePrinter = function(s) {
    let dfs = (str) => {
        if(str.length == 0) {
            return 0;
        } else if(str.length == 1) {
            return 1;
        }
        let table = new Array(26).fill(0);
        for(let i = 0; i < str.length; i++) {
            table[str.charCodeAt(i) - 97]++;
        }
        let max = 0;
        let maxPos = 0;
        for(let i = 0; i < table.length; i++) {
            if(table[i] > max) {
                max = table[i];
                maxPos = i;
            }
        }
        //以i为分界点求出子区间的长度
        let dstChar = String.fromCharCode([97 + maxPos]);
        //console.log(dstChar);
        let left = 0, right = 0;
        let sum = 1;
        while(right <= str.length) {
            if(right == str.length || str.charAt(right) == dstChar) {
                sum += dfs(str.substring(left,right));
                right++;
                left = right;
            } else {
                right++;
            }
        }
        return sum;
    }
    //合并连续相同字母
    let dstStr = '';
    for(let i = 0; i < s.length; i++) {
        if(dstStr.length == 0) {
            dstStr += s.charAt(i);
        } else if(dstStr.charAt(dstStr.length - 1) != s.charAt(i)) {
            dstStr += s.charAt(i);
        }
    }
    console.log(dstStr);
    return dfs(dstStr);
};

//双指针
var strangePrinter2 = function(s) {
    let left = 0, right = s.length - 1;
    let sum = 0;
    while(left <= right) {
        let curr = s.charAt(left);
        while(left <= right) {
            if(s.charAt(left) == curr) {
                left++;
            } else {
                break;
            }
        }
        while(left <= right) {
            if(s.charAt(right) == curr) {
                right--;
            } else {
                break;
            }
        }
        sum++;
    }
    return sum;
}
//动态规划
var strangePrinter3 = function(s) {
    let n = s.length;
    let dp = new Array(n).fill(0).map(() => new Array(n).fill(0));
    for(let i = n - 1; i >= 0; i--) {
        dp[i][i] = 1;
        for(let j = i + 1; j < n; j++) {
            //console.log(`${j} ${j + i}`);
            if(s.charAt(i) == s.charAt(j)) {
                dp[i][j] = dp[i+1][j];
            } else {
                let min = Number.MAX_VALUE;
                for(let k = i; k < j; k++) {
                    min = Math.min(min, dp[i][k] + dp[k + 1][j]);
                }
                dp[i][j] = min;
            }
        }
        // console.log(dp.join('\n'))
    }
    // console.log(dp.join('\n'))
    return dp[0][n-1];
}

s = "abcaba"
s = "baacdddaaddaaaaccbddbcabdaabdbbcdcbbbacbddcabcaaa"
// s = "bacdadacbdbcabdabdbcdcbacbdcabca"
// s = "bacdadacb"
// s = "bacdadac"
// s = "ab"
// console.log(strangePrinter(s));
// console.log(strangePrinter2(s));
console.log(strangePrinter3(s));