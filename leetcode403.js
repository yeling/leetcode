/*
* auther yeling
* 
* 
*/
/**
 * @param {number[]} stones
 * @return {boolean}
 */
//49 / 52
var canCross = function (stones) {
    let stoneMap = new Map();
    stones.forEach((value) => {
        stoneMap.set(value, new Set());
    })
    let kSet = stoneMap.get(0);
    kSet.add(1);
    for (let i = 0; i < stones.length; i++) {
        kSet = stoneMap.get(stones[i]);
        if (kSet.size == 0) {
            continue;
        }
        kSet.forEach(value => {
            let dst = stones[i] + value;
            if (stoneMap.has(dst)) {
                let dstSet = stoneMap.get(dst);
                dstSet.add(value);
                dstSet.add(value + 1);
                if (value > 1) {
                    dstSet.add(value - 1);
                }
            }
        })
        //console.log(stoneMap);
    }

    return stoneMap.get(stones.at(stones.length - 1)).size > 0 ? true : false;

};


stones = [0, 1, 3, 5, 6, 8, 12, 17];
stones = [0, 1, 2, 3, 4, 8, 9, 11];
stones = [0, 1, 3, 6, 10, 15, 16, 21];
console.log(`${canCross(stones)}`);
