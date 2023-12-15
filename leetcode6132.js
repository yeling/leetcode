/*
* auther yeling
* 
* 
*/


/**
 * @param {number[]} nums
 * @return {number}
 */
var minimumOperations = function(nums) {
    let ret = 0;
    nums.sort((a,b)=>a-b);
    let find = true;
    while(find) {
        find = false;
        let sub = 0;
        for(let i = 0; i < nums.length; i++) {
            if(nums[i] != 0 && find == false) {
                find = true;
                ret++;
                sub = nums[i];
            }
            nums[i] -= sub;
        }
    }
    //console.log(nums);
    return ret;
};

nums = [1,5,0,3,5]
console.log(minimumOperations(nums));