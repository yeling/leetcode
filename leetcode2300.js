/*
* auther yeling
* 
* 
*/

/**
 * @param {number[]} spells
 * @param {number[]} potions
 * @param {number} success
 * @return {number[]}
 */
var successfulPairs = function(spells, potions, success) {
    let n = spells.length;
    let m = potions.length;
    let res = new Array(n).fill(0);
    potions.sort((a,b) => a - b);
    for(let i = 0; i < n; i++) {
        let dst = success/spells[i];
        let index = -1;
        for(let j = 0; j < m; j++) {
            if(potions[j] >= dst) {
                index = j;
                break;
            }
        }
        if(index == -1) {
            res[i] = 0;
        } else {
            res[i] = m - index;
        }
    }
    return res;
};

spells = [5,1,3], potions = [1,2,3,4,5], success = 7
console.log(successfulPairs(spells,potions,success));

