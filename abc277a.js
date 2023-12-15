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

function begin(n, x, nums) {
    for(let i = 0; i < n; i++) {
        if(nums[i] == x) {
            print(i + 1)
        }
    }

}

function main() {
    var n = readline()
        .trim()
        .split(' ')
        .map((y) => parseInt(y, 10));
    var x = readline()
        .trim()
        .split(' ')
        .map((y) => parseInt(y, 10));
    begin(n[0],n[1], x);

}