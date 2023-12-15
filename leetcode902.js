/*
* auther yeling
* 
* 
*/

/**
 * @param {string[]} digits
 * @param {number} n
 * @return {number}
 */
//59 / 84 个通过的测试用例
//81 / 84 个通过的测试用例
//PASS
var atMostNGivenDigitSet = function(digits, n) {
    let sum = 0;    
    digits = digits.map((value) => Number(value));

    let dfs = (curr, target) => {
        let cal = 10;
        let len = digits.length;
        let count = 1;
        //全排列        
        while(target >= cal) {            
            count++;
            cal *= 10;
        }
        let first = Math.floor(target * 10/cal);
        if(digits[curr] < first) {
            return Math.pow(len, count - 1);
        } else if(digits[curr] == first){
            let tempSum = 0;
            let nextTarget = target % (cal / 10);
            if(nextTarget < Math.floor(cal/100)) {
                return 0;
            }
            if(digits[curr] == target) {
                tempSum++;
            } else {
                for(let i = 0; i < digits.length; i++) {
                    tempSum += dfs(i, nextTarget);
                }
            }            
            return tempSum;
        } else {
            return 0;
        }
    }

    let cal = 10;
    let len = digits.length;
    let count = 1;
    //全排列        
    while(n >= cal) {
        sum += Math.pow(len, count);            
        count++;
        cal *= 10;
    }
    console.log(`${sum}`)
    for(let i = 0; i < digits.length; i++) {
        sum += dfs(i, n);
        console.log(`${sum}`)
    }

    return sum;
}
digits = ["1","3","5","7"], n = 3
// n = 3

// digits = ["1","4","9"], n = 1000000000

// digits = ["1","5","7","8"], n = 10212

console.log(atMostNGivenDigitSet(digits, n));

