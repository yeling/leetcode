/*
* auther yeling
* 
* 
*/

/**
 * @param {number[]} nums
 * @param {number[]} removeQueries
 * @return {number[]}
 */
// 30 / 44 个通过测试用例 TLE
var maximumSegmentSum = function (nums, removeQueries) {
    let n = nums.length;
    let ret = [];
    for (let i = 0; i < n; i++) {
        nums[removeQueries[i]] = 0;
        let maxSum = 0;
        let sum = 0;
        for (let j = 0; j < n; j++) {
            if (nums[j] != 0) {
                sum += nums[j];
                maxSum = Math.max(maxSum, sum);
            } else {
                sum = 0;
            }
        }
        ret.push(maxSum);
    }
    return ret;
};

// 35 / 44 个通过测试用例 TLE
// 40 / 42 个通过测试用例
// PASS
var maximumSegmentSum2 = function (nums, removeQueries) {
    let n = nums.length;
    //存储区间和，三元组[left,right,sum]
    let position = [];
    let sum = 0;
    //前缀和
    let preCache = new Array(n + 1).fill(0);
    for (let i = 0; i < n; i++) {
        preCache[i + 1] = preCache[i] + nums[i];
    }
    position.push([0, n - 1, preCache[n]]);
    let ret = [];
    let lastMaxPosition = 0;
    let maxChange = false;

    for (let i = 0; i < n; i++) {
        let dst = removeQueries[i];
        maxChange = false;
        //插入位置，改成二分查找
        let left = 0, right = position.length - 1;
        let target = dst;
        while (left <= right) {
            let mid = left + Math.floor((right - left) / 2);
            if (target < position[mid][0]) {
                right = mid - 1;
            } else if (target > position[mid][1]) {
                left = mid + 1;
            } else {
                left = mid;
                break;
            }
        }

        let j = left;
        let currPos = position[j];
        if (lastMaxPosition == position[j][0]) {
            maxChange = true;
        }
        let preSum = preCache[dst] - preCache[currPos[0]];
        let afterSum = position[j][2] - nums[dst] - preSum;
        position.splice(j, 1);
        if (dst < currPos[1]) {
            position.splice(j, 0, [dst + 1, currPos[1], afterSum]);
        }

        if (currPos[0] < dst) {
            position.splice(j, 0, [currPos[0], dst - 1, preSum]);
        }

        nums[dst] = 0;
        //console.log(position.join());
        if (maxChange) {
            let maxSum = 0;
            for (let j = 0; j < position.length; j++) {
                if (position[j][2] > maxSum) {
                    lastMaxPosition = position[j][0];
                    maxSum = position[j][2];
                }
            }
            ret.push(maxSum);
        } else {
            ret.push(ret[ret.length - 1]);
        }
    }
    return ret;
};

//并查集倒序
//28 / 44 个通过测试用例 TLE
//32 / 44 个通过测试用例 TLE
var maximumSegmentSum3 = function (nums, removeQueries) {
    let n = nums.length;
    let ret = [];
    let father = new Array(n).fill(-1);
    for (let i = 0; i < n; i++) {

        let temp = removeQueries[i];
        let pre = temp - 1, preFather = father[pre];
        while (pre >= 0 && father[pre] == preFather) {
            father[pre] = temp - 1;
            pre--;
        }

        let after = temp + 1, afterFather = father[after];
        while (after < n && father[after] == afterFather) {
            father[after] = temp + 1;
            after++;
        }
        nums[temp] = 0;
        //console.log(father);
        let maxSum = 0;
        let cache = new Map();
        for (let i = 0; i < n; i++) {
            let curr = cache.get(father[i]);
            if (curr == null) {
                curr = 0;
            }
            curr += nums[i];
            cache.set(father[i], curr);
            maxSum = Math.max(maxSum, curr);
        }

        ret.push(maxSum);
    }

    return ret;
}

//并查集倒序
//30 / 44 个通过测试用例
var maximumSegmentSum4 = function (nums, removeQueries) {
    let n = nums.length;
    let ret = [];
    let father = new Array(n).fill(0);
    let cache = new Map();
    let sum = 0;
    for (let i = 0; i < n; i++) {
        sum += nums[i];
    }
    cache.set(0, sum);

    for (let i = 0; i < n; i++) {

        let temp = removeQueries[i];
        cache.set(father[temp], cache.get(father[temp]) - nums[temp]);

        let pre = temp - 1, preFather = father[pre];
        while (pre >= 0 && father[pre] == preFather) {
            cache.set(preFather, cache.get(preFather) - nums[pre]);
            if (cache.get(temp - 1) == null) {
                cache.set(temp - 1, nums[pre]);
            } else {
                cache.set(temp - 1, cache.get(temp - 1) + nums[pre]);
            }
            father[pre] = temp - 1;
            pre--;
        }

        let after = temp + 1, afterFather = father[after];
        while (after < n && father[after] == afterFather) {
            cache.set(afterFather, cache.get(afterFather) - nums[after]);
            if (cache.get(temp + 1) == null) {
                cache.set(temp + 1, nums[after]);
            } else {
                cache.set(temp + 1, cache.get(temp + 1) + nums[after]);
            }
            father[after] = temp + 1;
            after++;
        }
        nums[temp] = 0;
        //console.log(father);
        //console.log(cache);
        let maxSum = 0;
        cache.forEach((value, key) => {
            maxSum = Math.max(maxSum, value);
        })
        ret.push(maxSum);
    }

    return ret;
};

//TLE
var maximumSegmentSum5 = function (nums, removeQueries) {
    let n = nums.length;
    //存储区间和，三元组[left,right,sum]
    let position = [];
    //前缀和
    let preCache = new Array(n + 1).fill(0);
    for (let i = 0; i < n; i++) {
        preCache[i + 1] = preCache[i] + nums[i];
    }
    position.push([0, n - 1, preCache[n]]);

    let ret = [];
    for(let i = 0; i < n; i++) {
        let dst = removeQueries[i];
        let maxSum = 0;
        for(let j = 0; j < position.length; j++) {
            if( dst >= position[j][0] && dst <= position[j][1]) {
                let currPos = position[j];
                let preSum = preCache[dst] - preCache[currPos[0]];
                let afterSum = position[j][2] - nums[dst] - preSum;

                position.splice(j,1);
                if(currPos[0] < dst) {
                    maxSum = Math.max(maxSum,preSum);
                    position.splice(j, 0, [currPos[0], dst - 1, preSum]);
                    //position.push([currPos[0], dst - 1, preSum]);
                    j++;
                }
                if(dst < currPos[1]) {
                    maxSum = Math.max(maxSum,afterSum);
                    position.splice(j, 0, [dst + 1, currPos[1], afterSum]);
                    //position.push([dst + 1, currPos[1], afterSum]);
                    j++;
                }
                j--;
            } else {
                maxSum = Math.max(maxSum,position[j][2])
            }
        }
        nums[dst] = 0;
        ret.push(maxSum);
        //console.log(position.join());
    }
    return ret;
}
// nums = [3,2,11,1], removeQueries = [3,2,1,0]
nums = [1, 2, 5, 6, 1], removeQueries = [0, 3, 2, 4, 1]
// console.log(maximumSegmentSum(nums,removeQueries))

// nums = [500,822,202,707,298,484,311,680,901,319,343,340]
// removeQueries = [6,4,0,5,2,3,10,8,7,9,1,11]

console.log(maximumSegmentSum3(nums, removeQueries))

// console.log(maximumSegmentSum4(nums,removeQueries))