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

function begin(n, h, b) {
    let sum = 0; 
    let max = Number.MIN_SAFE_INTEGER;
    for(let i = 0; i < n; i++) {
        sum += h[i] + b[i];
        max = Math.max(max, b[i]);
    }
    sum -= max;
    print(sum);

}
function main() {
    var caseNum = parseInt(readline(), 10);
    for (var i = 0; i < caseNum; i++) {
        var n = parseInt(readline(), 10);
        var h = readline()
            .trim()
            .split(' ')
            .map((y) => parseInt(y, 10));
        var b = readline()
            .trim()
            .split(' ')
            .map((y) => parseInt(y, 10));
        begin(n, h, b);
    }
}