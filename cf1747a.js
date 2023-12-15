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

function begin2(n, nums) {
    // print(n, nums);
    let s1 = 0, s2 = 0;
    for(let i = 0; i < n; i++) {
        if(nums[i] >= 0) {
            s1 += nums[i];
        } else {
            s2 += nums[i];
        }
    }
    let res = Math.abs(Math.abs(s1) -Math.abs(s2));
    print(res);
}

function begin(n, nums) {
    // print(n, nums);
    let sum = 0;
    for(let i = 0; i < n; i++) {
        sum += nums[i]
    }
    let res = Math.abs(sum);
    print(res);   
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