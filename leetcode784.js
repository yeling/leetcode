/*
* auther yeling
* 
* 
*/
/**
 * @param {string} s
 * @return {string[]}
 */
var letterCasePermutation = function(s) {
    let res = [];
    let dfs = (index, pre) => {
        //console.log(`index ${index} pre ${pre}`);
        if(index == s.length) {
            res.push(pre);
            return;
        }
        let next = index + 1;
        while(next < s.length) {
            let code = s.charCodeAt(next);
            if(code >= 65 && code <= 90) {
                break;
            } else if(code >= 97 && code <= 122) {
                break;
            }
            next++;
        }
        
        //not choose
        let nextPre = pre + s.slice(index + 1, next + 1);
        dfs(next , nextPre);
        //choose
        pre += s.slice(index + 1, next);
        let code = s.charCodeAt(next);
        if(code > 58) {
            if(code <= 90) {
                pre += String.fromCharCode(code + 32);
            } else if(code <= 122){
                pre += String.fromCharCode(code - 32);
            }
            dfs(next, pre);
        }
    }
    dfs(-1,'');
    return res;
};

s = "a1b1c"
console.log(letterCasePermutation(s));

