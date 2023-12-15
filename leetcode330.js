/*
* auther yeling
* 330. 按要求补齐数组
* 贪心算法，既然要增加就增加最大的，从最小的开始计算
*/

//没有内存了 3 / 146 个通过测试用例

var minPatches = function (nums, n) {
    let count = 0;
    let allNum = new Array(n + 1);
    allNum.fill(0);
    allNum[0] = 1;
    dfs(allNum, nums, 0, 0);
    //console.log(allNum);
    while (true) {
        //贪心算法，既然要增加就增加最大的，从最小的开始计算
        let nextNum = 0;
        for (let i = 0; i < allNum.length; i++) {
            if (allNum[i] == 0) {
                nextNum = i;
                count++;
                break;
            }
        }
        if (nextNum == 0) {
            break;
        }
        for (let i = allNum.length - 1; i >= 0; i--) {
            if (i + nextNum <= n && allNum[i] == 1) {
                allNum[i + nextNum] = 1;
            }
        }
        allNum[nextNum] = 1;
        //console.log(`${nextNum}`)
        //console.log(`${nextNum} ${allNum}`);
    }
    return count;
};

let dfs = function (allNum, nums, index, preSum) {
    //console.log(`dfs ${index} ${preSum} ${allNum}`);
    if (preSum > allNum.length) {
        return;
    }
    allNum[preSum] = 1;
    if (index == nums.length) {
        return;
    }
    dfs(allNum, nums, index + 1, preSum + nums[index]);
    dfs(allNum, nums, index + 1, preSum);
}

//23 / 146 个通过测试用例，超时间
var minPatches2 = function (nums, n) {
    let count = 0;
    let allRange = [];
    let stack = new Array();
    for (let i = 0; i < nums.length; i++) {
        if(nums[i] > n) {
            break;
        }
        let len = stack.length;
        allRange.push({ start: nums[i], end: nums[i] });
        stack.push(nums[i]);
        for (let j = 0; j < len; j++) {
            allRange.push({ start: nums[i] + stack[j], end: nums[i] + stack[j] });
            stack.push(nums[i] + stack[j]);
        }
    }
    // console.log('allRange ==');
    // allRange.forEach((range) => {
    //     console.log(`${range.start} ${range.end}`);
    // })

    while (true) {
        //合并区间，从后向前合并
        for (let i = allRange.length - 2; i >= 0; i--) {
            if (allRange[i].end >= allRange[i + 1].start - 1) {
                allRange[i].end = Math.max(allRange[i].end, allRange[i + 1].end);
                allRange.splice(i + 1, 1)
            }
        }
        //只剩下一个区间返回
        if (allRange[allRange.length - 1].end >= n && allRange[allRange.length - 1].start == 1) {
            break;
        }

        console.log('allRange');
        allRange.forEach((range) => {
            console.log(`allRange ${range.start} ${range.end}`);
        })

        //贪心算法，既然要增加就增加最大的，从最小的开始计算
        let nextNum = 0;
        let len = allRange.length;
        if (allRange[0].start > 1) {
            allRange.unshift({ start: 1, end: 1 });
            nextNum = 1;
            for (let i = 1; i < allRange.length; i++) {
                allRange[i].end += nextNum;
            }
        } else {
            nextNum = allRange[0].end + 1;
            for (let i = 0; i < len; i++) {
                allRange[i].end += nextNum;
            }
        }
        count++;
        console.log(`nextNum ${nextNum}`)
    }
    return count;
};

//106 / 146
//PASS 贪心算法，从nums中取一个数字，还是单独增加一个数字
var minPatches3 = function (nums, n) {
    let count = 0;
    let numIndex = 0;
    let nextNum = 0;
    let end = 0;
    while (true) {
        let currPos = numIndex;
        for(let i = numIndex; i < nums.length; i++) {
            if(nums[i] <= end + 1) {
                end += nums[i];
                currPos = i + 1;
            } else {
                break;
            }
        }
        numIndex = currPos;
        if(end >= n) {
            break;
        }
        nextNum = end + 1;  
        count++;
        end += nextNum;
        console.log(`end ${end} nextNum ${nextNum} count ${count}  currN ${nums[numIndex]}`)
    }
    return count;
};

let nums = [1, 5, 10], n = 20;
// nums = [1, 4], n = 6;
//nums = [1,2,3,6,12]
console.time('begin');
//nums = [1,2,31], n = 2147483647;
// nums = [1,2,31], n = 128;
// nums = [1, 2, 2], n = 5;
// nums = [2], n = 2147483647;
// nums = [1,7,21,31,34,37,40,43,49,87,90,92,93,98,99],n = 12;
// nums = [2,3,9,10,13,15,15,18,19,20,21,30,33,34,47,48,66,70,71,71,82,97];
// n = 72;

// nums = [2,3,9,10,13,15,15,18,19,20,21,30,33,34,47,48,66]
// n = 21474836;

// nums = [10,30,36,42,50,76,87,88,91,92];
// n = 54;

console.log(`${nums} n ${n}`);
// console.log(minPatches(nums, n));
// console.log(minPatches2(nums, n));
console.log(minPatches3(nums, n));
console.timeEnd('begin');