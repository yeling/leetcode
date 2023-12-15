/*
* auther yeling
* 
* 
*/

/**
 * @param {string[]} words
 * @return {string}
 */
var oddString = function(words) {
    let n = words[0].length;

    for(let i = 1; i < n; i++) {
        let diff1 = null;//[diff,count,lastIndex]
        let diff2 = null;
        for(let j = 0; j < words.length; j++) {
            let curr = words[j].charCodeAt(i) - words[j].charCodeAt(i - 1);
            if(diff1 == null) {
                diff1 = [];
                diff1[0] = curr;
                diff1[1] = 1;
                diff1[2] = j;
            } else if(diff1[0] == curr) {
                diff1[1]++;
                diff1[2] = j;
            } else if(diff2 == null) {
                diff2 = [];
                diff2[0] = curr;
                diff2[1] = 1;
                diff2[2] = j;
            } else if(diff2[0] == curr) {
                diff2[1]++;
                diff2[2] = j;
            }
            if(diff1 != null && diff2 != null) {
                if(diff1[1] == 1 && diff2[1] > 1) {
                    return words[diff1[2]];
                }
                if(diff1[1] > 1 && diff2[1] == 1) {
                    return words[diff2[2]];
                }
            }
        }
    }
    return words[0];
};

words = ["aaa","bob","ccc","ddd"]
words = ["adc","wzy","abc"]
console.log(oddString(words));

