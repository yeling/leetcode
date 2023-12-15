/*
* auther yeling
* 
* 
*/

/**
 * @param {number[]} arr
 * @return {number}
 */
var maxChunksToSorted2 = function(arr) {
    let n = arr.length;
    let sorted = new Array(n).fill(0).map((value,index) => arr[index]);
    sorted.sort((a,b) => a - b);
    //console.log(sorted);
    let i = 0,si = 0; 
    let cache = [];
    let count = 0;
    let target = sorted[0];
    while(i < n) {
        cache.push(arr[i]);
        if(target != arr[i]) {
            i++;
        } else {
            //i找到了，cache开始移动
            cache.sort((a,b) => a - b);
            let find = true;
            for(let j = 0; j < cache.length; j++) {
                if(cache[j] == sorted[j + si]) {
                    continue;
                } else {
                    target = sorted[j + si];
                    find = false;
                    break;
                }
            }
            if(find) {
                cache.length = 0;
                count++;
                si = i + 1;
                if(i < n - 1) {
                    target = sorted[i + 1];
                }  
            }
            i++;
        }
    }
    return count;

};

var maxChunksToSorted = function(arr) {
    let n = arr.length;
    let sorted = new Array(n).fill(0).map((value,index) => arr[index]);
    sorted.sort((a,b) => a - b);
    //console.log(sorted);
    let i = 0,si = 0; 
    let cache = [];
    let count = 0;
    let target = sorted[0];
    while(i < n) {
        cache.push(arr[i]);
        if(target != arr[i]) {
            i++;
        } else {
            //i找到了，cache开始移动
            cache.sort((a,b) => a - b);
            let find = true;
            for(let j = 0; j < cache.length; j++) {
                if(cache[j] == sorted[j + si]) {
                    continue;
                } else {
                    target = sorted[j + si];
                    find = false;
                    break;
                }
            }
            if(find) {
                cache.length = 0;
                count++;
                si = i + 1;
                if(i < n - 1) {
                    target = sorted[i + 1];
                }  
            }
            i++;
        }
    }
    return count;

};

arr = [2,1,3,4,4]
arr = [4,2,3,1,4,5]

console.log(maxChunksToSorted(arr));
