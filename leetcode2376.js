/*
* auther yeling
* 2376. 统计特殊整数
* 
*/


/**
 * @param {number} n
 * @return {number}
 */
var countSpecialNumbers2 = function (n) {
    let sum = 0;
    let check = function (num) {
        let arr = String(num).split('').map((value) => Number(value));
        let cache = new Array(10).fill(0);
        for (let i = 0; i < arr.length; i++) {
            if (cache[arr[i]] == 1) {
                return false;
            }
            cache[arr[i]] = 1;
        }
        return true;
    }
    for (let i = 1; i <= n; i++) {
        if (check(i)) {
            sum++;
        }
    }
    return sum;
};

//PASS，条件太多了
var countSpecialNumbers = function (n) {
    if (n <= 9) {
        return n;
    }
    const CACHE = [
        9,
        9 * 9,
        9 * 9 * 8,
        9 * 9 * 8 * 7,
        9 * 9 * 8 * 7 * 6,
        9 * 9 * 8 * 7 * 6 * 5,
        9 * 9 * 8 * 7 * 6 * 5 * 4,
        9 * 9 * 8 * 7 * 6 * 5 * 4 * 3,
        9 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2,
        9 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1,
    ];
    let arr = String(n).split('').map((value) => Number(value));
    console.log(arr);
    let sum = 0;
    let preNum = new Set();
    for (let i = 0; i < arr.length; i++) {
        if (i == arr.length - 1) {
            let curr = arr[0] - 1;
            let begin = 9;
            for (let j = 0; j < arr.length - 1; j++) {
                curr = curr * begin;
                begin--;
            }
            sum += curr;
        } else {
            sum += CACHE[i];
        }
    }
    console.log(`sum ${sum}`);
    preNum.add(arr[0]);
    for (let i = 1; i < arr.length; i++) {
        //中间的0略过去
        if (preNum.has(arr[i]) && arr[i] == 0) {
            break;
        }
        if (arr[i] == 0 && i != arr.length - 1) {
            preNum.add(arr[i]);
            continue;
        }

        let curr = arr[i];
        //
        if (i == arr.length - 1) {
            curr += 1;
        }

        let begin = 9 - i;
        preNum.forEach((value) => {
            if (value < arr[i] || (i == arr.length - 1 && value <= arr[i])) {
                curr--;
            }
        })

        for (let j = i + 1; j < arr.length; j++) {
            curr *= (begin - (j - i - 1));
        }
        sum += curr;
        //console.log(`${arr[i]} ${curr} ${sum}`);

        if (preNum.has(arr[i])) {
            break;
        }
        preNum.add(arr[i]);
        //console.log(preNum);
    }
    return sum;
};
n = 129;
n = 135;
n = 225;
n = 199;
n = 225;
n = 30430;
n = 187268091;//2659626  1843146
// n = 1808;
// n = 15;
// console.log(countSpecialNumbers2(n));
console.log(countSpecialNumbers(n));
