/*
* auther yeling
* 6158. 字母移位 II
* 
*/

/**
 * @param {string} s
 * @param {number[][]} shifts
 * @return {string}
 */
var shiftingLetters = function(s, shifts) {
    let cache = new Array();
    for(let i = 0; i < s.length; i++) {
        cache.push(s.charCodeAt(i) - 97);
    }
    //console.log(cache);

    for(let i = 0; i < shifts.length; i++) {
        for(let j = shifts[i][0]; j <= shifts[i][1]; j++) {
            if(shifts[i][2] == 0) {
                cache[j]--;
            } else {
                cache[j]++;
            }
        }
        //console.log(cache);
    }

    for(let i = 0; i < cache.length; i++) {
        let temp = cache[i];
        while(temp < 0 || temp >= 26) {
            if(temp < 0) {
                temp += 26;
            }
            if(temp >= 26) {
                temp -= 26;
            }
        }
        cache[i] = temp + 97;
    }
    //console.log(cache);
    return String.fromCharCode(...cache);
};

// let s = 'a';

s = "abc", shifts = [[0,1,0],[1,2,1],[0,2,1]]
// shifts = [[0,1,0]]
s = "dztz", shifts = [[0,0,0],[1,1,1]]
console.log(shiftingLetters(s,shifts));
