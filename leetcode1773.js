/*
* auther yeling
* 1773. 统计匹配检索规则的物品数量
* 
*/

/**
 * @param {string[][]} items
 * @param {string} ruleKey
 * @param {string} ruleValue
 * @return {number}
 */
var countMatches = function (items, ruleKey, ruleValue) {
    let sum = 0;
    let index = 0;
    switch (ruleKey) {
        case 'type':
            index = 0;
            break;
        case 'color':
            index = 1;
            break;
        case 'name':
            index = 2;
            break;
    }
    for (let i = 0; i < items.length; i++) {
        if(items[i][index] == ruleValue) {
            sum++;
        }
    }
    return sum;
};



