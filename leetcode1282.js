/*
* auther yeling
* 
* 1282. 用户分组
*/

/**
 * @param {number[]} groupSizes
 * @return {number[][]}
 */
var groupThePeople = function(groupSizes) {
    let cache = new Map();
    for(let i = 0; i < groupSizes.length; i++) {
        let indexs = cache.get(groupSizes[i]);
        if(indexs == null) {
            indexs = [];
        }
        indexs.push(i);
        cache.set(groupSizes[i],indexs);
    }
    res = [];
    cache.forEach((value,key) => {
        let i = 0;
        let temp = [];
        while(i < value.length) {
            temp.push(value[i]);
            i++;
            if(i%key == 0) {
                if(temp.length > 0) {
                    res.push(temp);
                }
                temp = new Array();
            }
        }
    });
    return res;
};

groupSizes = [3,3,3,3,3,1,3]
console.log(groupThePeople(groupSizes).join(' '))
