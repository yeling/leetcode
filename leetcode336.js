/*
* auther yeling
* 336. 回文对
* 
*/

//时间复杂度O(n^2)
//135 / 136 个通过测试用例
var palindromePairs = function (words) {
    let res = [];
    for (let i = 0; i < words.length; i++) {
        for (let j = i + 1; j < words.length; j++) {
            if (isPalindrome(words[i] + words[j])) {
                res.push([i, j]);
            }
            if (isPalindrome(words[j] + words[i])) {
                res.push([j, i]);
            }
        }
    }
    return res;
};

var isPalindrome = function (str) {
    let left = 0, right = str.length - 1;
    while (left <= right) {
        if (str.charAt(left) != str.charAt(right)) {
            return false;
        }
        left++;
        right--;
    }
    return true;
}

//加了缓存之后，内存会超出
let cache = new Map();
var isPalindrome2 = function (str) {
    if(cache.get(str) != null) {
        return cache.get(str);
    }
    let left = 0, right = str.length - 1;
    let ret = true;
    while (left <= right) {
        if (str.charAt(left) != str.charAt(right)) {
            ret = false;
            break;
        }
        left++;
        right--;
    }
    cache.set(str,ret);
    return ret;
}

var palindromePairs2 = function (words) {
    let res = [];
    for (let i = 0; i < words.length; i++) {
        for (let j = i + 1; j < words.length; j++) {
            if (isPalindrome(words[i] + words[j])) {
                res.push([i, j]);
            }
            if (isPalindrome(words[j] + words[i])) {
                res.push([j, i]);
            }
        }
    }
    return res;
};

let words = ["abcd", "dcba", "lls", "s", "sssll"];

let res = palindromePairs(words);
console.log(`${res.join(' ')}`);
