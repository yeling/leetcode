/*
* auther yeling
* 481. 神奇字符串
* 
*/


/**
 * @param {number} n
 * @return {number}
 */
//TLE
var magicalString2 = function(n) {
    let index = 3;
    let sum = 1;
    let stack = [];
    let currNum = 2;
    stack.push(2);
    
    let res = [1,2]
    while(index <= n) {
        let temp = stack.shift();
        // res.push(temp);
        // console.log(res);
        if(temp == 2) {
            if(currNum == 1) {
                stack.push(2,2);
                currNum = 2;
            } else if(currNum == 2) {
                stack.push(1,1);
                currNum = 1;
            }
        } else if(temp == 1) {
            sum++;
            if(currNum == 1) {
                stack.push(2);
                currNum = 2;
            } else if(currNum == 2) {
                stack.push(1);
                currNum = 1;
            }
        }
        index++;
    }
    return sum;
};


var magicalString = function(n) {
    let sum = 1;
    let cache = new Array(n).fill(0);
    let currNum = 2;
    let left = 3, right = 3;
    cache[0] = 1;
    cache[1] = 2;
    cache[2] = 2;

    while(left <= n) {
        let temp = cache[left - 1];
        if(temp == 2) {
            if(currNum == 1) {
                cache[right++] = 2;
                cache[right++] = 2;
                currNum = 2;
            } else if(currNum == 2) {                
                cache[right++] = 1;
                cache[right++] = 1;
                currNum = 1;
            }
        } else if(temp == 1) {
            sum++;
            if(currNum == 1) {
                cache[right++] = 2;                
                currNum = 2;
            } else if(currNum == 2) {
                cache[right++] = 1;
                currNum = 1;
            }
        }
        left++;
        // console.log(cache);
    }
    //console.log(`${left} ${right}`)

    return sum;
};

n = 10000
console.log(magicalString2(n));
console.log('magicalString');
console.log(magicalString(n));