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
    // print(`${n} ${nums}`);
    let stack = [];
    let index = 0;
    for(let i = n - 1; i >= 0; i--) {
        if(stack.length == 0 || stack[stack.length - 1] > nums[i]) { 
            stack.push(nums[i]);
        } else {
            stack.push(nums[i]);
            index = i;
            break;
        }
    }
    stack.sort((a,b) => {
        return b - a;
    })
    for(let i = 0; i < stack.length; i++) {
        if(stack[i] < nums[index]) {
            let first = stack[i];
            // stack.splice(i,1,nums[index]);
            // stack.sort((a,b) => b - a);
            stack.splice(i,1);
            stack.splice(0,0,first);
            break;
        }
    }
    let res = nums.slice(0,index);
    res.push(...stack);
    print(res.join(' '));
}

function begin2(n, ps) {
    for (let i = n-2; i >= 0; i--) {
        const left = ps[i];
        const right = ps[i+1];
        if (left < right) {
            continue
        } else {
            const leftThanI = ps.slice(0, i);
            const numAtI = ps[i];
            const rightThanI = ps.slice(i+1);
 
            const newNumAtI = rightThanI.sort((a,b)=>b-a).filter(n=>n<numAtI)[0];
            const newRightThanI = rightThanI.filter(n=>n!==newNumAtI).concat([numAtI]).sort((a,b)=>b-a);
            // console.log(i);
            console.log([...leftThanI, newNumAtI, ...newRightThanI].join(' '));
            return
        }
    }
}


function main() {
    var n = parseInt(readline(), 10);
    var x = readline()
        .trim()
        .split(' ')
        .map((y) => parseInt(y, 10));
    begin(n, x);
    // begin2(n, x);
    
}