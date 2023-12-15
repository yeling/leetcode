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
    if(n%2 == 0) {
        print(n/2);
        let dis = (n/2) * 3 + 2;
        for(let i = 1; i <= n/2; i++) {
            print(`${(i - 1) * 3 + 1} ${(i - 1) * 3 + 1 + dis}`);
        }
    } else {
        print(Math.ceil(n/2));
        let dis = (n-1)/2 * 3 + 2;
        for(let i = 1; i <= Math.floor(n/2); i++) {
            print(`${(i - 1) * 3 + 1} ${(i - 1) * 3 + 1 + dis}`);
        }
        print(`${2} ${n*3}`);
    }

    
}

function main() {
    var caseNum = parseInt(readline(), 10);
    for (var i = 0; i < caseNum; i++) {
        var n = parseInt(readline(), 10);
        begin(n);
    }
}