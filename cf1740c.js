/*
* auther yeling
* 
* 
*/
// 'use strict';

// process.stdin.resume();
// process.stdin.setEncoding('utf-8');

// let inputString = '';
// let currentLine = 0;

// process.stdin.on('data', inputStdin => {
//     inputString += inputStdin;
// });

// process.stdin.on('end', _ => {
//     inputString = inputString.trim().split('\n').map(string => {
//         return string.trim();
//     });
    
//     main();    
// });

// function readline() {
//     return inputString[currentLine++];
// }
// function print(str) {
//     console.log(str);
// }

const { readline, print, testOutput } = require('@ip-algorithmics/codeforces-io');
main();
testOutput();

function begin2(n, nums) {
    nums.sort((a,b) => a - b);
    let w3 = nums[0];
    let w2 = nums[n - 1];
    let w1 = nums[n - 2];
    let res = 2 * w2 - w1 - w3;
    print(res); 
}

function begin(n, nums) {
    nums.sort((a,b) => a - b);
    let w1, w2, w3;
    let sum = 0;
    for(let i = 1; i < n; i++) {
        for(let j = i + 1; j < n; j++) {
            w1 = nums[i-1];
            w2 = nums[i];
            w3 = nums[j];
            let temp = 2 * w2 - w1 - w3;
            sum = Math.max(sum, temp);
        }
    }
    print(sum);
}


function begin3(n, nums) {
    let sum = 0;
    for(let i = 0; i < n; i++) {
        for(let j = 0; j < n; j++) {
            for(let k = 0; k < n; k++) {
                if(i != j && i != k && j != k) {
                    let w1 = nums[i];
                    let w2 = nums[j];
                    let w3 = nums[k];
                    let res = Math.abs(w2 - w1) + Math.abs(w3 - w2);
                    sum = Math.max(res, sum);
                    print(sum, res, w1, w2, w3);
                }
            }
        }
    }
    print(sum);

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
        begin2(n,x);
    }
}