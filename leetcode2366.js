/*
* auther yeling
* 2366. 将数组排序的最少替换次数
* 
*/

/**
 * @param {number[]} nums
 * @return {number}
 */
//19 / 47

var minimumReplacement2 = function (nums) {
    //1.单调栈，栈顶等于当前元素右侧的最小值，开始将栈中的数据分解
    //2.分解逻辑，a,b之间的任意个数，分解成 num/b > 1 , num - b，一直到num/b == 1, 剩余部分对半分 num/2 num/2+1
    let n = nums.length;
    let rightMin = new Array(n).fill(Number.MAX_SAFE_INTEGER);
    rightMin[n - 1] = nums[n - 1];
    let min = nums[n - 1];
    for (let i = n - 1; i >= 0; i--) {
        if (nums[i] <= min) {
            min = nums[i];
        }
        rightMin[i] = min;
    }
    //console.log(rightMin);

    let sum = 0;
    let stack = new Array();
    for (let i = 0; i < nums.length; i++) {
        stack.push(nums[i]);
        let temp = stack[stack.length - 1];
        if (temp == rightMin[i]) {
            let curr = rightMin[i];
            let currStack = new Array();
            while (stack[stack.length - 1] >= curr) {
                let temp = stack.pop();
                if (temp % curr == 0) {
                    sum += temp / curr - 1;
                    currStack.splice(0, 0, ...new Array(temp / curr).fill(curr));
                } else {
                    if (Math.floor(temp / curr) > 1) {
                        sum += Math.floor(temp / curr) - 1;
                        currStack.splice(0, 0, ...new Array(Math.floor(temp / curr) - 1).fill(curr));
                    }
                    temp = curr + temp % curr;
                    if (temp % 2 == 0) {
                        currStack.splice(0, 0, temp / 2, temp / 2);
                    } else {
                        currStack.splice(0, 0, Math.floor(temp / 2), Math.floor(temp / 2) + 1);
                    }
                    sum++;
                }
                curr = currStack[0];
                //console.log(sum);
            }
            stack.push(...currStack);
        }
        //console.log(sum);
    }
    console.log(stack);
    return sum;
};

//19 / 47
//20 / 47
var minimumReplacement3 = function (nums) {
    //1.从最后一个需要更改的元素开始分解
    //2.分解逻辑，a,b之间的任意个数，分解成 num/b > 1 , num - b，一直到num/b == 1, 剩余部分对半分 num/2 num/2+1
    //2.分解逻辑，29/7 可以分解成5个数字，需要扣除25-29，6。5个数字平分6，1个2，其他是1，所以分成 5 6 6 6 6
    let n = nums.length;
    let min = nums[n - 1];
    let lastIndex = -1;
    for (let i = n - 2; i >= 0; i--) {
        if (nums[i] > nums[i + 1]) {
            lastIndex = i;
            break;
        }
    }
    let sum = 0;
    let stack = nums.slice(0, lastIndex + 1);
    let curr = nums[lastIndex + 1];
    let currStack = new Array();
    while (stack.length > 0) {
        if (stack[stack.length - 1] < curr) {
            curr = stack.pop();
        } else {
            let temp = stack.pop();
            if (temp % curr == 0) {
                sum += temp / curr - 1;
                currStack.splice(0, 0, ...new Array(temp / curr).fill(curr));
            } else {
                if (Math.floor(temp / curr) > 1) {
                    sum += Math.floor(temp / curr) - 1;
                    currStack.splice(0, 0, ...new Array(Math.floor(temp / curr) - 1).fill(curr));
                }
                temp = curr + temp % curr;
                if (temp % 2 == 0) {
                    currStack.splice(0, 0, temp / 2, temp / 2);
                } else {
                    currStack.splice(0, 0, Math.floor(temp / 2), Math.floor(temp / 2) + 1);
                }
                sum++;
            }
            curr = currStack[0];
        }
        //console.log(sum);
    }
    stack.push(...currStack);

    console.log(stack);
    return sum;
};

var minimumReplacement = function (nums) {
    //1.从最后一个需要更改的元素开始分解    
    //2.分解逻辑，29/7 可以分解成5个数字，需要扣除25-29，6。5个数字平分6，1个2，其他是1，所以分成 5 6 6 6 6
    // 5 = 7 - (6/5 + 1)
    let n = nums.length;
    let min = nums[n - 1];
    let lastIndex = -1;
    for (let i = n - 2; i >= 0; i--) {
        if (nums[i] > nums[i + 1]) {
            lastIndex = i;
            break;
        }
    }
    let sum = 0;
    let stack = nums.slice(0, lastIndex + 1);
    let curr = nums[lastIndex + 1];    
    while (stack.length > 0) {
        if (stack[stack.length - 1] < curr) {
            curr = stack.pop();
        } else {
            let temp = stack.pop();
            if (temp % curr == 0) {
                sum += temp / curr - 1;                
            } else {
                let count = Math.floor(temp / curr) + 1;                
                sum += count - 1;
                let diff = curr * count - temp;
                if(diff%count != 0) {
                    curr = curr - (Math.floor(diff/count) + 1);
                } else {
                    curr = curr - Math.floor(diff/count);
                }
            }            
        }
        //console.log(sum);
    }    
    return sum;
};

nums = [5, 29, 7]
// nums = [3,10,3]
// nums = [1,2,3,4,5]
// nums = [3,10,5,3] //6
// nums = [7,6,15,6,11,14,10]//10
// nums = [1,13,15,2,5,14,12,17]
nums = [368,112,2,282,349,127,36,98,371,79,309,221,175,262,224,215,230,250,84,269,384,328,118,97,17,105,342,344,242,160,394,17,120,335,76,101,260,244,378,375,164,190,320,376,197,398,353,138,362,38,54,172,3,300,264,165,251,24,312,355,237,314,397,101,117,268,36,165,373,269,351,67,263,332,296,13,118,294,159,137,82,288,250,131,354,261,192,111,16,139,261,295,112,121,234,335,256,303,328,242,260,346,22,277,179,223]
//17748
// nums = [260,346,22]//27
console.log(minimumReplacement3(nums));
console.log(minimumReplacement(nums));