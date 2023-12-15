/*
* auther yeling
* 
* 446. 等差数列划分 II - 子序列
* 动态规划，记录以I为终点的等差数列数量和差值
* dp[i]表示以I为终点的等差数列数量
*/

/**
 * @param {number[]} nums
 * @return {number}
 */
//35 / 101 个通过测试用例 内存超了
var numberOfArithmeticSlices2 = function (nums) {
    let n = nums.length;
    if (n < 3) {
        return 0;
    }
    let dp = new Array(n).fill(0).map(() => new Array());
    let AriData = function (count, delta) {
        this.count = count;
        this.delta = delta;

        this.toString = () => {
            return this.count + ' ' + this.delta;
        }

    }
    let sum = 0;
    for (let i = 1; i < nums.length; i++) {
        //计算当前的
        for (let j = 0; j < i; j++) {
            dp[j].forEach((item) => {
                if (nums[i] - nums[j] == item.delta) {
                    sum += 1;
                    dp[i].push(new AriData(item.count + 1, item.delta));
                }
            })
            //计算备选的
            dp[i].push(new AriData(0, nums[i] - nums[j]));
        }
        //console.log(`${i} ${sum} ${dp[i].length} ${dp[i]}`);
    }
    return sum;
};

//PASS
var numberOfArithmeticSlices = function (nums) {
    let n = nums.length;
    if (n < 3) {
        return 0;
    }
    //map delta count
    let dp = new Array(n).fill(0).map(() => new Map());

    let sum = 0;
    for (let i = 1; i < nums.length; i++) {
        //计算当前的
        for (let j = 0; j < i; j++) {
            dp[j].forEach((value, key) => {
                if (nums[i] - nums[j] == key) {
                    sum += value;
                    if (dp[i].has(key)) {
                        dp[i].set(key, value + dp[i].get(key));
                    } else {
                        dp[i].set(key, value);
                    }
                }
            })
            //计算备选的
            let delta = nums[i] - nums[j];
            if (dp[i].has(delta)) {
                dp[i].set(delta, 1 + dp[i].get(delta));
            } else {
                dp[i].set(delta, 1);
            }
        }
        //console.log(`${i} ${sum} ${dp[i].size} ${dp[i]}`);
        //console.log(dp[i]);
    }
    return sum;
};

nums = [2, 4, 6, 8, 10] //7
nums = [2,4,6,8] //3
// nums = [7,7,7,7,7]
// console.log(numberOfArithmeticSlices3(nums));
console.log(numberOfArithmeticSlices(nums));