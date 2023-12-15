/*
* auther yeling
* 
* 
*/

/**
 * @param {string[]} words
 * @return {string[]}
 */
var stringMatching = function(words) {
    let res = new Set();
    let n = words.length;
    for(let i = 0; i < n; i++) {
        for(let j = i + 1; j < n; j++) {
            if(words[i].indexOf(words[j]) != -1){
                res.add(words[j]);
            }
            if(words[j].indexOf(words[i]) != -1) {
                res.add(words[i]);
            }
        }
    }
    return new Array(...res);
};

words = ["mass","as","hero","superhero"];
words = ["leetcoder","leetcode","od","hamlet","am"]
console.log(stringMatching(words));