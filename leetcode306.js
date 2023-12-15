/*
* auther yeling
* 306. 累加数
*/

/**
 * @param {string} num
 * @return {boolean}
 */
var isAdditiveNumber = function(num) {
    if(num.length < 3) {
        return false;
    }
    return dfs(num,0);
};

var dfs = function(num,start,num1,num2) {
    console.log(`dfs ${start} n1 ${num1} n2 ${num2}`)
    if(start == num.length) {
        return false;
    }
    if(num1 == null) {
        let endPos = start + (num.length - start)/2 + 1;
        for(let i = start + 1; i < endPos; i++) {
            let num1 = num.substring(start,i);
            //console.log(`${num1}`)
            if(dfs(num,i,num1)) {
                return true;
            }
        }
    } else if(num2 == null) {
        if(num.startsWith('0',start)) {
            return dfs(num,start + 1,num1,'0');
        }
        let endPos = start + (num.length - start)/2 + 1;
        for(let i = start + 1; i < endPos; i++) {
            let currNum = num.substring(start,i);
            if(dfs(num,i,num1,currNum)) {
                return true;
            }
        }
    } else {
        //计算num3
        let sum = bigNumAdd(num1,num2);
        //console.log(`sum ${sum} start ${start}`)
        if(num.startsWith(sum,start)) {
            if(start + sum.length == num.length) {
                return true;
            } else {
                return dfs(num,start + sum.length, num2, sum);
            }
        } else {
            return false
        }

    }

    return false;
}

var bigNumAdd = function(add1,add2) {
    let sum = '';
    let len = Math.max(add1.length,add2.length);
    let index = 0;
    let tempSum = 0;
    while(index < len) {
        let num1 = 0;
        if(add1.length - 1 - index >= 0) {
            num1 = Number.parseInt(add1.charAt(add1.length - 1 - index))
        }
        let num2 = 0;
        if(add2.length - 1 - index >= 0) {
            num2 = Number.parseInt(add2.charAt(add2.length - 1 - index))
        }
        tempSum += num1 + num2; 
        sum = tempSum%10 + sum;
        tempSum = Math.floor(tempSum/10);
        index++;
    }
    if(tempSum != 0) {
        sum = tempSum%10 + sum;
    }
    return sum;
}

// console.log(bigNumAdd('12','295'));
// let num1 = num.substring(0,1);
// console.log(num1);
let num = '112334';
num = '199100199';
num = '112358';
num = "101"
console.log(isAdditiveNumber(num));


