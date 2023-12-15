/*
* auther yeling
* 769. 最多能完成排序的块
* 
*/

/**
 * @param {number[]} arr
 * @return {number}
 */
var maxChunksToSorted = function(arr) {
    let sorted = arr.slice(0);
    sorted.sort((a,b) => a - b);
    let cache = new Set();
    let sum = 0;
    //console.log(arr);
    //console.log(sorted);
    for(let i = 0; i < arr.length; i++) {        
        if(cache.has(arr[i])) {
            cache.delete(arr[i]);
        } else {
            cache.add(arr[i]);
        }

        if(cache.has(sorted[i])) {
            cache.delete(sorted[i]);
        } else {
            cache.add(sorted[i]);
        }
        if(cache.size == 0) {
            sum++;
        }
    }
    return sum;
};

arr = [1,0,2,3,4];
console.log(maxChunksToSorted(arr));
