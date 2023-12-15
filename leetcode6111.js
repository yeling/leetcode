/*
* auther yeling
* 6111. 螺旋矩阵 IV
* 
*/

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {number} m
 * @param {number} n
 * @param {ListNode} head
 * @return {number[][]}
 */
function ListNode(val, next) {
    this.val = (val===undefined ? 0 : val)
    this.next = (next===undefined ? null : next)
}
var spiralMatrix = function(m, n, head) {
    let result = new Array(m);
    for(let i = 0 ; i < m; i++) {
        result[i] = new Array(n);
        result[i].fill(-1);
    }
    //0，1，2，3
    let direction = 0;
    let i = 0, j = 0;
    while(head != null) {
        result[i][j] = head.val;
        head = head.next;
        switch(direction) {
            case 0:
                if(j == n-1 || result[i][j+1] != -1) {
                    if(i + 1 <= m -1 && result[i+1][j] != -1){
                        direction = 1;
                        i++;
                    } else {
                        return result;
                    }
                } else {
                    j++;
                }
                break;
            case 1:
                if(i == m-1 || result[i + 1][j] != -1) {
                    if( j-1 >= 0 && result[i][j-1] != -1){
                        direction = 2;
                        j--;
                    } else {
                        return result;
                    }
                } else {
                    i++;
                }
                break;
            case 2:
                if(j == 0 || result[i][j - 1] != -1) {
                    if( i-1 >= 0 && result[i - 1][j] != -1){
                        direction = 3;
                        i--;
                    } else {
                        return result;
                    }
                } else {
                    j--;
                }
                break;
                
            case 3:
                if(i == 0 || result[i-1][j] != -1) {
                    if( j + 1 <= n - 1 && result[i][j + 1] != -1){
                        direction = 0;
                        j++;
                    } else {
                        return result;
                    }
                } else {
                    i--;
                }
                break;
        }
    }
    return result;
};

let res = spiralMatrix(2,3);
console.log(res.join(' '));
