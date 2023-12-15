/*
* auther yeling
* 
* 
*/

/**
 * @param {string[]} garbage
 * @param {number[]} travel
 * @return {number}
 */
var garbageCollection = function(garbage, travel) {
    let n = garbage.length;

    let preSum = new Array(n + 1).fill(0);
    for(let i = 0; i < n - 1; i++) {
        preSum[i + 1] = preSum[i] + travel[i];
    }
    //console.log(preSum);

    //存储位置和总时间
    let res = new Array(3).fill(0).map(() => [0,0]);
    let path = 0;
    //MPG
    for(let i = 0; i < n; i++) {
        let curr = garbage[i];
        let currLen = new Array(3).fill(0);
        for(let j = 0; j < curr.length; j++) {
            if(curr.charAt(j) == 'M') {
                currLen[0]++;
            } else if(curr.charAt(j) == 'P') {
                currLen[1]++;
            } else if(curr.charAt(j) == 'G') {
                currLen[2]++;
            }
        }
        for(let j = 0; j < res.length; j++) {
            if(currLen[j] != 0) {
                res[j][1] += preSum[i] - preSum[res[j][0]] + currLen[j];
                res[j][0] = i;
            }
        }
        //console.log(res.join(' '));
    }

    let sum = 0;
    for(let j = 0; j < res.length; j++) {
        sum += res[j][1];
        
    }
    return sum;
};

garbage = ["G","P","GP","GG"], travel = [2,4,3];
garbage = ["MMM","PGM","GP"], travel = [3,10];
console.log(garbage + ' ' + travel);
console.log(garbageCollection(garbage,travel));
