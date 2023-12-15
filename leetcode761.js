/*
* auther yeling
* 761. 特殊的二进制序列
* 把0，1理解成()，括号配对
*/

/**
 * @param {string} s
 * @return {string}
 */
var makeLargestSpecial = function(s) {

    let dfs = function(str, start ,end) {
        if(start > end) {
            return '';
        }
        let count = 0;
        let last = start;
        let sub = new Array();
        for(let i = start; i < end; i++) {
            if(str.charAt(i) == '1') {
                count++;
            } else {
                count--;
                if(count == 0) {
                    sub.push('1' + dfs(str,last + 1,i) + '0');
                    last = i + 1;
                }
            }
        }
        sub.sort((a,b) => {return b.localeCompare(a)});
        //console.log(sub);
        return sub.join('');
    }
    return dfs(s,0,s.length);
};

S = "11011000";
// S = "1010";
console.log(makeLargestSpecial(S));
