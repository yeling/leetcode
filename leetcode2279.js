/*
* auther yeling
* 2279. 装满石头的背包的最大数量
*/

/**
 * @param {number[]} capacity
 * @param {number[]} rocks
 * @param {number} additionalRocks
 * @return {number}
 */
var maximumBags = function(capacity, rocks, additionalRocks) {
    for(let i = 0; i < capacity.length;i++) {
        rocks[i] = rocks[i] - capacity[i];
    }
    rocks.sort((a,b) => {
        return a - b;
    });
    console.log(rocks);
    let sum = 0;
    for(let i = rocks.length - 1; i >= 0; i--) {
        additionalRocks = additionalRocks + rocks[i];
        if(additionalRocks >= 0) {
            sum++;
        } else {
            break;
        }
    }
    return sum;
};

let capacity = [2,3,4,5],rocks = [1,2,4,4], additionalRocks = 2;
capacity = [91,54,63,99,24,45,78];
rocks = [35,32,45,98,6,1,25];
additionalRocks = 17;
console.log(maximumBags(capacity,rocks,additionalRocks));


