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

function begin(n, m, nums) {
    //print(`${n} ${m} ${nums}`)
    let cache = new Array(n + 1).fill(0).map(() => new Array());
    for(let i = 0; i < nums.length; i++) {
        cache[nums[i][0]].push(nums[i][1]);
        cache[nums[i][1]].push(nums[i][0]);
    }
    for(let i = 1; i <= n; i++) {
        let temp = cache[i].sort((a,b) => a - b);
        print(`${temp.length} ${temp.join(' ')}`);
    }
}

function main() {
    var size = readline()
        .trim()
        .split(' ')
        .map((y) => parseInt(y, 10));
    let nums = [];
    let x = null;
    while ((x = readline()) != null) {
        let temp = x.trim()
            .split(' ')
            .map((y) => parseInt(y, 10));
        nums.push(temp);
    }

    begin(size[0], size[1], nums);

}