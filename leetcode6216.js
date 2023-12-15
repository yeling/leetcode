/*
* auther yeling
* 
* 
*/

/**
 * @param {number[]} nums
 * @param {number[]} cost
 * @return {number}
 */
//TLE 41/44
var minCost3 = function (nums, cost) {
    let n = nums.length;
    let cache = new Array(n).fill(0).map((value, index) => {
        return [nums[index], cost[index]];
    });
    cache.sort((a, b) => a[1] - b[1]);

    let sum = Number.MAX_SAFE_INTEGER;
    for (let i = 0; i < n; i++) {
        let tempSum = 0;
        for (let j = 0; j < n; j++) {
            tempSum += Math.abs(cache[j][0] - cache[i][0]) * cache[j][1];
        }
        //console.log(`${i} ${tempSum} ${sum}`);
        sum = Math.min(sum, tempSum);
    }
    return sum;
}

//MLE 41/44
var minCost4 = function (nums, cost) {
    let n = nums.length;
    let cache = [];
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < cost[i]; j++) {
            cache.push(nums[i]);
        }
    }
    cache.sort((a, b) => {
        return a - b
    });
    let target = cache[Math.floor(cache.length / 2)];
    let sum = 0;
    for (let i = 0; i < n; i++) {
        sum += Math.abs(nums[i] - target) * cost[i];
    }
    return sum;
}
//42 / 44
//11883552859682560 溢出问题处理
//11883552859682561
var minCost = function (nums, cost) {
    let n = nums.length;
    nums = nums.map((value) => BigInt(value));
    cost = cost.map((value) => BigInt(value));

    let cache = new Array(n).fill(0).map((value, index) => {
        return [nums[index], cost[index]];
    });
    cache.sort((a, b) => {
        if (a[0] < b[0]) {
            return -1;
        } else if (a[0] == b[0]) {
            return 0;
        } else {
            return 1;
        }
    });
    let max = 0n;
    for (let i = 0; i < n; i++) {
        max += cost[i];
    }
    let target = 0n;
    let temp = 0n;
    let halfMax = 0n;
    if (max % 2n == 0) {
        halfMax = max / 2n;
    } else {
        halfMax = (max + 1n) / 2n;
    }

    for (let i = 0; i < n; i++) {
        temp += cache[i][1];
        if (temp >= halfMax) {
            target = cache[i][0];
            break;
        }
    }

    let sum = 0n;
    for (let i = 0; i < n; i++) {
        if (nums[i] > target) {
            sum += (nums[i] - target) * cost[i];
        } else {
            sum += (target - nums[i]) * cost[i];
        }

    }
    return sum;
}
let label = 'minCost2';
nums = [100, 3, 5, 2], cost = [2, 3, 7, 10]
// nums = [2,2,2,2,2], cost = [4,2,8,1,3]

// nums = [735103,366367,132236,133334,808160,113001,49051,735598,686615,665317,999793,426087,587000,649989,509946,743518]
// cost = [724182,447415,723725,902336,600863,287644,13836,665183,448859,917248,397790,898215,790754,320604,468575,825614]
//1907611126748

// nums = [735103,366367,132236]
// cost = [724182,447415,723725]

console.time(label);
console.log(minCost3(nums, cost));
console.timeLog(label, 'minCost2');
console.log(minCost(nums, cost));
console.timeEnd(label);