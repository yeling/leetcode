/*
* auther yeling
* 6156. 得到 K 个黑块的最少涂色次数
* 
*/

/**
 * @param {string} blocks
 * @param {number} k
 * @return {number}
 */
var minimumRecolors = function(blocks, k) {
    
    let n = blocks.length;
    let ret = n;
    let left = 0, right = 0;
    let count = 0;
    let find = false;
    while(right < n) {
        //console.log(`${count}`)
        //移动right
        if(count < k || left == right) {
            if(blocks[right] == 'B') {
                count++;
            }
            right++;
        } else if(count == k) {
            find = true;
            //移动left
            if(blocks[left] == 'B') {
                ret = Math.min(ret,right - left);
                count--;
            } 
            left++;
        }
    }
    if(find == false) {
        return n - count;
    }
    //console.log(count);
    return ret - k;

};

var minimumRecolors = function(blocks, k) {
    let n = blocks.length;
    let ret = n;
    let left = 0, right = k;
    let count = 0;
    for(let i = 0 ; i < right; i++) {
        if(blocks[i] == 'B') {
            count++;
        }
    }
    ret = k - count;
    while(right < n) {
        if(blocks[right] == 'B') {
            count++;
        }
        if(blocks[left] == 'B') {
            count--;
        }
        ret = Math.min(ret,k - count);
        left++;
        right++;
    }
    return ret;
};

blocks = "WBBWWBBWBW", k = 7
blocks = "BBB", k = 2
// blocks = "BWWWBB", k = 6


console.log(minimumRecolors(blocks,k));