/*
* auther yeling
* 
* 
*/

/**
 * @param {string[]} queries
 * @param {string[]} dictionary
 * @return {string[]}
 */
var twoEditWords = function(queries, dictionary) {
    let res = [];
    for(let i = 0; i < queries.length; i++) {
        let src = queries[i];
        for(let j = 0; j < dictionary.length; j++) {
            let dst = dictionary[j];
            let diff = 0;
            for(let k = 0; k < src.length; k++) {
                if(src.charAt(k) != dst.charAt(k)) {
                    diff++;
                }
                if(diff > 2) {
                    break;
                }
            }
            if(diff <= 2) {
                res.push(queries[i]);
                break;
            }
        }
    }
    return res;
};

var twoEditWords2 = function(queries, dictionary) {
    

};

queries = ["word","note","ants","wood"], dictionary = ["wood","joke","moat"]
queries = ["yes"], dictionary = ["not"]
console.log(twoEditWords(queries, dictionary));
