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

function begin(n, q, nums, querys) {
    //print(n, q, nums, querys);
    let odd = 0;
    let even = 0;
    let sum = 0;
    for (let i = 0; i < n; i++) {
        if (nums[i] % 2 == 0) {
            even++;
        } else {
            odd++;
        }
        sum += nums[i];
    }
    for (let i = 0; i < q; i++) {
        if (querys[i][0] == 0) {
            if (querys[i][1] % 2 == 0) {
                sum += even * querys[i][1];
            } else {
                sum += even * querys[i][1];
                odd += even;
                even = 0;
            }
        } else if (querys[i][0] == 1) {
            if (querys[i][1] % 2 == 0) {
                sum +=  odd * querys[i][1];
            } else {
                sum +=  odd * querys[i][1];
                even += odd;
                odd = 0;
            }
        }
        print(sum);
    }
}

function main() {
    var caseNum = parseInt(readline(), 10);
    for (var i = 0; i < caseNum; i++) {
        var n = readline()
            .trim()
            .split(' ')
            .map((y) => parseInt(y, 10));

        var x = readline()
            .trim()
            .split(' ')
            .map((y) => parseInt(y, 10));

        let querys = [];
        for (let j = 0; j < n[1]; j++) {
            var temp = readline()
                .trim()
                .split(' ')
                .map((y) => parseInt(y, 10));
            querys.push(temp);

        }
        begin(n[0], n[1], x, querys);
    }
}