/*
* auther yeling
* 
* 
*/
// 'use strict';

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

function begin(n, curr, lights) {
    // print(n, curr, lights);
    // 每个curr后面最远的一个g
    let ret = 0;
    if(curr == 'g') {
        print(ret);
        return;
    }
    let max = 0;
    let last = null;
    for(let i = 0; i < 2 * n; i++) {
        if(i < n) {
            if(last == null && lights.charAt(i%n) == curr) {
                last = i;
            }
        } else if(last == null){
            break;
        }
        if(last != null && lights.charAt(i%n) == 'g') {
            max = Math.max(max, i - last);
            last = null;
        }
    }
    print(max);
}

function main() {
    var caseNum = parseInt(readline(), 10);
    for (var i = 0; i < caseNum; i++) {
        var n = readline()
            .trim()
            .split(' ')
        var str = readline()
            .trim()
        begin(Number(n[0]), n[1],str);
    }
}