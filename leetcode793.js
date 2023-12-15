/*
* auther yeling
* 793. 阶乘函数后 K 个零
* 
*/

/**
 * @param {number} k
 * @return {number}
 */
var preimageSizeFZF = function(k) {
    let num = 0;
    let count = 0;
    while(count < k) {
        num += 5;
        count++;
        let temp = num/5;
        while(temp%5 == 0) {
            temp = temp/5;
            count++;
        }
        console.log(`${count} ${num}`);
    }
    //console.log(`${count} ${num}`);
    if(count == k) {
        return 5;
    } else {
        return 0;
    }
};

var preimageSizeFZF2 = function(k) {
    let num = 0;
    let count = 0;
    let add = 0;
    let last = 5;
    while(count < k) {
        num += 5;
        count++;
        let temp = num/5;
        if(temp%last == 0) {
            last = num;
            add++;
            count += add;
        }
        console.log(`${count} ${num} ${last} ${add}`);
    }
    //console.log(`${count} ${num}`);
    if(count == k) {
        return 5;
    } else {
        return 0;
    }
};

k = 11
console.time('preimageSizeFZF');
console.log(preimageSizeFZF(k));
console.timeLog('preimageSizeFZF', '1');
console.log(preimageSizeFZF2(k));
console.timeEnd('preimageSizeFZF');