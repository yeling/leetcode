/*
* auther yeling
* 
* 658. 找到 K 个最接近的元素
*/

/**
 * @param {number[]} arr
 * @param {number} k
 * @param {number} x
 * @return {number[]}
 */
//27 / 66
//25 / 66

var findClosestElements = function(arr, k, x) {
    let left = 0, right = arr.length - 1;
    let target = x;
    while(left <= right) {
        let mid = left + Math.floor((right - left)/2);
        if(target <= arr[mid]) {
            right = mid - 1;
        } else if(target > arr[mid]) {
            left = mid + 1;
        }
    }
    if(left == arr.length) {
        left = arr.length - 1;
    }
    console.log(left);
    let res = [];
    right = left;
    left = left - 1;
    while(res.length < k) {
        if(left >= 0 && right <= arr.length - 1) {
            if(x - arr[left] <= arr[right] - x) {
                res.splice(0,0,arr[left]);
                left--;
            } else {
                res.push(arr[right]);
                right++;
            }
        } else if(left == -1){
            res.push(arr[right]);
            right++;
        } else if(right >= arr.length) {
            res.splice(0,0,arr[left]);
            left--;
        }
    }
    
    return res;
};

arr = [1,2,3,4,5], k = 4, x = 3

arr = [1,2,3,4,5], k = 4, x = 0

// arr = [1,2], k = 1,x = 1

// arr = [0,0,1,2,3,3,4,7,7,8], k = 3, x = 5

// arr = [1,1,1,10,10,10], k =1, x = 9

console.log(findClosestElements(arr,k,x));
