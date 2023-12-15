/*
* auther yeling
* 324. 摆动排序 II
* NAC 
*/
/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var wiggleSort1 = function(nums) {

}
var wiggleSort = function(nums) {
    if(nums.length == 1) {
        return;
    }
    let left = 0,right = 1, needBig = true;

    let swap = function(left,right) {
        let temp = nums[left];
        nums[left] = nums[right];
        nums[right] = temp;
    }
    
    while(left < nums.length) {
        if(needBig) {
            if(nums[left] > nums[right]) {
                swap(left,right);
                left++;
                right++;
                needBig = !needBig;
            } else if(nums[left] == nums[right]){
                while(nums[left] == nums[right] && right < nums.length) {
                    right++;
                }
                if(right == nums.length) {
                    // left = 0;
                    // right = 1;
                    // needBig = false;
                } else {
                    swap(left + 1,right);
                }
                swap(left + 1,right);
                right = left + 1;
            } else {
                left++;
                right++;
                needBig = !needBig;
            }
        } else {
            if(nums[left] < nums[right]) {
                swap(left,right);
                left++;
                right++;
                needBig = !needBig;
            } else if(nums[left] == nums[right]){
                while(nums[left] == nums[right] && right < nums.length) {
                    right++;
                }
                if(right == nums.length) {
                    swap(left,right - 1);
                    // left = 0;
                    // right = 1;
                    // needBig = false;
                } else {
                    swap(left + 1,right);
                    right = left + 1;
                }
                
            } else {
                left++;
                right++;
                needBig = !needBig;
            }
        }
        console.log(`needBig ${needBig} l ${left} r ${right} ${nums}`)
    }

};

let  nums = [1,5,1,1,6,4];
// nums = [1,3,2,2,3,1];
nums = [1,3,2,2,3,1];
// nums = [1,4,3,4,1,2,1,3,1,3,2,3,3];
// nums = [1,3,2,3,3];
nums = [2,1,3,3];
console.log(nums);
wiggleSort(nums);
console.log(nums);
