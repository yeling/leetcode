/*
* auther yeling
* 873. 最长的斐波那契子序列的长度
* 
*/

/**
 * @param {number[]} arr
 * @return {number}
 */
var lenLongestFibSubseq = function (arr) {
    let cache = new Map();
    arr.forEach((item) => {
        cache.set(item, true);
    });
    let maxLen = 0;
    for (let i = 0; i < arr.length; i++) {
        for (let j = i + 1; j < arr.length; j++) {
            let len = 2, first = arr[i], second = arr[j];
            while (cache.has(first + second)) {
                len++;
                second = first + second;
                first = second - first;
            }
            if (len != 2) {
                maxLen = Math.max(maxLen, len);
            }
        }
    }
    return maxLen;
};

let arr = [1, 3, 7, 11, 12, 14, 18];
arr = [1,2,3,4,5,6,7,8]
console.log(lenLongestFibSubseq(arr));
