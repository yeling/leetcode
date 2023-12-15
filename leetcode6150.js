/*
* auther yeling
* 
* 
*/

/**
 * @param {string} pattern
 * @return {string}
 */
//暴力一下
var smallestNumber2 = function (pattern) {
    let check = function (num, pattern) {
        //只包含1-9，无重复数字
        let numArray = new Array(10).fill(0);
        let temp = num;
        while (temp > 0) {
            let index = temp % 10;
            if (index == 0) {
                return false;
            }
            if (numArray[index] == 1) {
                return false;
            }
            numArray[index] = 1;
            temp = Math.floor(temp / 10);
        }

        let last = num % 10;
        num = Math.floor(num / 10);
        for (let i = pattern.length - 1; i >= 0; i--) {
            let next = num % 10;
            if (pattern.charAt(i) == 'D') {
                if (next <= last) {
                    return false;
                }
            } else {
                if (next >= last) {
                    return false;
                }
            }
            last = next;
            num = Math.floor(num / 10);
        }
        return true;
    }
    let minArray = [12, 123, 1234, 12345, 123456, 1234567, 12345678, 123456789];
    let maxArray = [21, 321, 4321, 54321, 654321, 7654321, 87654321, 987654321];
    let min = minArray[pattern.length - 1];
    let max = maxArray[pattern.length - 1];

    for (let i = min; i <= max; i++) {
        if (check(i, pattern) == true) {
            return '' + i;
        }
    }
};

//dfs
var smallestNumber = function (pattern) {
    let dfs = function (num, pattern, index, used) {
        if(index == pattern.length) {
            return num;
        }
        let last = num % 10;
        if (pattern.charAt(index) == 'D') {
            if (last == 1) {
                return null;
            } else {
                for(let i = 1; last - i >= 1; i++) {
                    if(used[i] == true) {
                        continue;
                    }
                    used[i] = true;
                    let res = dfs(num * 10 + i, pattern, index + 1, used);
                    used[i] = false;
                    if(res != null) {
                        return res;
                    }
                }
            }
        } else {
            if (last == 9) {
                return null;
            } else {
                for(let i = last + 1; i <= 9; i++) {
                    if(used[i] == true) {
                        continue;
                    }
                    used[i] = true;
                    let res = dfs(num * 10 + i, pattern, index + 1, used);
                    used[i] = false;
                    if(res != null) {
                        return res;
                    }
                }
            }
        }

    }
    let used = new Array(10).fill(false);
    for (let i = 1; i <= 9; i++) {
        used[i] = true;
        let res = dfs(i, pattern, 0, used);
        used[i] = false;
        if (res != null) {
            return '' + res;
        }
    }
};

pattern = "IIIDIDDD";
// pattern = "IDIIDDI";
console.time('smallestNumber')
console.log(smallestNumber(pattern));
console.timeLog('smallestNumber','smallestNumber2')
console.log(smallestNumber2(pattern));
console.timeEnd('smallestNumber')