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

function begin(steps, legs) {
    let n = steps.length;
    let q = legs.length;
    let res = new Array(q).fill(0);

    //print(steps);

    let maxSteps = new Array(n);
    let max = 0;
    for(let i = 0; i < n; i++) {
        if(steps[i] > max) {
            max = steps[i];
        }
        maxSteps[i] = max;
    }
    //print(maxSteps);

    let preSum = new Array(n);
    preSum[0] = steps[0];
    for(let i = 1; i < n; i++) {
        preSum[i] = steps[i] + preSum[i-1];
    }
    //print(preSum);

    let find = (num, nums) => {
        let left = 0, right = nums.length - 1;
        let target = num;
        while(left <= right) {
            let mid = left + Math.floor((right - left)/2);
            if(target < nums[mid]) {
                right = mid - 1;
            } else if(target >= nums[mid]) {
                left = mid + 1;
            }
        }
        return left;
    }

    for(let i = 0; i < q; i++) {
        let pos = find(legs[i], maxSteps);
        if(pos > 0) {
            res[i] = preSum[pos - 1];
        }
        //console.log(pos);
    }
    print(res.join(' '));
    
}

function main() {
    var caseNum = parseInt(readline(), 10);
    for (var i = 0; i < caseNum; i++) {
        var n = readline()
            .trim()
            .split(' ')
            .map((y) => parseInt(y, 10));
        let steps =  readline()
            .trim()
            .split(' ')
            .map((y) => parseInt(y, 10));
        let legs =  readline()
            .trim()
            .split(' ')
            .map((y) => parseInt(y, 10));
        begin(steps, legs);
    }
}