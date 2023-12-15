/*
* auther yeling
* 1643. 第 K 条最小指令
* 
*/

/**
 * @param {number[]} destination
 * @param {number} k
 * @return {string}
 */
var kthSmallestPath2 = function(destination, k) {
    let m = destination[0] + 1;
    let n = destination[1] + 1;
    let count = (num) => {
        let temp = 0;
        while(num > 0) {
            temp += num%2;
            num = Math.floor(num/2);
        }
        return temp;
    }
    //0 => H 1=>V
    let beginStr = new Array(m + n - 2).fill('0');
    for(let i = n-1; i < m + n - 2; i++) {
        beginStr[i] = '1';
    }
    let begin = Number.parseInt(beginStr.join(''), 2);
    console.log(`begin ${begin}`);
    for(let i = 1; i < k; i++) {
        //console.log(`${begin} ${begin.toString(2)}`);
        while(true) {
            begin++;
            let one = count(begin);
            if(one == m - 1) {
                break;
            }
        }
        
    }
    console.log(`end ${begin}`);
    beginStr = begin.toString(2).split(''); 
    let res = new Array(m + n - 2).fill(0);
    for(let i = m + n - 3; i >= 0; i--) {
        let last = beginStr.pop();
        if(last == '1') {
            res[i] = 'V';
        } else {
            res[i] = 'H';
        } 
    }
    return res.join('');
};

//找到最高的一位1需要变0的，低位补1，中间补0
var kthSmallestPath3 = function(destination, k) {
    let m = destination[0] + 1;
    let n = destination[1] + 1;
    
    let next = (currStr, m) => {
        //let res = [];
        let flag = false;
        let dstPos = -1;
        for(let i = currStr.length - 1; i >= 0; i--) {
            if(currStr[i] == '1') {
                flag = true;
            } else if(flag == true) {
                dstPos = i;
                break;
            }
        }
        //
        let one = 0;
        for(let i = 0; i < currStr.length; i++) {
            if(i < dstPos) {
                //res.push(currStr[i]);
                if(currStr[i] == '1') {
                    one++;
                }
            } else if(i == dstPos) {
                //res.push('1');
                currStr[i] = '1';
                one++;
            } else if(i <= currStr.length - (m - one)) {
                //res.push('0');
                currStr[i] = '0';
            } else {
                //res.push('1');
                currStr[i] = '1';
            }
        }
        return currStr;
    }
    //0 => H 1=>V
    let beginStr = new Array(m + n - 2).fill('0');
    for(let i = n-1; i < m + n - 2; i++) {
        beginStr[i] = '1';
    }
    for(let i = 1; i < k; i++) {
        //console.log(beginStr.join(''));
        beginStr = next(beginStr, m);
    }
    //console.log(beginStr.join(''));
    let res = new Array(m + n - 2).fill(0);
    for(let i = m + n - 3; i >= 0; i--) {
        let last = beginStr.pop();
        if(last == '1') {
            res[i] = 'V';
        } else {
            res[i] = 'H';
        } 
    }
    return res.join('');
};

//339 / 462
//459 / 462 个通过测试用例 TLE
//预先计算
var kthSmallestPath4 = function(destination, k) {
    let m = destination[0] + 1;
    let n = destination[1] + 1;
    
    let next = (currStr, m) => {
        //let res = [];
        let flag = false;
        let dstPos = -1;
        for(let i = currStr.length - 1; i >= 0; i--) {
            if(currStr[i] == '1') {
                flag = true;
            } else if(flag == true) {
                dstPos = i;
                break;
            }
        }
        //
        let one = 0;
        for(let i = 0; i < currStr.length; i++) {
            if(i < dstPos) {
                //res.push(currStr[i]);
                if(currStr[i] == '1') {
                    one++;
                }
            } else if(i == dstPos) {
                //res.push('1');
                currStr[i] = '1';
                one++;
            } else if(i <= currStr.length - (m - one)) {
                //res.push('0');
                currStr[i] = '0';
            } else {
                //res.push('1');
                currStr[i] = '1';
            }
        }
        return currStr;
    }

    //
    //0 => H 1=>V
    let beginStr = new Array(m + n - 2).fill('0');
    for(let i = n-1; i < m + n - 2; i++) {
        beginStr[i] = '1';
    }

    let beginNum = Number.parseInt(beginStr.join(''), 2);

    let beginNumStr = new Array(m+1).fill(0);
    beginNumStr[0] = 1;
    let a = m - 1, b = 1;
    let startPos = 1;
    for(let i = 1; i <= n; i++) {
        beginNumStr[i] = beginNumStr[i - 1] + a / b;
        a = a * (i + m - 1);
        b = b * (i + 1);
        if(k < beginNumStr[i]) {
            startPos = beginNumStr[i - 1];
            break;
        }
        beginNum = (beginNum << 1)
    }
    console.log(beginNumStr);

    //beginStr = beginNum.toString(2).split('');
    for(let i = beginStr.length - 1; i >= 0; i--) {
        beginStr[i] = beginNum%2 == 1 ? '1' : '0';
        beginNum = (beginNum >> 1);
    }

    console.log(beginStr.join('') + ' ' + Number.parseInt(beginStr.join(''), 2));
    for(let i = startPos; i < k; i++) {
        beginStr = next(beginStr, m);
        //console.log(beginStr.join('') + ' ' + Number.parseInt(beginStr.join(''), 2));
    }
    let res = new Array(m + n - 2).fill(0);
    for(let i = m + n - 3; i >= 0; i--) {
        let last = beginStr.pop();
        if(last == '1') {
            res[i] = 'V';
        } else {
            res[i] = 'H';
        } 
    }
    return res.join('');
};

//339 / 462
//459 / 462 个通过测试用例 TLE
//二分
var kthSmallestPath = function(destination, k) {
    let m = destination[0];
    let n = destination[1];
    //0 => H 1=>V
    let sum = m + n;
    let dp = new Array(sum + 1).fill(0).map(() => new Array(sum + 1).fill(0));
    for(let i = 0; i <= sum; i++) {
        for(let j = 0; j <= i; j++) {
            if(j == 0 || j == i) {
                dp[i][j] = 1;
            } else {
                dp[i][j] = dp[i-1][j] + dp[i-1][j-1];
            }
        }
    }
    //console.log(dp.join('\n'));
    //console.log(dp[4][2]);

    let res = [];
    let dst = k;
    let index = 1;
    //0 => H 1=>V
    let zero = n;
    while(index <= sum) {
        //console.log(dp[sum][n - index])
        if(zero > 0 &&  dst <= dp[sum - index][zero - 1]) {
            res.push('H');
            zero--;
        } else {
            res.push('V');
            if(dst > 0) {
                dst -= dp[sum - index][zero - 1];
            }
        }
        index++;
        //console.log(`${dst} ${res}`);
    }
    return res.join('');
    //
};

// destination = [5,6], k = 421;
// destination = [3,2], k = 3;

destination = [15,15]
k = 155117520
// k = 45330676
// destination = [9,9]
// k = 1005

let label = 'kthSmallestPath';
console.time(label);
console.log(kthSmallestPath3(destination, k));
console.timeLog(label, 'kthSmallestPath2');
console.log(kthSmallestPath(destination, k));
console.timeEnd(label);
