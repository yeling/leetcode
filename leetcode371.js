/*
* auther yeling
* 
* 
*/

/**
 * @param {number} a
 * @param {number} b
 * @return {number}
 */
//-1 1
var getSum2 = function(a, b) {
    let as = a.toString(2);
    let bs = b.toString(2);
    console.log(`${as} ${bs}`);
    let i = as.length - 1, j = bs.length - 1,add = 0;
    let rs = '';
    while(i >= 0 || j >= 0) {
        let ai = 0,bj = 0;
        if(i >= 0) {
            ai = as[i];
        }
        if(j >= 0) {
            bj = bs[j];
        }
        
        if(ai & bj == 1) {
            rs = add + rs;
            add = 1;
        } else {
            let temp = ai | bj;
            if(temp == 0) {
                rs = add + rs;
                add = 0;
            } else if(temp == 1){
                if(add == 1) {
                    rs = '0' + rs;
                    add = 1;
                } else {
                    rs = temp + rs;
                }
            }
        }
        i--;
        j--; 
    }
    if(add == 1) {
        rs = add + rs;
    }
    // console.log(rs);
    return Number.parseInt(rs,2);
};

var getSum = function(a, b) {
    while (b != 0) {
        const carry = (a & b) << 1;
        a = a ^ b;
        b = carry;
    }
    return a;
};

// console.log(`${getSum(7,7)}`);
// console.log(`${getSum(6,7)}`);
// console.log(`${getSum(13,8)}`);
console.log(`${getSum(-1,1)}`);
