/*
* auther yeling
* 
* 
*/
/**
 * @param {string[]} creators
 * @param {string[]} ids
 * @param {number[]} views
 * @return {string[][]}
 */
var mostPopularCreator = function(creators, ids, views) {
    //name ,[count, views, ids]
    let cache = new Map();
    let n = creators.length;
    for(let i = 0; i < n; i++) {
        let item = cache.get(creators[i]);
        if(item == null) {
            item = [0,-1,null];
            cache.set(creators[i], item);
        }
        item[0] += views[i];
        if(views[i] > item[1]) {
            item[1] = views[i];
            item[2] = ids[i];
        } else if(views[i] == item[1]) {
            if(ids[i].localeCompare(item[2]) < 0) {
                item[1] = views[i];
                item[2] = ids[i];
            }
        }
    }
    //console.log(cache);
    let arr = Array.from(cache.keys());
    let max = -1;
    for(let i = 0; i < arr.length; i++) {
        let temp = cache.get(arr[i]);
        if(temp[0] > max) {
            max = temp[0];
        }
    }

    let res = [];
    for(let i = 0; i < arr.length; i++) {
        let temp = cache.get(arr[i]);
        if(temp[0] == max) {
            res.push([arr[i], temp[2]])
        }
    }
    return res;
};

creators = ["alice","alice","alice"], ids = ["a","b","c"], views = [1,2,2]
creators = ["alice","bob","alice","chris"], ids = ["one","two","three","four"], views = [5,10,5,4]
creators = ["d"]
ids = ["rdf"]
views = [0]
console.log(mostPopularCreator(creators, ids, views).join(' '));

