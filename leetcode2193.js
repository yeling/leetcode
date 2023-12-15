/*
* auther yeling
* 2193. 得到回文串的最少操作次数
* 
*/

/**
 * @param {string} s
 * @return {number}
 */
//91 / 129
var minMovesToMakePalindrome = function(s) {
    let sum = 0;
    let n = s.length;
    let cache = s.split('');
    let left = 0, right = s.length - 1;
    while(left < Math.floor(n / 2)) {
        let tempR = right;
        while(cache[tempR] != cache[left] && left < tempR) {
            tempR--;
        }

        //只有一个字符了，需要移动到中间，n%2 == 1，该字符掠过，不模拟移动，可以最后移动
        if(left == tempR) {
            sum += Math.floor(n/2) - left;
            // console.log(`one char`);
            left++;
        } else {
            sum += right - tempR;
            let curr = cache[tempR];
            cache.splice(tempR,1);
            cache.splice(right,0,curr);
            left++;
            right--;
        }
        // console.log(sum);
        // console.log(cache);
        
    }
    return sum;
};

s = "letelt"
s = "skwunskegmdtutlgeunmlud" //62 60
// s = "skwunskegmdulgeunmlud" //52 
// s = "skwhhaaunskegmdtutlgtteunmuuludii"
s = "skwhhaaunskegmdtutlgtteunmuuludii" //169 163
console.log(minMovesToMakePalindrome(s));
// let arr = s.split('');
// arr.splice(1,0,'a')
// console.log(arr);