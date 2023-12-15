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

function begin(n, m, grid) {
    //print(`${n} ${m} ${grid.join(' ')}`);
    let rows = new Array(n).fill(0);
    let cols = new Array(n).fill(0);
    for(let i = 0; i < grid.length; i++) {
        rows[grid[i][0] - 1]++;
        cols[grid[i][1] - 1]++;
    }
    //zero one two
    let rowRes = [0,0,0];
    let colRes = [0,0,0];
    
    for(let i = 0; i < n; i++) {
        if(rows[i] <= 2) {
            rowRes[rows[i]]++;
        } else {
            print("NO");
            return;
        }
        if(cols[i] <= 2) {
            colRes[cols[i]]++;
        } else {
            print("NO");
            return;
        }
    }
    if(colRes[2] + rowRes[2] > 1) {
        print("NO");
        return;
    }
    if(colRes[2] == 1 && colRes[0] == 0) {
        print("NO");
        return;
    }
    if(rowRes[2] == 1 && rowRes[0] == 0) {
        print("NO");
        return;
    }
    if(rowRes[1] == n || colRes[1] == n) {
        print("NO");
        return;
    }
    print("YES");
}

function main() {
    var caseNum = parseInt(readline(), 10);
    for (var i = 0; i < caseNum; i++) {
        var n = readline().trim()
            .split(' ')
            .map((y) => parseInt(y, 10));
        let m = n[1];
        let grid = [];
        for(let i = 0; i < m; i++) {
            var x = readline()
            .trim()
            .split(' ')
            .map((y) => parseInt(y, 10));
            grid.push(x);
        }
        begin(n[0], m, grid);
    }
}