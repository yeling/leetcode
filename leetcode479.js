/*
* auther yeling
* 479. 最大回文数乘积
* 
*/
//暴力方法超时了，需要裁剪 TLE
MOD = 1337;
var largestPalindrome2 = function (n) {
    let i = 0;
    let begin = 1, end = 1;
    while (i < n) {
        end *= 10;
        i++;
    }
    begin = Math.floor(end / 10);
    end = end - 1;

    let find = false;
    let max = 0;
    for (let i = end; i >= begin && find == false; i--) {
        for (let j = i + 1; j <= end; j++) {
            let mul = i * j;
            if (isHuiwen(mul.toString())) {
                find = true;
                max = mul;
                console.log(`${max} ${i} ${j}`);
                break;
            }
        }
    }
    console.log(max);
    return max % MOD;
};

//n == 8的时候处理不了，超范围了
var largestPalindrome3 = function (n) {
    if (n == 1) {
        return 9;
    }
    let i = 0;
    let begin = 1, end = 1;
    while (i < n) {
        end *= 10;
        i++;
    }
    begin = Math.floor(end / 10);
    end = end - 1;
    let max = 0;
    let curr = end;
    let find = false;
    while (curr >= begin) {
        //if(isHuiwen())
        let num = curr;
        if (curr.toString().length >= 1) {
            let numStr = curr.toString();
            for (let i = 0; i < n; i++) {
                numStr += numStr.charAt(n - 1 - i);
            }
            num = Number.parseInt(numStr);
            //num = BigInt(numStr);
            console.log(`${numStr} ${num}`);
        } else if (isHuiwen(curr) == false) {
            curr--;
            continue;
        }

        let resi = Math.floor(Math.sqrt(num));
        while (resi <= end) {
            //console.log(`resi ${resi} ${num}`);
            if (num % resi == 0 && num / resi >= begin && num / resi <= end) {
                console.log(`res = ${num} ${num / resi} ${resi}`)
                return num % MOD;
            }
            resi++;
        }
        curr--;
    }

    console.log(max);
    return max % MOD;
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


var largestPalindrome = function (n) {
    if (n == 1) {
        return 9;
    }
    let i = 0;
    let begin = 1, end = 1;
    while (i < n) {
        end *= 10;
        i++;
    }
    begin = Math.floor(end / 10);
    end = end - 1;
    let max = 0;
    let curr = end;
    while (curr >= begin) {
        let numStr = curr.toString();
        for (let i = 0; i < n; i++) {
            numStr += numStr.charAt(n - 1 - i);
        }
        let num = BigInt(numStr);
        //console.log(`${numStr} ${num}`);
        let resi = BigInt(end);
        while (resi * resi > num) {
            //console.log(`resi ${resi} ${num}`);
            if (num % resi == 0 && num / resi >= begin && num / resi <= end) {
                console.log(`res = ${num} ${num / resi} ${resi}`)
                return num % BigInt(MOD);
            }
            resi--;
        }
        curr--;
    }
    console.log(max);
    return max % MOD;
};




n = 8; //8  475
// console.log(div('9999999999999999',99999999));
// console.log(906609/1337);
// console.log(678*1337 + 140);
// console.log(largestPalindrome(n));
// console.log(largestPalindrome3(n));
console.log(largestPalindrome(n));
