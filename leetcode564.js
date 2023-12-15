/*
* auther yeling
* 564. 寻找最近的回文数
* 分类讨论，一半的位置开始，分为等于，大于1，小于1，计算回文串，取距离最小的那个
*/

//163 / 217 个通过测试用例 TLE
var nearestPalindromic2 = function (n) {
    let left = BigInt(n) - 1n, right = BigInt(n) + 1n;
    while (true) {
        if (isHuiwen(left.toString())) {
            return left.toString();
        }
        if (isHuiwen(right.toString())) {
            return right.toString();
        }
        left = left - 1n;
        right = right + 1n;
    }


};

var isHuiwen = function (temp) {
    //console.log(`isHuiwen ${temp}`)
    let left = 0, right = temp.length - 1;
    while (left < right) {
        if (temp.charAt(left) != temp.charAt(right)) {
            return false;
        }
        left++;
        right--;
    }
    return true;
}

//PASS
var nearestPalindromic = function (n) {
    const LEN = new Array(15).fill(0).map((value,index) => 10n ** (BigInt(index) + 1n) - 1n);
    //console.log(LEN);
    
    let res = new Array(3).fill('');
    let pre = n.substring(0, Math.floor(n.length / 2));
    if (n.length % 2 == 1) {
        pre += n.charAt(Math.floor(n.length / 2));

        res[1] = (BigInt(pre) - 1n).toString();
        res[2] = (BigInt(pre) + 1n).toString();
        for (let i = pre.length - 2; i >= 0; i--) {
            pre += pre.charAt(i);
            res[1] += res[1].charAt(i);
            res[2] += res[2].charAt(i);
        }
        res[0] = pre;
        if(res[1].length < res[0].length || (res[1] == 0n && res[0].length >= 2)) {
            res[1] = LEN[res[0].length - 2];
        }
    } else {
        res[1] = (BigInt(pre) - 1n).toString();
        res[2] = (BigInt(pre) + 1n).toString();
        for (let i = pre.length - 1; i >= 0; i--) {
            pre += pre.charAt(i);
            res[1] += res[1].charAt(i);
            res[2] += res[2].charAt(i);
        }
        res[0] = pre;
        if(res[1].length < res[0].length || (res[1] == 0n && res[0].length >= 2)) {
            res[1] = LEN[res[0].length - 2];
        }
    }

    res = res.map((value) => BigInt(value));
    let dis = Number.MAX_VALUE;
    let ret = res[0];
    for(let i = 0; i < res.length; i++) {
        let temp = 0n;
        let resTemp = BigInt(res[i]);
        if(resTemp > BigInt(n)) {
            temp = resTemp - BigInt(n);
        } else if(resTemp < BigInt(n)) {
            temp = BigInt(n) - resTemp;
        }
        if(temp != 0n) {
            if(temp < dis) {
                dis = temp;
                ret = res[i];
            } else if(temp == dis && ret > res[i]) {
                ret = res[i];
            }
        }
    }
    //console.log(res);
    return ret.toString();

};

let n = "807045053224792883";
n = "807045053224";
n = "100";
console.log(n);
console.time('nearestPalindromic')
console.log(nearestPalindromic2(n));
console.timeLog('nearestPalindromic', '2');
console.log(nearestPalindromic(n));
console.timeEnd('nearestPalindromic');
// console.log(nearestPalindromic('100'));
