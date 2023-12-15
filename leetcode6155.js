/*
* auther yeling
* 6155. 找出数组的第 K 大和
* 
*/

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
//7 / 111 个通过测试用例
var kSum2 = function (nums, k) {

    let insert = (stack, curr) => {
        //console.log(stack);
        let left = 0, right = stack.length - 1;
        let middle = 0;
        while(left < right) {
            middle = left + Math.floor((right - left)/2);
            if(stack[middle] < curr) {
                right = middle - 1;
            } else {
                left = middle + 1;
            }
        }
        stack.splice(left,0,curr);
        //console.log(stack);
        
    } 

    let dfs = (nums, index, preSum, sumStack, k) => {
        //console.log(sumStack);
        if (index == nums.length) {
            sumStack.push(preSum);
            if(sumStack.length > k) {
                sumStack.sort((a,b) => b - a);
                sumStack.pop();
            }
            return;
        }
        dfs(nums, index + 1, preSum, sumStack, k);
        dfs(nums, index + 1, preSum + nums[index], sumStack, k);
    }
    let stack = new Array();
    dfs(nums, 0, 0, stack, k);

    stack.sort((a,b) => b - a);
    //console.log(stack);
    let res = null;
    while(k > 0) {
        res = stack.shift();
        k--;
    }
    return res;

};

//34 / 111 个通过测试用例 二分插入 TLE
var kSum3 = function (nums, k) {
    nums.sort((a,b) => b - a);

    let insert = (stack, curr) => {
        // console.log(stack);
        // console.log(curr);
        let left = 0, right = stack.length - 1;
        let middle = 0;
        while(left <= right) {
            middle = left + Math.floor((right - left)/2);
            if(stack[middle] < curr) {
                right = middle - 1;
            } else {
                left = middle + 1;
            }
        }
        stack.splice(left,0,curr);
        //console.log(stack);
        
    } 

    let dfs = (nums, index, preSum, sumStack, k) => {
        if (index == nums.length) {
            insert(sumStack,preSum);
            if(sumStack.length > k) {
                sumStack.pop();
            }
            return;
        }
        dfs(nums, index + 1, preSum, sumStack, k);
        dfs(nums, index + 1, preSum + nums[index], sumStack, k);
    }
    let stack = new Array();
    dfs(nums, 0, 0, stack, k);

    return stack[k - 1];
}

//20 / 110
var kSum = function (nums, k) {
    let sum = 0;
    let n = nums.length;
    //负数转换为正数，求出最大sum
    for(let i = 0; i < n; i++) {
        if(nums[i] >= 0) {
            sum += nums[i];
        } else {
            nums[i] = - nums[i];
        }
    }

    console.log(`sum ${sum}`);

    //二分枚举，一直到K
    nums.sort((a,b) => a - b);

    let dfs = (nums, index, preSum, sumStack, k) => {
        if(sumStack.length > k) {
            return;
        }
        if (index == nums.length) {
            sumStack.push(preSum);
            return;
        }
        dfs(nums, index + 1, preSum, sumStack, k);
        dfs(nums, index + 1, preSum + nums[index], sumStack, k);  
    }

    let stack = new Array();
    dfs(nums, 0, 0, stack, k);
    console.log(stack);


    return sum - stack[k - 1];
}


nums = [1, -2, 3, 4, -10, 12], k = 16

// nums = [1000,1001,1002,1003,1004,1005,1006,1007,1008,1009]
// k = 10

// nums = [153123449,-974739108,-408679566,-996444415,-978921261,805907128,-102259288,-397930077,51033052,-193994032,158654659,-486195972,-294264190,-65262667,375941242,-890038230,315970860,403847239,-32469129,-350561293,192113942,794248972,-632675681,434029943,746632801,500370163,164413366,346449701,473890512]
// nums = [153123449,-974739108,-408679566,-996444415,-978921261,805907128,-102259288,-397930077,51033052,-193994032,158654659,-486195972,-294264190,-65262667,375941242,-890038230,315970860,403847239,-32469129,-350561293,192113942,794248972,-632675681,434029943]

// k = 1619
// nums = [1, -2, 3, 4], k = 5
nums = [492634335,899178915,230945927]
nums = [4,8,2]
k = 2
console.time('kSum');
console.log(kSum3(nums, k));
console.timeLog('kSum','kSum3')
// console.log(kSum(nums, k));
console.timeEnd('kSum');