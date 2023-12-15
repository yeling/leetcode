/*
* auther yeling
* 
* 
*/

/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var maxPalindromes2 = function(s, k) {
    let cache = new Array(s.length).fill(false);
    for(let i = 0; i < s.length; i++) {
        let left = i, right = i + k - 1;
        let find = true;
        while (left < right) {
            if (s.charAt(left) != s.charAt(right)) {
                find = false;
                break;
            }
            left++;
            right--;
        }
        cache[i] = find;
    }
    console.log(cache)


};

var maxPalindromes = function(s, k) {
    let dp = new Array(s.length + k + 1).fill(0);
    for(let i = 0; i < s.length; i++) {
        dp[i + 1] = Math.max( dp[i + 1], dp[i]);
        let left = i, right = i + k - 1;
        let find = true;
        while (left < right) {
            if (s.charAt(left) != s.charAt(right)) {
                find = false;
                break;
            }
            left++;
            right--;
        }
        if(find) {
            dp[i + k] = Math.max(dp[i + k], dp[i] + 1);
        }
        

        left = i, right = i + k;
        find = true;
        while (left < right) {
            if (s.charAt(left) != s.charAt(right)) {
                find = false;
                break;
            }
            left++;
            right--;
        }
        if(find) {
            dp[i + k + 1] = Math.max(dp[i + k + 1], dp[i] + 1);
        }   
    }
    // console.log(dp)
    return dp[s.length]


};

s = "abaccdbbd", k = 3
s = "ttekddofxoxfqmnyw"
k = 1
console.log(maxPalindromes(s,k));

