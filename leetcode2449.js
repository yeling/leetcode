/*
* auther yeling
* 2449. 使数组相似的最少操作次数
* 
*/

/**
 * @param {number[]} nums
 * @param {number[]} target
 * @return {number}
 */
var makeSimilar2 = function(nums, target) {
    let n = nums.length;
    nums.sort((a,b) => a - b);
    target.sort((a,b) => a - b);
    let diff = new Array(n).fill(0).map((value, index) => {
        return nums[index] - target[index];
    });
    console.log(nums);
    console.log(target);
    console.log(diff);
    let sum = 0;
    for(let i = 0; i < n; i++) {
        if(diff[i] > 0) {
            sum += diff[i];
        }
        //console.log(sum);
    }
    if(sum&1 == 1) {
        return (sum + 1)/2;
    } else {
        return sum/2;
    }
};

var makeSimilar = function(nums, target) {
    let n = nums.length;
    let a = new Array(2).fill(0).map(() => []), b = new Array(2).fill(0).map(() => []);
    for(let i = 0; i < nums.length; i++) {
        a[nums[i]%2].push(nums[i]);
        b[target[i]%2].push(target[i]);        
    }
    let sum = 0;
    a[0].sort((a,b) => a - b);
    a[1].sort((a,b) => a - b);
    b[0].sort((a,b) => a - b);
    b[1].sort((a,b) => a - b);
    for(let i = 0; i < a[0].length; i++) {
        if(a[0][i] > b[0][i]) {
            sum += (a[0][i] - b[0][i])/2;
        }
    }

    for(let i = 0; i < a[1].length; i++) {
        if(a[1][i] > b[1][i]) {
            sum += (a[1][i] - b[1][i])/2;
        }
    }
    return sum;
};

nums = [8,12,6], target = [2,14,10]

nums = [758,334,402,1792,1112,1436,1534,1702,1538,1427,720,1424,114,1604,564,120,578]
target = [1670,216,1392,1828,1104,464,678,1134,644,1178,1150,1608,1799,1156,244,2,892]
//645
console.log(makeSimilar2(nums, target));
console.log(makeSimilar(nums, target));