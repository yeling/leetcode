/*
* auther yeling
* 
* 
*/
'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readline() {
    return inputString[currentLine++];
}
function print(str) {
    console.log(str);
}

// const { readline, print, testOutput } = require('@ip-algorithmics/codeforces-io');
// main();
// testOutput();

function begin(m, n, grid) {
    // print(grid);
    let start = [];
    for(let i = 0; i < m; i++) {
        for(let j = 0; j < n; j++) {
            if(grid[i][j] == 2) {
                start = [i,j];
            }
        }
    }
    let dfs = (i, j, start, used, path) => {
        let dir = [[-1, 0], [1,0], [0,1], [0, -1]];
        for(let k = 0; k < dir.length; k++) {
            let next = [i + dir[k][0], j + dir[k][1]];
            if(next[0] >= 0 && next[0] < m && next[1] >= 0 && next[1] < n) {
                if(next[0] == start[0] && next[1] == start[1] && path.length >= 4) {
                    // print(path.join(' '));
                    return true;
                }
                if(used[next[0]][next[1]] == false && grid[next[0]][next[1]] == 0) {
                    used[next[0]][next[1]] = true;
                    path.push(next);
                    let res = dfs(next[0], next[1], start, used, path);
                    path.pop();
                    if(res == true) {
                        // print(path.join(' '));
                        return true;
                    }
                    used[next[0]][next[1]] = false;
                }
            }
        }
        return false;
    }
    let used = new Array(m).fill(0).map(() => new Array(n).fill(false));
    let path = new Array();
    path.push(start);
    let res = dfs(start[0], start[1], start, used, path);
    if(res) {
        print('Yes');
    } else {
        print('No');
    }   
}

function main() {
    var size = readline()
    .trim()
    .split(' ')
    .map((y) => parseInt(y, 10));
    let nums = [];
    let x = null;
    while ((x = readline()) != null) {
        let temp = x.trim()
            .split('')
            .map((y) => {
                if(y == '.') {
                    return 0;
                } else if(y == '#') {
                    return 1;
                } else if(y == 'S') {
                    return 2
                }
            });
        if(temp.length == 0) {
            break;
        }
        nums.push(temp);
    }

    begin(size[0],size[1], nums);
    
}