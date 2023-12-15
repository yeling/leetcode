/*
* auther yeling
* 
* 
*/


/**
 * @param {number[][]} items1
 * @param {number[][]} items2
 * @return {number[][]}
 */
var mergeSimilarItems = function(items1, items2) {
    let cache = new Map();
    for(let i = 0; i < items1.length; i++) {
        cache.set(items1[i][0],items1[i][1]);
    }

    for(let i = 0; i < items2.length; i++) {
        if(cache.has(items2[i][0])) {
            cache.set(items2[i][0],cache.get(items2[i][0]) + items2[i][1]);
        } else {
            cache.set(items2[i][0],items2[i][1]);
        }
    }

    let res = [];
    cache.forEach((value,key) => {
        res.push([key,value]);
    });
    res.sort((a,b) => a[0] - b[0]);
    return res;

};


items1 = [[1,1],[3,2],[2,3]], items2 = [[2,1],[3,2],[1,3]]
items1 = [[1,3],[2,2]],items2 = [[7,1],[2,2],[1,4]]
console.log(mergeSimilarItems(items1,items2).join(' '));
