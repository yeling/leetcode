/*
* auther yeling
* 
* 
*/

/**
 * @param {number[]} ranks
 * @param {character[]} suits
 * @return {string}
 */
var bestHand = function(ranks, suits) {
    let result = ['Flush','Three of a Kind','Pair','High Card'];
    let ret = 3;
    let tempSuit = suits[0];
    let sameSuit = 0;
    let rankMap = new Map();
    for(let i = 0; i < suits.length; i++) {
        if(suits[i] == tempSuit) {
            sameSuit++;
        }
        if(rankMap.has(ranks[i]) == false) {
            rankMap.set(ranks[i],1);
        } else {
            rankMap.set(ranks[i],rankMap.get(ranks[i]) + 1);
        }
    }
    if(sameSuit == 5) {
        return result[0];
    }
    let maxSame = 0;
    rankMap.forEach((value) => {
        maxSame = Math.max(maxSame,value);
    });
    if(maxSame >= 3) {
        return result[1];
    } else if(maxSame == 2) {
        return result[2];
    } else {
        return result[3];
    }
};

ranks = [4,4,2,4,4], suits = ["d","a","a","b","c"];
console.log(`${bestHand(ranks,suits)}`);

