/*
* auther yeling
*522. 最长特殊序列 II
*题目可以转化为最长公共子序列
*/
let count = 0;
var findLUSlength = function(strs) {
    let maxSum = -1;
    let subCache = new Map();
    for(let i = 0; i < strs.length; i++) {
        let temp = strs[i];
        // calcSub(temp,0,[],subCache);
        let preStr = [];
        for(let i = 0; i < temp.length; i++) {
            preStr.push(temp.charAt(i));
        }
        calcSub2(temp,temp.length - 1,preStr,subCache);
    }
    subCache.forEach((value,key) => {
        //console.log(`${key} ${value}`)
        if(value == true) {
            maxSum = Math.max(maxSum,key.length);
        }
    });
    return maxSum;
};

var calcSub2 = function(str, index, preStr, subCache) {
    count++;
    console.log(`calcSub ${index} ${preStr} ${subCache}`)
    let subStr = '';
    // for(let i = 0; i < preStr.length; i++) {
    //     subStr += preStr[i];
    // }
    // if(subCache.get(subStr) != null) {
    //     subCache.set(subStr, false);
    //     return 
    // }
    if(index == -1) {
        let subStr = '';
        for(let i = 0; i < preStr.length; i++) {
            subStr += preStr[i];
        }
        if(subCache.get(subStr) == null) {
            subCache.set(subStr, true);
        } else {
            subCache.set(subStr, false);
        }
        //console.log(`calcSub1 ${index} ${preStr} ${subCache}`)
        //console.log(subCache)
        return 
    }
    //要i位置
    calcSub2(str,index - 1,preStr ,subCache);
    //不要i位置
    preStr.splice(index,1);
    calcSub2(str,index - 1, preStr ,subCache);
    preStr.splice(index,0,str.charAt(index));
}

var calcSub = function(str, index, preStr, subCache) {
    count++;
    if(index == str.length) {
        let subStr = '';
        for(let i = 0; i < preStr.length; i++) {
            subStr += preStr[i];
        }
        if(subCache.get(subStr) == null) {
            subCache.set(subStr, true);
        } else {
            subCache.set(subStr, false);
        }
        // console.log(`calcSub ${index} ${preStr} ${subCache}`)
        // console.log(subCache)
        return 
    }
    
    calcSub(str,index + 1,preStr ,subCache);
    preStr.push(str.charAt(index));
    calcSub(str,index + 1,preStr ,subCache);
    preStr.pop();
    
}

// let strs = ["aba","cdc","eae"];
// let strs = ["aba"];
strs = ["aaa","aaa","a"];
console.log(findLUSlength(strs));
console.log(`count ${count}`)