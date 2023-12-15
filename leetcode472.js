/*
* auther yeling
* 472. 连接词
* 
*/

/**
 * @param {string[]} words
 * @return {string[]}
 */
var findAllConcatenatedWordsInADict = function (words) {
    let cache = new Set(words);
    //words.sort((a, b) => a.length - b.length);

    let dfs = function (start, s1, subLen, subCount, cache) {
        //console.log(`dsf ${start} ${s1}`)
        if (subLen == s1.length) {
            if (subCount > 1) {
                return true;
            } else {
                return false;
            }
        }
        let ret = false;
        for (let i = start + 1; i <= s1.length; i++) {
            let tmp = s1.substring(start, i);
            if (cache.has(tmp)) {
                ret = dfs(i, s1, subLen + tmp.length, subCount + 1, cache);
            }
            if (ret == true) {
                return true;
            }
        }
        return false;
    }

    let res = [];
    for (let i = 0; i < words.length; i++) {
        if (dfs(0, words[i], 0, 0, cache)) {
            res.push(words[i]);
        }
    }
    return res;
};

words = ["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"]
words = ["catsdog", "cat", "cats","dog"];

console.log(findAllConcatenatedWordsInADict(words));