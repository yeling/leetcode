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

//TLE o(n^2)
function begin2(n, nums) {
    var gcd = function (a, b) {
        if (b == 0) {
            return a;
        }
        return gcd(b, a % b);
    }

    let max = -1;
    for(let i = 0; i < n; i++) {
        for(let j = 0; j < n; j++) {
            if(gcd(nums[i], nums[j]) == 1) {
                max = Math.max(max, i+j+2);
            }
        }
    }
    print(max);
}

function begin(n, nums) {
    var gcd = function (a, b) {
        if (b == 0) {
            return a;
        }
        return gcd(b, a % b);
    }
    let cache = new Array(1001).fill(-1);
    for(let i = 0; i < n; i++) {
        cache[nums[i]] = Math.max(cache[nums[i]], i+1);
    }

    let max = -1
    for(let i = 1; i <= 1000; i++) {
        for(let j = 1; j <= 1000; j++) {
            if(cache[i] != -1 && cache[j] != -1 && gcd(i, j) == 1) {
                max = Math.max(max, cache[i]+cache[j]);
            }
        }
    }
    print(max);
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