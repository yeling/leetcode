/*
* auther yeling
* 1217. 玩筹码
* 所有的奇数在一起之后，cost为0，所有的偶数在一起后cost为0，
* 最终的cost为，两个里面的最小的值
*/

/**
 * @param {number[]} position
 * @return {number}
 */
var minCostToMoveChips = function(position) {
    let odd = 0;
    position.forEach((item) => {
        if(item&1 == 1) {
            odd++;
        }
    })
    return Math.min(odd,position.length - odd);

};

let position = [1,2,3];
position = [2,2,3,2,3];
console.log(minCostToMoveChips(position));