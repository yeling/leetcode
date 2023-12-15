/*
* auther yeling
* 907. 子数组的最小值之和
* 
*/

/**
 * @param {number[]} arr
 * @return {number}
 */
//73 / 87 
var sumSubarrayMins = function(arr) {
    let MOD = 10 ** 9 + 7;
    let n = arr.length;
    let left = new Array(n).fill(-1);
    let right = new Array(n).fill(n);
    let stack = [];
    for(let i = 0; i < n; i++) {
        while (stack.length > 0 && arr[i] <= arr[stack[stack.length - 1]]) {
            right[stack.pop()] = i;
        }
        stack.push(i);
    }
    stack.length = 0;
    for(let i = n - 1; i >= 0; i--) {
        while (stack.length > 0 && arr[i] < arr[stack[stack.length - 1]]) {
            left[stack.pop()] = i;
        }
        stack.push(i);
    }
    let sum = 0; 
    for(let i = 0; i < n; i++) {
        sum += ((i - left[i]) * ( right[i] - i) * arr[i])%MOD;
    }
    // console.log(left);
    // console.log(right);
    // console.log(sum);
    return sum%MOD;

    
};
arr = [3,1,2,4] // 17
arr = [71,55,82,55]//593
arr = [2,3,2]
console.log(sumSubarrayMins(arr));