/*
* auther yeling
* 946. 验证栈序列
* 
*/

/**
 * @param {number[]} pushed
 * @param {number[]} popped
 * @return {boolean}
 */
// 127 / 151
var validateStackSequences = function (pushed, popped) {
    let n = pushed.length;
    let stack = new Array();
    let pushIndex = 0, popIndex = 0;
    stack.push(pushed[pushIndex]);
    while (popIndex < n) {
        if (stack[stack.length - 1] != popped[popIndex]) {
            pushIndex++;
            if (pushIndex == n) {
                return false;
            } else {
                stack.push(pushed[pushIndex]);
            }
        } else {
            popIndex++;
            stack.pop();
        }
        console.log('stack ' + stack);
    }
    return true;
};

pushed = [1, 2, 3, 4, 5], popped = [4, 5, 3, 2, 1]
popped = [5,4,3,2,1]
// pushed = [1,2,3,4,5], popped = [4,3,5,1,2]

// pushed = [4,0,1,2,3]
// popped = [4,2,3,0,1]

console.log(pushed);
console.log(popped);
console.log(validateStackSequences(pushed, popped));
