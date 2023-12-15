/*
* auther yeling
* 6157. 二进制字符串重新安排顺序需要的时间
* 
*/

/**
 * @param {string} s
 * @return {number}
 */
var secondsToRemoveOccurrences = function (s) {
    let n = s.length;
    let count = null;
    for (let i = n - 1; i >= 0; i--) {
        if (count == null && s.charAt(i) == '1') {
            count = 0;
        }
        if (s.charAt(i) == '0' && count != null) {
            count++;
        }
    }
    if (count == null) {
        count = 0;
    }
    return count;
};


var secondsToRemoveOccurrences2 = function (s) {
    let n = s.length;
    let count = 0;
    let end = false;
    while (true) {
        //console.log(s);
        end = true;
        for (let i = 1; i < n; i++) {
            if (s.charAt(i - 1) == 0 && s.charAt(i) == 1) {
                end = false;
                s =  s.substring(0,i-1) + '10' + s.substring(i+1);
                i++;
            }
        }
        if (end == false) {
            count++;
        } else {
            break;
        }
    }
    return count;
};
s = "0110101"
console.log(secondsToRemoveOccurrences2(s));