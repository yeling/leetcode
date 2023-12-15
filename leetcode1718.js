/*
* auther yeling
* 1718. 构建字典序最大的可行序列
* 
*/

/**
 * @param {number} n
 * @return {number[]}
 */
var constructDistancedSequence = function(n) {
    let find = false;
    let len = 2 * (n - 1) + 1;
    let res = [];

    let dfs = (index, used, array) => {
        //console.log(`${index} ${used.join(' ')} ${array.join(',')}`)
        for(let i = n; i > 0; i--) {
            if(i == 1) {
                if(used[i] == false) {
                    array[index] = i;
                    used[i] = true;
                    let currFind = false;
                    for(let j = index + 1; j < array.length; j++) {
                        if(array[j] == 0) {
                            dfs(j, used, array);
                            currFind = true;
                            break;
                        }
                    }
                    if(currFind == false) {
                        if(find == false) {
                            find = true;
                            res = array.slice(0);
                        }
                        console.log(`find ${res.join(' ')}`);
                        return;
                    }
                    array[index] = 0;
                    used[i] = false;
                }
            } else {
                if(used[i] == false && array[index + i] == 0) {
                    array[index] = i;
                    array[index + i] = i;
                    used[i] = true;
                    let currFind = false;
                    for(let j = index + 1; j < array.length; j++) {
                        if(array[j] == 0) {
                            dfs(j, used, array);
                            currFind = true;
                            break;
                        }
                    }
                    if(currFind == false) {
                        if(find == false) {
                            find = true;
                            res = array.slice(0);
                        }
                        console.log(`find ${res.join(' ')}`);
                        return;
                    }
                    array[index] = 0;
                    array[index + i] = 0;
                    used[i] = false;
                }
            }
            
        }

    }
    let used = new Array(n + 1).fill(false);
    let array = new Array(len).fill(0);
    dfs(0, used, array);
    return res;
};



let label = 'numWays2';
let n = 20;
n = 6;
// [6,4,2,5,2,4,6,3,5,1,3]
// [5,1,4,6,3,5,4,3,2,6,2]
// dfs需要改成bfs

console.time(label);
console.log(constructDistancedSequence(n));
console.timeLog(label, 'constructDistancedSequence ' );
// console.log(constructDistancedSequence(5));
console.timeEnd(label);