/*
* auther yeling
* 975. 奇偶跳
* 
*/

/**
 * @param {number[]} arr
 * @return {number}
 */
var oddEvenJumps2 = function(arr) {
    let n = arr.length;
    let cache = new Array(n).fill(0).map((value,index) => {
        return [arr[index], index];
    })
    cache.sort((a,b) => {
        if(a[0] == b[0]) {
            return a[1] - b[1];
        } else {
            return a[0] - b[0];
        }
    });

    console.log(cache.join(' '));
    let sortPos = new Array(n).fill(0);
    cache.forEach((value,index) => {
        sortPos[value[1]] = index;
    })
    //console.log(sortPos.join(' '));
    //0偶数跳，1奇数跳
    let possible = new Array(n).fill(0).map(() => new Array(2).fill(-1));
    possible[n-1] = [1,1];
    for(let i = 0 ; i < n; i++) {
        //
        let step = 1;
        let curr = cache[sortPos[i]];
        if(possible[curr[1]][0] != -1) {
            continue;
        }
        let path = new Array();
        path.push([...curr, 0]);
        //pathHash.add(curr);
        while(true) {
            let next = null;
            if(step%2 == 1) {
                //奇数找排序的下一个
                for(let j = sortPos[curr[1]] + 1; j < cache.length; j++) {
                    if(cache[j][1] > curr[1]) {
                        next = cache[j];
                        break;
                    }
                }
                
            } else {
                //偶数找排序的前一个，等于的话要找附近的几个
                let begin = sortPos[curr[1]];
                while(begin < n && cache[begin][0] == curr[0]) {
                    begin++;
                }
                let dst = null
                for(let j = begin - 1; j >= 0; j--) {
                    if(dst != null){
                        if(dst[0] == cache[j][0] && cache[j][1] > curr[1] && j != sortPos[curr[1]]) {
                            dst = cache[j];
                        } else {
                            break;
                        }
                    }
                    if(cache[j][1] > curr[1] && j != sortPos[curr[1]]) {
                        dst = cache[j];
                    }
                }
                next = dst;
            }
            if(next == null) {
                break;
            }
            //到底了
            if(possible[next[1]][step%2] == 1) {
                for(let j = 0; j < path.length; j++) {
                    possible[path[j][1]][path[j][2]] = 1;
                }
                break;
            }          
            path.push([...next, step]);
            curr = next;
            step++;
        }
        console.log(`i=${i} ${possible.join(' ')}`);
    }

    let sum = 0;
    for(let i = 0; i < n; i++) {
        if(possible[i][0] == 1) {
            sum++;
        }
    }
    return sum;
};
//TLE 
//PASS dp记录之前的结果，偶数跳结果，奇数跳结果分开
//倒序遍历会更快
var oddEvenJumps = function(arr) {
    let n = arr.length;
    let cache = new Array(n).fill(0).map((value,index) => {
        return [arr[index], index];
    })
    cache.sort((a,b) => {
        if(a[0] == b[0]) {
            return a[1] - b[1];
        } else {
            return a[0] - b[0];
        }
    });

    console.log(cache.join(' '));
    let sortPos = new Array(n).fill(0);
    cache.forEach((value,index) => {
        sortPos[value[1]] = index;
    })
    //console.log(sortPos.join(' '));
    //0偶数跳，1奇数跳
    let possible = new Array(n).fill(0).map(() => new Array(2).fill(-1));
    possible[n-1] = [1,1];
    for(let i = n - 1 ; i >= 0; i--) {
        //
        let step = 1;
        let curr = cache[sortPos[i]];
        if(possible[curr[1]][0] != -1) {
            continue;
        }
        let path = new Array();
        path.push([...curr, 0]);
        //pathHash.add(curr);
        while(true) {
            let next = null;
            if(step%2 == 1) {
                //奇数找排序的下一个
                for(let j = sortPos[curr[1]] + 1; j < cache.length; j++) {
                    if(cache[j][1] > curr[1]) {
                        next = cache[j];
                        break;
                    }
                }
                
            } else {
                //偶数找排序的前一个，等于的话要找附近的几个
                let begin = sortPos[curr[1]];
                while(begin < n && cache[begin][0] == curr[0]) {
                    begin++;
                }
                let dst = null
                for(let j = begin - 1; j >= 0; j--) {
                    if(dst != null){
                        if(dst[0] == cache[j][0] && cache[j][1] > curr[1] && j != sortPos[curr[1]]) {
                            dst = cache[j];
                        } else {
                            break;
                        }
                    }
                    if(cache[j][1] > curr[1] && j != sortPos[curr[1]]) {
                        dst = cache[j];
                    }
                }
                next = dst;
            }
            if(next == null) {
                break;
            }
            //到底了
            if(possible[next[1]][step%2] == 1) {
                for(let j = 0; j < path.length; j++) {
                    possible[path[j][1]][path[j][2]] = 1;
                }
                break;
            } else if(possible[next[1]][step%2] == 0) {
                break;
            }     
            path.push([...next, step]);
            curr = next;
            step++;
        }
        //console.log(`i=${i} ${possible.join(' ')}`);
    }

    let sum = 0;
    for(let i = 0; i < n; i++) {
        if(possible[i][0] == 1) {
            sum++;
        }
    }
    return sum;
}
arr = [10,13,12,14,15];
// arr = [2,3,1,1,4];//3
// arr = [5,1,3,4,2];//3
arr = [1,2,3,2,1,4,4,5]; //6
// arr = [1,2,3,2,1];//3
// arr = [81,54,96,60,58];//2
// arr = [1,1,1,1];//
label = 'oddEvenJumps';
console.time(label);
console.log(oddEvenJumps(arr));
console.timeLog(label, 'oddEvenJumps');
// console.log(oddEvenJumps(arr));
console.timeEnd(label);