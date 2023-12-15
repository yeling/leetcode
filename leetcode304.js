/*
304. 二维区域和检索 - 矩阵不可变
dp数组只保留前缀
*/
/**
 * @param {number[][]} matrix
 */
 var NumMatrix = function(matrix) {
    this.matrix = matrix;
    this.dp = new Array();
    for(let i = 0; i < matrix.length; i++) {
        this.dp[i] = new Array();
        let sum = 0;
        this.dp[i][0] = 0;
        for(let j = 0; j < matrix[0].length; j++) {
            sum += matrix[i][j];
            this.dp[i][j + 1] = sum;
            
        }
    }
    console.log(this.dp[0]);
};

/** 
 * @param {number} row1 
 * @param {number} col1 
 * @param {number} row2 
 * @param {number} col2
 * @return {number}
 */
NumMatrix.prototype.sumRegion = function(row1, col1, row2, col2) {
    let sum = 0;
    for(let i = row1; i <= row2; i++) {
        for(let j = col1; j <= col2; j++) {
            sum += this.matrix[i][j];
        }
    }
    return sum;
};

NumMatrix.prototype.sumRegion2 = function(row1, col1, row2, col2) {
    let sum = 0;
    for(let i = row1; i <= row2; i++) {
        //sum += this.dp[i][col1][col2];
        sum += this.dp[i][col2 + 1] - this.dp[i][col1];
    }
    return sum;
};

/**
 * Your NumMatrix object will be instantiated and called as such:
 * var obj = new NumMatrix(matrix)
 * var param_1 = obj.sumRegion(row1,col1,row2,col2)
 */

var matrix = [[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]];

var temp = new NumMatrix(matrix);
console.log(`sumRegion ${temp.sumRegion(2, 1, 4, 3)}`);
console.log(`sumRegion2 ${temp.sumRegion2(2, 1, 4, 3)}`);

