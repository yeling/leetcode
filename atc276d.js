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

var gcd = function (a, b) {
    if (b == 0) {
        return a;
    }
    return gcd(b, a % b);
}

function begin(n, nums) {
    // print(nums)
    let dst = nums[0];
    for(let i = 0; i < nums.length; i++) {
        dst = gcd(dst, nums[i]);
    }
    let sum = 0;
    for(let i = 0; i < nums.length; i++) {
        let temp = nums[i]/dst;
        while(temp % 2 == 0) {
            temp = temp / 2;
            sum++;
        }
        while(temp % 3 == 0) {
            temp = temp / 3;
            sum++;
        }
        if(temp != 1) {
            print(-1);
            return
        }
    }
    print(sum)
    
}

function main() {
    var n = parseInt(readline(), 10);
    var x = readline()
        .trim()
        .split(' ')
        .map((y) => parseInt(y, 10));
    begin(n, x);
    
}