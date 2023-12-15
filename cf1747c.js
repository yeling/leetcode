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

function begin(n, nums) {
    let min = Number.MAX_SAFE_INTEGER;
    let minIndex = 0;
    for(let i = 0; i < nums.length; i++) {
        if(min > nums[i]) {
            min = nums[i];
            minIndex = i;
        }
    }
    if(minIndex > 0) {
        print("Alice");
    } else {
        print("Bob");
    }
}

function main() {
    var caseNum = parseInt(readline(), 10);
    for (var i = 0; i < caseNum; i++) {
        var n = parseInt(readline(), 10);
        var x = readline()
            .trim()
            .split(' ')
            .map((y) => parseInt(y, 10));
        begin(n, x);
    }
}