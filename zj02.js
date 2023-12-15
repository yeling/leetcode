/*
* auther yeling
* 滑动数组，前缀和，连续的K个中，白子最少的情况
* zj-future02. 黑白棋游戏
*/

/**
 * @param {number[]} chess
 * @return {number}
 */
var minSwaps = function(chess) {
        //滑动窗口，前缀和，连续的K个中，白子最少的情况
        let count = 0;
        let pre = new Array(chess.length + 1);
        pre.fill(0);
        chess.forEach((item,index) => {
            count += item;
            if(index == 0) {
                pre[index + 1] = item;
            } else {
                pre[index + 1] = pre[index] + item;
            }
        })
        console.log(pre);
        let min = chess.length;
        for(let i = count - 1; i < chess.length; i++) {
            min = Math.min(min,count - (pre[i + 1] - pre[i - count + 1]));
        }
        return min;

};

chess = [1,0,1,0,1,0];
chess = [1,1,0,1,0,1,0,0,1,0,1];
chess = [1,0,1,0,1,0,0,1,1,0,1];
console.log(chess);
console.log(`${minSwaps(chess)}`);
