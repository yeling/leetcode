/*
* auther yeling
* 363. 矩形区域不超过 K 的最大数值和
* 
*/

/**
 * @param {number[][]} matrix
 * @param {number} k
 * @return {number}
 */

// 24 / 39 个通过测试用例 没有内存
var maxSumSubmatrix2 = function (matrix, k) {
    //二维矩阵前缀和
    let m = matrix.length;
    let n = matrix[0].length;
    let preSum = [];
    for (let i = 0; i < m; i++) {
        preSum[i] = new Array(n);
        preSum[i].fill(0);
    }

    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            let sum = 0;
            for (let a = 0; a <= i; a++) {
                for (let b = 0; b <= j; b++) {
                    sum += matrix[a][b];
                }
            }
            preSum[i][j] = sum;
        }
    }
    let allSum = new Set();
    //计算所有 i,j -> a,b的和
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            for (let a = i; a < m; a++) {
                for (let b = j; b < n; b++) {
                    //let sum = preSum[a][b] - preSum[a][j - 1] - preSum[i - 1][b] + preSum[i - 1][j - 1];
                    let sum = preSum[a][b];
                    if (j > 0) {
                        sum -= preSum[a][j - 1];
                    }
                    if (i > 0) {
                        sum -= preSum[i - 1][b];
                    }
                    if (i > 0 && j > 0) {
                        sum += preSum[i - 1][j - 1];
                    }
                    if (sum < k) {
                        allSum.add(sum);
                    } else if (sum == k) {
                        return k;
                    }
                }
            }
        }
    }
    //console.log('preSum \n' + preSum.join('\n'));
    //console.log(`${allSum}`);
    let sumArray = [];
    allSum.forEach((value) => {
        sumArray.push(value);
    })
    sumArray.sort((a, b) => a - b);
    //console.log(`${allSum}`);
    let ret = sumArray[0];
    for (let i = 0; i < sumArray.length; i++) {
        if (sumArray[i] <= k) {
            ret = sumArray[i];
        } else {
            break;
        }
    }
    return ret;
};

var maxSumSubmatrix3 = function (matrix, k) {
    //二维矩阵前缀和
    let m = matrix.length;
    let n = matrix[0].length;
    let preSum = [];
    for (let i = 0; i <= m; i++) {
        preSum[i] = new Array(n + 1);
        preSum[i].fill(0);
    }

    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            let sum = 0;
            for (let a = 0; a <= i; a++) {
                for (let b = 0; b <= j; b++) {
                    sum += matrix[a][b];
                }
            }
            preSum[i + 1][j + 1] = sum;
        }
    }
    let allSum = new Set();
    //计算所有 i,j -> a,b的和
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            for (let a = i; a < m; a++) {
                for (let b = j; b < n; b++) {
                    let sum = preSum[a + 1][b + 1] - preSum[a + 1][j] - preSum[i][b + 1] + preSum[i][j];
                    if (sum < k) {
                        allSum.add(sum);
                    } else if (sum == k) {
                        return k;
                    }
                }
            }
        }
    }
    //console.log('preSum \n' + preSum.join('\n'));
    //console.log(`${allSum}`);
    let sumArray = [];
    allSum.forEach((value) => {
        sumArray.push(value);
    })
    sumArray.sort((a, b) => b - a);
    //console.log(`${sumArray}`);
    let ret = sumArray[0];
    for (let i = 0; i < sumArray.length; i++) {
        if (sumArray[i] < k) {
            ret = sumArray[i];
            break;
        }
    }
    return ret;
};

var maxSumSubmatrix = function (matrix, k) {
    //二维矩阵前缀和
    let m = matrix.length;
    let n = matrix[0].length;
    let preSum = [];
    for (let i = 0; i <= m; i++) {
        preSum[i] = new Array(n + 1);
        preSum[i].fill(0);
    }

    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            let sum = 0;
            for (let a = 0; a <= i; a++) {
                for (let b = 0; b <= j; b++) {
                    sum += matrix[a][b];
                }
            }
            preSum[i + 1][j + 1] = sum;
        }
    }
    //计算所有 i,j -> a,b的和
    let res = Number.MAX_VALUE;
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            for (let a = i; a < m; a++) {
                for (let b = j; b < n; b++) {
                    let sum = preSum[a + 1][b + 1] - preSum[a + 1][j] - preSum[i][b + 1] + preSum[i][j];
                    if (sum < k) {
                        res = Math.min(res,k - sum);
                    } else if (sum == k) {
                        return k;
                    }
                }
            }
        }
    }
    //console.log(`res ${k - res} ret ${ret}`);
    return k - res;
};

matrix = [[1, 0, 1], [0, -2, 3], [1, 2, 4]], k = 100
console.log(matrix.join(' '));
console.log(maxSumSubmatrix(matrix, k));