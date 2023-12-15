/*
* auther yeling
* 1184. 公交站间的距离
* 
*/

/**
 * @param {number[]} distance
 * @param {number} start
 * @param {number} destination
 * @return {number}
 */
var distanceBetweenBusStops = function (distance, start, destination) {

    let s = Math.min(start,destination);
    let d = Math.max(start,destination);

    let n = distance.length;
    let preSum = new Array(n + 1).fill(0);

    distance.forEach((value, index) => {
        preSum[index + 1] = preSum[index] + value;
    })
    console.log(preSum);
    let ret = preSum[d] - preSum[s];
    ret = Math.min(ret, preSum[s] + preSum[n] - preSum[d]);
    return ret;
};


distance = [1, 2, 3, 4], start = 0, destination = 3
distance = [7,10,1,12,11,14,5,0] ,start = 7 ,destination  = 2

console.log(distanceBetweenBusStops(distance, start, destination));
