/*
* auther yeling
* 6202. 使用机器人打印字典序最小的字符串
* 
*/
/**
 * @param {string} s
 * @return {string}
 */
var robotWithString = function(s) {
    let n = s.length;
    let cache = new Array(n).fill(false);    
    cache[n - 1] = false;
    let min = s.charCodeAt(n-1);
    for(let i = n - 2; i >= 0; i--) {
        if(min <= s.charCodeAt(i)) {
            cache[i] = true;
        } else {
            min = s.charCodeAt(i);
        }
    }
    console.log(cache);
    let stack = new Array();
    let res = new Array();
    for(let i = 0; i < n; i++) {
        if(cache[i]) {
            stack.push(s.charAt(i));
        } else {
            res.push(s.charAt(i));
        }
    }
    while(stack.length > 0) {
        res.push(stack.pop());
    }
    return res;

};

s = "zza"
s = "bccaeeaced"
console.log(robotWithString(s));
