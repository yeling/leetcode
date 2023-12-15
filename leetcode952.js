/*
* auther yeling
* 952. 按公因数计算最大组件大小
* 数据集有限，可以用质数打表法
*/

/**
 * @param {number[]} nums
 * @return {number}
 */

// 75 / 105 个通过测试用例 并查集超时
var largestComponentSize2 = function (nums) {
    let n = nums.length;
    let father = new Array(n);
    for (let i = 0; i < n; i++) {
        father[i] = i;
    }
    //查找father
    var find = function (father, u) {
        if (father[u] != u) {
            father[u] = find(father, father[u])
        }
        return father[u];
    }

    //合并
    var join = function (father, u, v) {
        let fu = find(father, u);
        let fv = find(father, v);
        if (fu != fv) {
            father[fu] = fv;
        }
    }

    var gcd = function (a, b) {
        if (b == 0) {
            return a;
        }
        return gcd(b, a % b);
    }

    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
            if (gcd(nums[i], nums[j]) > 1) {
                join(father, i, j);
            }
        }
    }

    //计算连通节点数目
    let rootMap = new Map();
    let maxCount = 0;
    for (let i = 0; i < father.length; i++) {
        //这里是节点合并
        let root = find(father, father[i])
        let count = rootMap.get(root);
        if (count == null) {
            count = 0;
        }
        rootMap.set(root, count + 1);
        maxCount = Math.max(maxCount, count + 1);
    }
    return maxCount;
};

let calcCount = 0;
//95 / 108
var largestComponentSize = function (nums) {
    let n = nums.length;
    let father = new Array(n);
    for (let i = 0; i < n; i++) {
        father[i] = i;
    }
    //查找father
    var find = function (father, u) {
        if (father[u] != u) {
            father[u] = find(father, father[u])
        }
        return father[u];
    }

    //合并
    var join = function (father, u, v) {
        let fu = find(father, u);
        let fv = find(father, v);
        if (fu != fv) {
            father[fu] = fv;
        }
    }

    let isPrime = function (num) {
        if (num == 1 || num == 2) {
            return true;
        }
        for (let i = 2; i * i <= num; i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }

    
    //console.log(allPrimes);
    let cacheMap = new Map();
    let maxNum = 0;
    nums.forEach((item,index) => {
        cacheMap.set(item,index);
        maxNum = Math.max(maxNum,item);
    });

    let allPrimes = [];
    for(let i = 2; i <= maxNum/2; i++) {
        if(isPrime(i)) {
            allPrimes.push(i);
        }
    }

    for(let i = 0; i < allPrimes.length; i++) {
        let first = -1, second = -1;
        let temp = allPrimes[i];
        let multi = 1;
        while(temp * multi <= maxNum) {
            if(cacheMap.has(temp * multi)) {
                second = first;
                first = cacheMap.get(temp * multi);
                if(second != -1 && first != -1) {
                    join(father, first, second);
                }
            }
            multi++;
        }
    }

    //计算连通节点数目
    let rootMap = new Map();
    let maxCount = 0;
    for (let i = 0; i < father.length; i++) {
        //这里是节点合并
        let root = find(father, father[i])
        let count = rootMap.get(root);
        if (count == null) {
            count = 0;
        }
        rootMap.set(root, count + 1);
        maxCount = Math.max(maxCount, count + 1);
    }
    return maxCount;
};



nums = [2, 3, 6, 7, 4, 12, 21, 39]
nums = [1,2,3,4,5,6,7,8,9]
nums = [83,99,39,11,19,30,31]
console.log(largestComponentSize2(nums));
console.log(largestComponentSize(nums));
console.log(calcCount)
