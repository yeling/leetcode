/*
* auther yeling
* 
* 6187. 完成所有交易的初始最少钱数
*/
/**
 * @param {number[][]} transactions
 * @return {number}
 */
var minimumMoney = function(transactions) {
    let totalLost = 0;
    let maxCost = 0;
    let maxCb = 0;
    for(let i = 0; i < transactions.length; i++) {
        let t = transactions[i];
        if(t[0] > t[1]) {
            //最小的累积损失
            totalLost += t[0] - t[1];
            //以负数为最后一项时需要的totalLost - (c - b) + c = totalLost + b 
            //需要知道cb的最大值
            maxCb = Math.max(maxCb, t[1]);
        } else {
            //做完负数，做最大的正数，需要知道最大的正数值
            maxCost = Math.max(maxCost, t[0]);
        }
    }
    return  totalLost + Math.max(maxCb, maxCost);
};

transactions = [[2,1],[5,0],[4,2],[14,2]];
console.log(minimumMoney(transactions));





