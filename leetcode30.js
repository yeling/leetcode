/* 30. 串联所有单词的子串
给定一个字符串 s 和一些 长度相同 的单词 words 。
找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。
注意子串要与 words 中的单词完全匹配，中间不能有其他字符 ，
但不需要考虑 words 中单词串联的顺序。
*/

/**
 * @param {string} s
 * @param {string[]} words
 * @return {number[]}
 */
 var findSubstring = function(s, words) {
    let result = new Array();
    let right = 0;
    let wordLen = words[0].length;
    let used = new Array(words.length);
    let allUsed = false;
    while(right < s.length) {
        let nextRight = right;
        used.fill(false);
        allUsed = false;
        while(nextRight < s.length && allUsed == false) {
            let temp = s.substring(nextRight,nextRight + wordLen);
            nextRight+=wordLen;
            let find = false;
            for(let i = 0; i< words.length; i++) {
                if(temp == words[i] & used[i] == false) {
                    used[i] = true;
                    find = true;
                    break;
                }
            }
            if(find == false) {
                break;
            }
        }
        allUsed = true;
        for(let i = 0; i < used.length; i++) {
            if(used[i] == false) {
                allUsed = false;
                break;
            }
        }
        //console.log(`wordset ${allUsed} ${used} ${right}`)
        if(allUsed == true) {
            result.push(right)
        }
        right++;
    }
    return result;
};

var findSubstring1 = function(s, words) {
    let result = new Array();
    let wordLen = words[0].length;
    let count = 0;
    let findByPosition = (startPos) => {
        let left = startPos, right = left;
        let originCache = new Map();
        for(let i = 0; i < words.length; i++) {
            if(originCache.has(words[i])) {
                originCache.set(words[i],originCache.get(words[i]) + 1);
            } else {
                originCache.set(words[i],1);
            }
        }
        let usedCache = new Map();
        originCache.forEach((value,key) => {
            //console.log(`${key} ${value}`) 
            usedCache.set(key,value);
        });
        let allUsed = false; 
        //right尽可能的走远
        while(right < s.length) {
            allUsed = false;
            let temp = s.substring(right,right + wordLen);
            if(usedCache.has(temp)) {
                if(usedCache.get(temp) > 0) {
                    usedCache.set(temp, usedCache.get(temp) - 1);
                    right += wordLen;
                    //判断是否结束
                    allUsed = true;
                    usedCache.forEach((value,key) => {
                        if(value > 0) {
                            allUsed = false;
                        } 
                    });
                    if(allUsed) {
                        result.push(left);
                    }
                } else {
                    //left向前走
                    let leftTemp = s.substring(left,left + wordLen);
                    usedCache.set(leftTemp, usedCache.get(leftTemp) + 1);
                    left += wordLen;
                }
            } else {
                //遇到了没有的单子left right对齐
                right += wordLen;
                left = right;
                originCache.forEach((value,key) => {
                    usedCache.set(key,value);
                });
            }
            usedCache.forEach((value,key) => {
                console.log(`${key} ${value}`) 
            });
            console.log(`=wordset ${allUsed} ${left} nr ${right}`)
            
        }
    }
    for(let i = 0; i < wordLen; i++) {
        findByPosition(i);
    }
    return result;
};


let s = 'barfoothefoobarman';
let words = ["foo","bar"];

// s = "wordgoodgoodgoodbestword";
// words = ["word","good","best","word"];

// s = "barfoofoobarthefoobarman"
// words = ["bar","foo","the"]

s = "aaa"
words = ["a","a"]

s = "aaaaaaaaaaaaaa"
words = ["aa","aa"]

// s = "lingmindraboofooowingdingbarrwingmonkeypoundcake"
// words = ["fooo","barr","wing","ding","wing"]

console.log(`${s} ${words}`)
let res = findSubstring(s,words);
console.log(res)
res = findSubstring1(s,words);
console.log(res)