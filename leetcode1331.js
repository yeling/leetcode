/*
* auther yeling
* 1331. 数组序号转换
* 
*/
/**
 * @param {number[]} arr
 * @return {number[]}
 */
var arrayRankTransform = function(arr) {
    let cache = new Map();
    arr.forEach((value,index) => {
        let nums = cache.get(value);
        if(nums == null) {
            nums = [];
        }
        nums.push(index);
        cache.set(value,nums);
    })
    let allKeys = new Array();
    cache.forEach((v,k) => {
        allKeys.push(k);
    })
    allKeys.sort((a,b) => a - b);
    allKeys.forEach((v,i) => {
        cache.set(v,i+1);
    })
    let res = new Array();
    arr.forEach((v,i) => {
        res.push(cache.get(v));
    })
    return res;
};

arr = [40,40,10,20,30]
console.log(arrayRankTransform(arr));
