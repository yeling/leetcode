/*
* auther yeling
* 6108. 解密消息
* HashMap
*/

/**
 * @param {string} key
 * @param {string} message
 * @return {string}
 */
var decodeMessage = function(key, message) {
    let cache = new Map();
    let tempMap = new Set();
    let index = 0;
    for(let i = 0; i < key.length; i++) {
        let tempChar = key.charAt(i);
        if(tempChar != ' ' && tempMap.has(tempChar) == false) {
            cache.set(tempChar,index);
            index++;
            tempMap.add(tempChar);
        }
    }
    let result = '';
    for(let i = 0; i < message.length; i++) {
        let tempChar = message.charAt(i);
        if(tempChar != ' ') {
            let index = cache.get(tempChar);
            //console.log(index);
            result += String.fromCharCode(index + 'a'.charCodeAt(0));
        } else {
            result += ' '
        }
    }
    //console.log(cache);
    return result;
};

let  key = "the quick brown fox jumps over the lazy dog", message = "vkbs bs t suepuv";
// key = "abc";
console.log(decodeMessage(key,message));

