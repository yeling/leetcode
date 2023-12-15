/*
* auther yeling
* 319. 灯泡开关
*/
/**
 * @param {number} n
 * @return {number}
 */
var bulbSwitch = function(n) {
    let state = new Array(n);
    state.fill(true);
    for(let i = 2; i <= n; i++) {
        let index = 0;
        while(index < n) {
            state[index + i - 1] = !state[index + i - 1];
            index += i;
        }
    }
    let count = 0;
    for(let i = 0; i < n; i++) {
        if(state[i] == true) {
            count++;
        }
    }
    return count;
};

//使用ArrayBuffer，每个开关表示一位
//33 / 35 个通过测试用例 前进一点点
var bulbSwitch2 = function(n) {
    let state = new ArrayBuffer(n/8 + 1);
    let stateView = new DataView(state);
    for(let i = 1; i <= n; i++) {
        let index = i - 1;
        while(index < n) {
            let temp = stateView.getUint8(index/8);
            let bit = 1 << (index%8);
            temp ^= bit;
            stateView.setUint8(index/8,temp);
            index += i;
            //console.log(`temp i ${i} ${(temp).toString(2)} `)
        }
    }
    let count = 0;
    for(let i = 0; i < n; i++) {
        let temp = stateView.getUint8(i/8);
        let bit = 1 << (i%8);
        temp &= bit;
        temp = temp >> i%8;
        if(temp == 1) {
            count++;
        }
        //console.log(`temp i ${i} ${(temp).toString(2)} `)
    }
    return count;
};

//求出一个数的因子，为奇数等开，偶数灯关
var bulbSwitch1 = function(n) {
    let count = 0;
    for(let i = 1; i <= n; i++) {
        let tnum = new Set();
        let len = Math.sqrt(i);
        //console.log(`i ${i} ${count}`);
        for(let j = 1; j <= len; j++) {
            if(i%j == 0) {
                tnum.add(j);
                tnum.add(i/j);
            }
        }
        if(tnum.size%2 == 1) {
            count++;
        }
    }
    return count;
};
let num = 99999999;
num = 9999;

// console.time('bulbSwitch')
// let res = bulbSwitch(num)
// console.log(`bulbSwitch ${res}`);
// console.timeEnd('bulbSwitch')

// console.time('bulbSwitch1')
// let res1 = bulbSwitch1(num)
// console.log(`bulbSwitch1 ${res1}`);
// console.timeEnd('bulbSwitch1')

//只有完全平方数的因子个数为奇数，其他的为偶数，只需要记录1-n完全平方数的个数
var bulbSwitch3 = function(n) {
    return Math.floor(Math.sqrt(n));
}

console.time('bulbSwitch2')
let res2 = bulbSwitch2(num)
console.log(`bulbSwitch2 ${res2}`);
console.timeEnd('bulbSwitch2')


console.time('bulbSwitch3')
let res3 = bulbSwitch3(num)
console.log(`bulbSwitch3 ${res3}`);
console.timeEnd('bulbSwitch3')

