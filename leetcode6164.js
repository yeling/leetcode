/*
* auther yeling
* 
* 
*/

var maximumSum = function(nums) {
    //let cache = new Array();
    let c2 = new Map();
    let ret = -1;
    nums.forEach((item,index) => {
        let temp = 0;
        while(item > 0) {
            temp += item%10;
            item = Math.floor(item/10);
        }
        //cache[index] = temp;

        if(c2.get(temp) != null) {
            let sum = nums[index] + nums[c2.get(temp)];
            ret = Math.max(ret,sum);
            if(nums[index] > nums[c2.get(temp)]) {
                c2.set(temp,index);
            }
        } else {
            c2.set(temp,index);
        }
    });
    //console.log(cache);
    return ret;
};

nums = [18,43,36,13,7,81]
console.log(maximumSum(nums));