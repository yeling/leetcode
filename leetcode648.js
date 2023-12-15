/*
* auther yeling
* 648. 单词替换
* 10分钟
*/
/**
 * @param {string[]} dictionary
 * @param {string} sentence
 * @return {string}
 */
var replaceWords = function(dictionary, sentence) {
    let dicSet = new Set(dictionary);
    let result = '';
    let i = 0; 
    while(i < sentence.length) {
        if(sentence.charAt(i) == ' ') {
            result += ' ';
            i++;
            continue;
        }
        let nextPos = sentence.indexOf(' ', i);
        if(nextPos == -1) {
            nextPos = sentence.length;
        }
        let subStr = sentence.substring(i,nextPos);
        let find = false;
        for(let j = 1; j <= subStr.length; j++) {
            if(dicSet.has(subStr.substring(0,j))) {
                result += subStr.substring(0,j);
                find = true;
                break;
            }
        }
        if(find == false) {
            result += subStr;
        }
        i = nextPos;
    }
    return result;
};

let dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery";
//"the cat was rat by the bat"
// dictionary = []
console.log(replaceWords(dictionary,sentence));