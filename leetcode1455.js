/*
* auther yeling
* 
* 
*/

/**
 * @param {string} sentence
 * @param {string} searchWord
 * @return {number}
 */
var isPrefixOfWord = function(sentence, searchWord) {
    let array = sentence.split(' ');
    for(let i = 0; i < array.length; i++) {
        if(array[i].startsWith(searchWord)) {
            return i+1;
        }
    }
    return -1;
};

sentence = "i love eating burger", searchWord = "burg"
console.log(isPrefixOfWord(sentence,searchWord))

