/*
* auther yeling
* 
* 
*/

/**
 * @param {number[][]} mat
 * @param {number} cols
 * @return {number}
 */
var maximumRows = function(mat, cols) {
    let m = mat.length;
    let n = mat[0].length;
    let used = new Array(n).fill(false);
    let maxLine = 0;
    let calUsed = true;
    let dfs = (mat, m , n, used, preLen) => {
        if(preLen == cols) {
            let count = 0;
            for(let i = 0; i < m; i++) {
                let find = true;
                for(let j = 0; j < n; j++) {
                    if(calUsed && used[j] == false && mat[i][j] == 1) {
                        find = false;
                        break;
                    } else if(calUsed == false && used[j] == true && mat[i][j] == 1){
                        find = false;
                        break;
                    }
                }
                if(find) {
                    count++;
                }
            }
            maxLine = Math.max(maxLine, count);
            return;
        }

        for(let i = 0; i < n; i++) {
            if(used[i] == false) {
                used[i] = true;
                dfs(mat, m, n, used, preLen + 1);
                used[i] = false;
            }
        }
    }
    if(cols < n / 2) {
        calUsed = true;
    } else {
        calUsed = false;
        cols = n - cols;
    }
    
    dfs(mat, m, n, used, 0);
    return maxLine;
};

//82 / 103 个通过测试用例
var maximumRows2 = function(mat, cols) {

}

mat = [[0,0,0],[1,0,1],[0,1,1],[0,0,1]], cols = 2
mat = [[1],[0]], cols = 1
mat = [[1,0,0,1,0,0,1,1,1,1,0,1],[1,1,1,1,0,0,1,1,1,0,0,1],[0,1,1,0,0,0,1,1,0,1,1,1],[0,0,0,1,0,0,1,0,1,0,1,1],[0,1,1,1,0,0,0,1,1,1,1,0],[1,1,0,1,0,1,1,1,1,0,1,1],[1,1,0,0,0,1,0,0,0,0,1,1],[1,1,1,0,1,0,0,1,1,0,0,1],[1,0,1,1,1,0,1,0,0,0,1,0],[0,0,0,1,1,0,1,1,1,1,1,1],[1,1,0,1,0,0,1,1,1,0,1,1],[0,0,1,0,0,1,1,1,1,0,1,1]]
cols = 5

// mat = [[1,0,0,1,0,0,1,1,1,1,0,1],[1,1,1,1,0,0,1,1,1,0,0,1],[0,1,1,0,0,0,1,1,0,1,1,1],[0,0,0,1,0,0,1,0,1,0,1,1],[0,1,1,1,0,0,0,1,1,1,1,0],[1,1,0,1,0,1,1,1,1,0,1,1],[1,1,0,0,0,1,0,0,0,0,1,1]]
// cols = 8
console.time('maximumRows');
console.log(maximumRows(mat,cols));
console.timeEnd('maximumRows');
