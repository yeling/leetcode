/*
* auther yeling
* 2334. 元素值大于变化阈值的子数组
* 
*/
/**
 * @param {number[]} nums
 * @param {number} threshold
 * @return {number}
 */
//54 / 68 个通过测试用例 超时
var validSubarraySize2 = function (nums, threshold) {
    let dp = [];
    nums.forEach((item, index) => {
        dp[index] = Math.floor(threshold / item) + 1;
    })
    console.log(dp);

    for (let i = 0; i < dp.length; i++) {
        let count = 0;
        let begin = i - dp[i];
        let end = i + dp[i];
        begin = Math.max(0, begin);
        end = Math.min(dp.length - 1, end);
        for (let j = begin; j <= end; j++) {
            if (dp[j] <= dp[i]) {
                count++;
                if (count >= dp[i]) {
                    return count;
                }
            } else {
                count = 0;
            }
        }
    }
    return -1;

};
//54 / 68 个通过测试用例 超时
//62 / 68 解答错误
//67 / 68 超时
var validSubarraySize3 = function (nums, threshold) {
    let dp = [];
    nums.forEach((item, index) => {
        dp[index] = Math.floor(threshold / item) + 1;
    })
    console.log(dp);

    for (let i = 0; i < dp.length; i++) {
        let count = 0;
        let begin = i - dp[i];
        let end = i + dp[i];
        //begin end不要
        begin = Math.max(-1, begin);
        end = Math.min(dp.length, end);
        if (end - 1 - begin >= dp[i]) {
            for (let j = begin + 1; j < end; j++) {
                if (dp[j] <= dp[i]) {
                    count++;
                    if (count >= dp[i]) {
                        return count;
                    }
                } else {
                    count = 0;
                }
                if (j > i && count == 0) {
                    break;
                }
            }
        }
    }
    return -1;
};

//54 / 68 个通过测试用例 超时
//62 / 68 解答错误
//67 / 68 超时 , 尝试双指针
var validSubarraySize4 = function (nums, threshold) {
    let dp = [];
    nums.forEach((item, index) => {
        dp[index] = Math.floor(threshold / item) + 1;
    })
    console.log(dp);

    for (let i = 0; i < dp.length; i++) {
        let count = 0;
        let begin = i - dp[i];
        let end = i + dp[i];
        //begin end不要，中心扩展法
        begin = Math.max(-1, begin);
        end = Math.min(dp.length, end);
        let left = i, right = i + 1, leftEnd = false, rightEnd = false;
        while ((leftEnd == false || rightEnd == false) && count < dp[i]) {
            if (dp[left] <= dp[i]) {
                left--;
                count++;
                if (left <= begin) {
                    leftEnd = true;
                }
            } else {
                leftEnd = true;
            }

            if (dp[right] <= dp[i]) {
                right++;
                count++;
                if (right >= end) {
                    rightEnd = true;
                }
            } else {
                rightEnd = true;
            }
        }
        if (count >= dp[i]) {
            return count;
        }
    }

    return -1;

};

//54 / 68 个通过测试用例 超时
//62 / 68 解答错误
//67 / 68 超时 , 尝试双指针
//单调栈，分别求出左右距离
//55 / 68 个通过测试用例
var validSubarraySize5 = function (nums, threshold) {
    let dp = [];
    nums.forEach((item, index) => {
        dp[index] = Math.floor(threshold / item) + 1;
    })
    console.log(dp);
    let right = new Array(dp.length);
    right.fill(0);
    let left = new Array(dp.length);
    left.fill(0);

    for (let i = 0; i < dp.length; i++) {
        let count = 0;
        let begin = i - dp[i];
        let end = i + dp[i];
        //begin end不要，分别求出左右
        begin = Math.max(-1, begin);
        end = Math.min(dp.length, end);
        for (let j = i - 1; j >= begin + 1; j--) {
            if (dp[j] <= dp[i]) {
                count++;
                if (count >= dp[i]) {
                    return count;
                }
            } else {
                break;
            }
        }
        left[i] = count;
    }

    for (let i = dp.length - 1; i >= 0; i--) {
        let count = 0;
        let begin = i - dp[i];
        let end = i + dp[i];
        //begin end不要，分别求出左右
        begin = Math.max(-1, begin);
        end = Math.min(dp.length, end);
        for (let j = i + 1; j < end; j++) {
            if (dp[j] <= dp[i]) {
                count++;
                if (count >= dp[i]) {
                    return count;
                }
            } else {
                break;
            }

        }
        right[i] = count;
    }

    console.log(`left ${left} right ${right}`);
    for (let i = 0; i < dp.length; i++) {
        let count = left[i] + right[i] + 1;
        if (count >= dp[i]) {
            return count;
        }
    }

    return -1;

};

//54 / 68 个通过测试用例 超时
//62 / 68 解答错误
//67 / 68 超时 , 尝试双指针
//单调栈，分别求出左右距离
//55 / 68 个通过测试用例
var validSubarraySize = function (nums, threshold) {
    let dp = [];
    nums.forEach((item, index) => {
        dp[index] = Math.floor(threshold / item) + 1;
    })
    console.log(dp);
    let right = new Array(dp.length);
    right.fill(0);
    let left = new Array(dp.length);
    left.fill(0);
    let stack = new Array();

    //单调栈，存储绝对下降的数字，如果遇到上升，计算count
    for (let i = 0; i < dp.length; i++) {
        if (stack.length == 0) {
            stack.push(i);
        } else {
            let head = stack.at(stack.length - 1);
            if (dp[head] > dp[i]) {
                stack.push(i);
            } else {
                let count = 0;
                while (dp[head] <= dp[i] && stack.length > 0) {
                    count += left[head] + 1;
                    stack.pop();
                    head = stack.at(stack.length - 1);
                }
                stack.push(i);
                left[i] = count;
            }
        }
    }

    //单调栈，存储绝对下降的数字，如果遇到上升，计算count
    stack.length = 0;
    for (let i = dp.length - 1; i >= 0; i--) {
        if (stack.length == 0) {
            stack.push(i);
        } else {
            let head = stack.at(stack.length - 1);
            if (dp[head] > dp[i]) {
                stack.push(i);
            } else {
                let count = 0;
                while (dp[head] <= dp[i] && stack.length > 0) {
                    count += right[head] + 1;
                    stack.pop();
                    head = stack.at(stack.length - 1);
                }
                stack.push(i);
                right[i] = count;
            }
        }
    }
    
    //console.log(`left ${left} right ${right}`);
    for (let i = 0; i < dp.length; i++) {
        let count = left[i] + right[i] + 1;
        if (count >= dp[i]) {
            return count;
        }
    }

    return -1;

};


let nums = [1, 3, 4, 2, 6], threshold = 6;
// nums = [20,10,6,5], threshold = 20;
// nums = [1, 3, 4, 3, 1], threshold = 6;

// nums = [3, 2, 3], threshold = 4;

console.log(validSubarraySize(nums, threshold));

