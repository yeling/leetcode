/*
* auther yeling
* 440. 字典序的第K小数字
* 
*/

/**
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
//10叉树的前序遍历，> N是结束

//29 / 69
//48 / 69 ,看样只能用数学方案了
var findKthNumber2 = function(n, k) {
    let stack = new Array();
    let count = 0;
    let num = 0;

    while(true) {
        if(stack.length == 0) {
            for(let i = 9; i >= 1; i--) {
                stack.push(i);
            }
        } else {
            num = stack.pop();
            count++;
            if(count == k) {
                return num;
            }
            //没有child
            if(num * 10 > n) {
                continue;
            } else {
                num = num * 10;
                let begin = Math.min(num+9,n);
                for(let i = begin; i >= num; i--) {
                    stack.push(i);
                }
            }
        }
        //console.log(stack);
    }
};

//跳层，理论上每层都可以跳
var findKthNumber = function(n, k) {
    let stack = new Array();
    let count = 0;
    let num = 0;

    while(true) {
        if(stack.length == 0) {
            let skipNum = skip(n,k);
            count = skipNum[0];
            for(let i = 9; i >= skipNum[1]; i--) {
                stack.push(i);
            }
        } else {
            num = stack.pop();
            count++;
            if(count == k) {
                return num;
            }
            //没有child
            if(num * 10 > n) {
                continue;
            } else {
                num = num * 10;
                let begin = Math.min(num+9,n);
                for(let i = begin; i >= num; i--) {
                    stack.push(i);
                }
            }
        }
        //console.log(stack);
    }
};

var skip = function(n,k) {
    let sum = 0;
    let preSum = 0;
    let oneLen = 1, base = 1;
    while(sum < k) {
        preSum = sum;
        oneLen = base;
        while(oneLen <= n) {
            sum += Math.floor(oneLen/10/base);
            oneLen *= 10;
        }
        if(oneLen > n) {
            oneLen = Math.floor(oneLen/10)
            if(n >= oneLen/base * (base + 1)) {
                sum += oneLen/base;
            } else {
                sum += n - oneLen + 1;
            }
        }
        //console.log(sum);
        base++; 
    }
    let ret = [preSum, base - 1];
    //console.log(ret);
    return ret;
}

n = 100,k = 24
n = 304089173,k = 87099045
// console.log(skip(100,2));
console.log('findKthNumber2 ' + findKthNumber2(n,k));
console.log('findKthNumber ' + findKthNumber(n,k));