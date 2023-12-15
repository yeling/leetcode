/*
* auther yeling
* 779. 第K个语法符号
* 
*/

/**
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
var kthGrammar = function(n, k) {
    let index = n;
    let path = new Array();    
    while(index > 0) {        
        path.push(k);
        if(k%2 == 0) {
            k = k/2;
        } else {
            k = Math.floor(k/2) + 1            
        }        
        index--;
    }
    let curr = 0;
    for(let i = n - 1; i >= 0; i--) {
        if(i == n - 1) {
            curr = 0;
        } else {
            if(path[i] == 2 * path[i+1]) {
                if(curr == 0) {
                    curr = 1;
                } else {
                    curr = 0;
                }
            } 
        }
    }
    //console.log(path);
    return curr;
};

n = 2, k = 1
n = 4, k = 8
console.log(kthGrammar(n,k));