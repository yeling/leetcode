/*
* auther yeling
* 
* 556. 下一个更大元素 III
* 数学问题
*/

/**
 * @param {number} n
 * @return {number}
 */
//内存会溢出
//19 / 39 个通过测试用例
var nextGreaterElement = function (n) {
    let str = n.toString();
    let charArray = [];
    let used = [];
    for (let i = 0; i < str.length; i++) {
        charArray.push(str.charAt(i));
        used.push(false);
    }
    //console.log(`used ${used} charArray ${charArray}`);
    let result = []
    dfs(charArray, used, [], result);
    //console.log(result.join(' '));
    let resultNum = result.map(value => {
        let num = Number.parseInt(value.join(''))
        return num;
    })
    resultNum.sort((a, b) => {
        return a - b;
    });
    //console.log(`resultNum ${resultNum}`);
    let currPos = resultNum.findIndex((a) => {
        return a > n;
    })
    if (currPos != -1) {
        return resultNum[currPos];
    } else {
        return -1;
    }
};

var dfs = function (charArray, used, curr, result) {
    if (curr.length == charArray.length) {
        result.push(curr.slice());
        return;
    }
    for (let i = 0; i < charArray.length; i++) {
        if (used[i] == false) {
            used[i] = true;
            curr.push(charArray[i]);
            dfs(charArray, used, curr, result)
            curr.pop();
            used[i] = false;
        }
    }

}

//31 / 39 个通过测试用例
let MAX = Math.pow(2,31) - 1;
var nextGreaterElement2 = function (n) {
    let str = n.toString();
    let charArray = [];
    let startIndex = -1;
    let result = [];
    charArray.unshift(Number.parseInt(str.charAt(str.length - 1)));
    for (let i = str.length - 2; i >= 0; i--) {
        if (str[i] < str[i + 1]) {
            startIndex = i;
            charArray.unshift(Number.parseInt(str.charAt(i)));
            break;
        }
        charArray.unshift(Number.parseInt(str.charAt(i)));
    }
    if (startIndex == -1) {
        return -1;
    }
    result = str.substring(0, startIndex);
    charArray.sort((a,b) => {
        return a - b;
    })
    let changeIndex = startIndex;
    for(let i = 0; i < charArray.length; i++) {
        if(charArray[i] > Number.parseInt(str.charAt(startIndex))) {
            changeIndex = i;
            break;
        }
    }
    result = result + charArray[changeIndex];
    charArray.splice(changeIndex,1); 
    //console.log(`resutl ${result}`);
    charArray.forEach((value) => {
        result += value;
    })
    let resultNum = Number.parseInt(result);
    if(resultNum >  MAX ) {
        resultNum = -1;
    }
    return resultNum;
}
let num = 2147483476;
num = 215764;
console.log(num);
//console.log(`${nextGreaterElement(num)}`)
console.log(`${nextGreaterElement2(num)}`)
// console.log(Math.pow(2,31) - 1);