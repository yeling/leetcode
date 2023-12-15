/*
* auther yeling
* 
* 
*/

/**
 * @param {number[]} nums
 * @return {number}
 */
//16 / 61 个通过测试用例
var longestNiceSubarray = function(nums) {
    let max = 1;
    
    let left = 0; right = 0;
    let cache = new Array(32).fill(0);
    while(right < nums.length) {
        //check
        let r = nums[right].toString(2);
        let find = false;
        //console.log(cache);
        //console.log(`${left} ${right}`);
        for(let i = r.length - 1; i >= 0; i--) {
            if(r.charAt(i) == '1' && cache[r.length - 1 - i] == 1) {
                find = true;
                break;
            }
        }
        if(find) {
            //left 左移
            let r = nums[left].toString(2);
            for(let i = r.length - 1; i >= 0; i--) {
                if(r.charAt(i) == '1') {
                    cache[r.length - 1 - i] = 0;
                }
            }
            left++;
        } else {
            //right右移
            for(let i = r.length - 1; i >= 0; i--) {
                if(r.charAt(i) == '1') {
                    cache[r.length - 1 - i] = 1;
                }
                
            }
            max = Math.max(max,right - left + 1);
            right++;
            
        }
        
    }
    return max;

};
nums = [3,1,5,11,13]
// nums = [1,3,8,48,10]
// nums = [3,8,48]
//
nums = [744437702,379056602,145555074,392756761,560864007,934981918,113312475,1090,16384,33,217313281,117883195,978927664]

console.log(longestNiceSubarray(nums));
