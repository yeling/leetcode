/*
* auther yeling
*318. 最大单词长度乘积
*给你一个字符串数组 words ，找出并返回 length(words[i]) * length(words[j]) 的最大值，
*并且这两个单词不含有公共字母。如果不存在这样的两个单词，返回 0 。
*/

var maxProduct = function(words) {
    let max = 0;
    let cache = [];
    //初始化cache数组
    for(let i = 0; i < words.length; i++) {
        cache[i] = new Array(27);
        cache[i].fill(false);
        let temp = words[i];
        let index = 0,count = 0;
        while(index < temp.length && count < 26) {
            //console.log(`${temp.charCodeAt(index)}`)
            if(cache[i][temp.charCodeAt(index) - 97] == false) {
                cache[i][temp.charCodeAt(index) - 97] = true;
                count++;
                if(count == 26) {
                    cache[i][26] = true;
                    break;
                }
            }
            index++;
        }
    }
    for(let i = 0; i < words.length; i++) {
        if(cache[i][26]) {
            continue;
        }
        for(let j = i + 1; j < words.length; j++) {
            if(cache[j][26]) {
                continue;
            }
            let tempA = cache[i];
            let tempB = cache[j];
            let find = true, k = 0;
            while(k < 26) {
                if(tempA[k] == true && tempB[k] == true) {
                    find = false;
                    break;
                }
                k++;
            }
            if(find) {
                max = Math.max(max,words[i].length * words[j].length);
            }
        }
    }

    return max;
};

let words = ["a","abe","abc","d","cd","bcd","abcd"]
console.log(maxProduct(words));

