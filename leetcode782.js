/*
* auther yeling
* 782. 变为棋盘
* 
*/

/**
 * @param {number[][]} board
 * @return {number}
 */
var movesToChessboard = function(board) {
    let n = board.length;
    if(n%2 == 0) {
        //n为偶数，每行列，0,1相等
        for(let i = 0; i < n; i++) {
            let temp = 0;
            let temp2 = 0;
            for(let j = 0; j < n; j++) {
                temp += board[i][j];
                temp2 += board[j][i];
            }
            if(temp != n/2) {
                return -1;
            }
            if(temp2 != n/2) {
                return -1;
            }
        }
    } else {
        //n为偶数

    }
};

board = [[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]]
console.log(movesToChessboard(board));
