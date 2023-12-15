/*
* auther yeling
* 1224. 最大相等频率
* 
*/
/**
 * @param {number[]} nums
 * @return {number}
 */
//暴力解法 n^2
//27 / 45
//29 / 45
//31 / 45
//36 / 45 个通过测试用例 TLE
var maxEqualFreq2 = function (nums) {
    let max = 1;
    let n = nums.length;
    for (let i = 1; i < n; i++) {
        let cache = new Map();
        for (let k = 0; k <= i; k++) {
            let temp = cache.get(nums[k]);
            if (temp == null) {
                temp = 0;
            }
            temp++;
            cache.set(nums[k], temp);
        }

        let valueMap = new Map();
        cache.forEach((value, key) => {
            let temp = valueMap.get(value);
            if (temp == null) {
                temp = 0;
            }
            temp++;
            valueMap.set(value, temp);
        })
        //console.log(cache);
        if (valueMap.size == 2) {
            let array = [];
            valueMap.forEach((value, key) => {
                array.push(key);
            })
            //console.log(array);
            if ((array[0] == 1 && valueMap.get(array[0]) == 1) ||
                (array[1] == 1 && valueMap.get(array[1]) == 1)) {
                max = Math.max(max, i + 1);
            }
            let maxSize = Math.max(array[0], array[1]);
            if (Math.abs(array[0] - array[1]) == 1 && valueMap.get(maxSize) == 1) {
                max = Math.max(max, i + 1);
            }
        } else if (valueMap.size == 1) {
            let array = [];
            valueMap.forEach((value, key) => {
                array.push(key);
            })
            //console.log(array);
            if (array[0] == 1 || valueMap.get(array[0]) == 1) {
                max = Math.max(max, i + 1);
            }
        }
        //console.log(max);
    }
    return max;
};

var maxEqualFreq = function (nums) {
    let max = 1;
    let n = nums.length;
    let cache = new Map();
    let valueMap = new Map();
    for (let i = 0; i < n; i++) {

        let temp = cache.get(nums[i]);
        if (temp == null) {
            temp = 0;
        }
        temp++;
        cache.set(nums[i], temp);

        if (valueMap.has(temp - 1)) {
            if(valueMap.get(temp - 1) - 1 == 0) {
                valueMap.delete(temp - 1);
            } else {
                valueMap.set(temp - 1, valueMap.get(temp - 1) - 1);
            }
        }

        let tempValue = valueMap.get(temp);
        if (tempValue == null) {
            tempValue = 0;
        }
        tempValue++;
        valueMap.set(temp, tempValue);

        //console.log(cache);
        if (valueMap.size == 2) {
            let array = [];
            valueMap.forEach((value, key) => {
                array.push(key);
            })
            //console.log(array);
            if ((array[0] == 1 && valueMap.get(array[0]) == 1) ||
                (array[1] == 1 && valueMap.get(array[1]) == 1)) {
                max = Math.max(max, i + 1);
            }
            let maxSize = Math.max(array[0], array[1]);
            if (Math.abs(array[0] - array[1]) == 1 && valueMap.get(maxSize) == 1) {
                max = Math.max(max, i + 1);
            }
        } else if (valueMap.size == 1) {
            let array = [];
            valueMap.forEach((value, key) => {
                array.push(key);
            })
            //console.log(array);
            if (array[0] == 1 || valueMap.get(array[0]) == 1) {
                max = Math.max(max, i + 1);
            }
        }
        //console.log(max);
    }
    return max;
};



nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5]
nums = [2, 2, 1, 1, 5, 3, 3, 5]
nums = [1,1,1,2,2,2]
// nums = [10, 2, 8, 9, 3, 8, 1, 5, 2, 3, 7, 6]
// nums = [1, 2]
// nums = [1,1,1,1,1,1];
// nums = [1, 1, 1, 2, 2, 2, 3, 3, 3]
console.log(nums);
console.log(maxEqualFreq2(nums));
console.log(maxEqualFreq(nums));
