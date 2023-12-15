/*
* auther yeling
* 1808. 好因子的最大数目
* 
*/

/**
 * @param {number} primeFactors
 * @return {number}
 */
//计算3的倍数，a%3 余2，有1个2，余1有两个2.
//78 / 213
//115 / 213
//116 / 213 个通过测试用例 TLE
//146 / 213 个通过测试用例

var maxNiceDivisors2 = function(primeFactors) {
    if(primeFactors == 1) {
        return 1;
    }
    let MOD = 10 ** 9 + 7;
    let count = Math.floor(primeFactors/3);
    let res = 1;
    if(primeFactors%3 == 1) {
        res = 4;
        primeFactors -= 4;
        count--;
    } else if(primeFactors%3 == 2) {
        res = 2;
        primeFactors -= 2;
    }
    // res = res * Math.pow(3, count);
    while(count > 0) {
        res = (res * 3)%MOD;
        count--;        
    }
    return res%MOD;
};

//计算3的倍数，a%3 余2，有1个2，余1有两个2.
//78 / 213
//115 / 213
//116 / 213 个通过测试用例 TLE
//146 / 213 个通过测试用例
//160 / 213 个通过测试用例

var maxNiceDivisors3 = function(primeFactors) {
    if(primeFactors == 1) {
        return 1;
    }
    let MOD = 10n ** 9n + 7n;
    let count = Math.floor(primeFactors/3);
    let res = 1n;
    if(primeFactors%3 == 1) {
        res = 4n;
        primeFactors -= 4;
        count--;
    } else if(primeFactors%3 == 2) {
        res = 2n;
        primeFactors -= 2;
    }
    // res = res * Math.pow(3, count);
    let SPACE = 10000n;
    let TEN = 1n;
    let temp = SPACE;
   
    while(temp > 0) {
        TEN = (3n * TEN)%MOD;
        temp--;
    }
    let sum = 1n;
    count = BigInt(count)
    while(count > 0) {        
        if(count >= SPACE) {
            sum = (sum * TEN)%MOD;
            count = count - SPACE;
        } else {
            while(count > 0) {  
                sum = (sum * 3n)%MOD;
                count--;  
            }            
        }        
    }
    return (res * sum)%MOD;
};

var maxNiceDivisors = function(primeFactors) {
    if(primeFactors == 1) {
        return 1;
    }
    let MOD = 10n ** 9n + 7n;
    let count = Math.floor(primeFactors/3);
    let res = 1n;
    if(primeFactors%3 == 1) {
        res = 4n;
        primeFactors -= 4;
        count--;
    } else if(primeFactors%3 == 2) {
        res = 2n;
        primeFactors -= 2;
    }
    count = BigInt(count);
    res = res * (3n ** count);    
    return (res)%MOD;
};

label = 'primeFactors'
primeFactors = 8
// primeFactors = 1
primeFactors = 73 //572712676
primeFactors = 602753420 //216825759

console.time(label);
// console.log(maxNiceDivisors2(primeFactors))
console.timeLog(label, 'primeFactors');
console.log(maxNiceDivisors(primeFactors))
console.timeEnd(label);

