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

function begin(n) {
    if(n == 1) {
        print('1');
        return;
    }
    let res = new Array(n).fill(0);
    for(let i = 1; i < n; i++) {
        res[i] = i + 2;
    }
    res[0] = 1;
    res[n - 1] = 2;
    print(res.join(' '));
}

function main() {
    var caseNum = parseInt(readline(), 10);
    for (var i = 0; i < caseNum; i++) {
        var n = parseInt(readline(), 10);
        begin(n);
    }
}