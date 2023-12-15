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
    nums = nums.map((value) => {
        let ret = [];
        if(value[0] < value[1]) {
            ret = value;
        } else {
            ret = [value[1], value[0]];
        }
        return ret;
    })
    //print(nums.join(' '));
    nums.sort((a,b) => {
        return a[1] - b[1];
    })
    //print(nums);
    let sum = 0;
    for(let i = 0; i < nums.length; i++) {
        if(i == 0 ) {
            sum += nums[i][1];
        }
        if(i == nums.length - 1) {
            sum += nums[i][1];
        }
        sum += 2 * nums[i][0];
        if(i > 0) {
            sum += nums[i][1] - nums[i-1][1];
        }
    }
    print(sum);
}

function main() {
    var caseNum = parseInt(readline(), 10);
    for (var i = 0; i < caseNum; i++) {
        var n = parseInt(readline(), 10);
        let nums = [];
        for(let j = 0; j < n; j++) {
            var x = readline()
            .trim()
            .split(' ')
            .map((y) => parseInt(y, 10));
            nums.push(x);
        }
        begin(n, nums);
    }
}