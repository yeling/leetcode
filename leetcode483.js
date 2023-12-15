/*
* auther yeling
* 483. 最小好进制
* 
*/

/**
 * @param {string} n
 * @return {string}
 */
//暴力方案
var smallestGoodBase = function(n) {
    let ret = BigInt(2);
    while(ret < n) {
        let temp = BigInt(n);
        let test = ret;
        while((temp - 1n)%test == 0n) {
            temp = (temp - 1n)/test;
        }
        if(temp == 0n) {
            break;
        }
        ret++;
        //console.log(ret);
    }
    return ret.toString();
};

let count = 0;
//15位，通过开根号进行裁剪
var smallestGoodBase2 = function(n) {
    let ret = BigInt(2);
    let find = false;
    while(ret * ret < n ) {
        let temp = BigInt(n);
        let test = ret;
        while(temp%test == 1n) {
            temp = (temp - 1n)/test;
        }
        if(temp == 0n) {
            find = true;
            break;
        }
        ret++;
        //console.log(ret);
    }
    if(find == false) {
        ret = BigInt(n) - 1n;
    }
    return ret.toString();
};

var smallestGoodBase3 = function(n) {
    let ret = BigInt(2);
    let find = false;
    while(ret * ret < BigInt(n - 1) ) {
        let temp = BigInt(n - 1);
        let test = ret;
        while(temp != 0n && temp%test == 0n) {
            temp = temp/test - 1n;
        }
        if(temp == 0n) {
            find = true;
            break;
        }
        ret++;
        //console.log(ret);
    }
    if(find == false) {
        ret = BigInt(n) - 1n;
    }
    return ret.toString();
};

let n = '28'
n = '112883900008390'
// n = '130'
// console.log(smallestGoodBase('4681'))
console.time('smallestGoodBase')
// console.log(smallestGoodBase(n))
console.timeLog('smallestGoodBase')
console.log(smallestGoodBase3(n))
console.timeEnd('smallestGoodBase')
// for(let i = 10; i < 300; i+=2) {
//     console.log(smallestGoodBase2(i))
// }
