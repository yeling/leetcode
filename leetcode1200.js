/*
* auther yeling
* 1200. 最小绝对差
* 排序，再排序
*/

var minimumAbsDifference = function (arr) {
    let res = [];
    console.log(arr);
    arr.sort((a, b) => a - b);
    let diffArray = [];
    for (let i = 0; i < arr.length - 1; i++) {
        diffArray.push({ a: arr[i], b: arr[i + 1], val: arr[i + 1] - arr[i] })
    }
    diffArray.sort((a, b) => a.val - b.val);
    
    res.push([diffArray[0].a, diffArray[0].b]);
    for (let i = 1; i < diffArray.length; i++) {
        if (diffArray[i].val == diffArray[0].val) {
            res.push([diffArray[i].a, diffArray[i].b]);
        } else {
            break;
        }
    }
    console.log(arr);
    return res;
};

let arr = [3, 8, -10, 23, 19, -4, -14, 27];
let res = minimumAbsDifference(arr)
console.log(res.join(' '));
