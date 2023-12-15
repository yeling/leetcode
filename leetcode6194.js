/*
* auther yeling
* 6194. 最小 XOR
* 
*/

/**
 * @param {number} num1
 * @param {number} num2
 * @return {number}
 */
var minimizeXor = function(num1, num2) {
    let oneNum2 = 0;
    let num3 = num1;
    while(num2 > 0) {
        if(num2%2 == 1) {
            oneNum2++;
        }
        num2 = Math.floor(num2/2);
    }
    let oneNum1 = 0;
    while(num1 > 0) {
        if(num1%2 == 1) {
            oneNum1++;
        }
        num1 = Math.floor(num1/2);
    }
    //console.log(`one ${oneNum1} ${oneNum2}`);
    //从高位开始去除0
    let num3Str = num3.toString(2).split('');
    //console.log(num3Str);
    if(oneNum1 >= oneNum2) {
        let dst = oneNum2;
        let resStr = new Array(num3Str.length).fill(0);
        for(let i = 0; i < num3Str.length; i++) {
            if(num3Str[i] == '1') {
                resStr[i] = '1';
                dst--;
            }
            if(dst == 0) {
                break;
            }
        }
        let res = Number.parseInt(resStr.join(''),2);
        //console.log(res);
        return res;
    } else {
        //低位0，变成1
        let dst = oneNum2 - oneNum1;
        let resStr = num3Str.map((value) => value);
        for(let i = num3Str.length - 1; i>= 0;  i--) {
            if(num3Str[i] == '0') {
                resStr[i] = '1';
                dst--;
            }
            if(dst == 0) {
                break;
            }
        }
        while(dst > 0) {
            resStr.splice(0,0,'1');
            dst--;
        }
        let res = Number.parseInt(resStr.join(''),2);
        //console.log(res);
        return res;
    }

};

let num1 =  1;
let num2 = 33;

// num1 =  3;
// num2 = 5;
console.log(minimizeXor(num1, num2));