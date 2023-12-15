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
    // print(n, nums.join(' '))
    let father = new Array(10 ** 9);
    // for(let i = 0; i < father.length; i++) {
    //     father[i] = i;
    // }
    //查找father
    var find = function(father, u) {
        if(father[u] == null) {
            father[u] = u;
        }
        if(father[u] != u) {
            father[u] = find(father,father[u])
        }
        return father[u];
    }

    //合并
    var join = function(father, u, v) {
        let fu = find(father,u);
        let fv = find(father,v);
        if(fu == null) {
            fu = u;
        }
        if(fv == null) {
            fv = v;
        }
        if(fu != fv) {
            father[fu] = fv;
        }
    }

    for(let i = 0; i < n; i++) {
        let temp = nums[i];
        join(father, temp[0], temp[1]);
    }

    let dstFather = find(father, 1);
    let max = 1;
    if(dstFather == null) {
        print(max);
        return;
    } 
    
    for(let i = 0; i < n; i++) {
        //这里是节点合并
        let temp = nums[i];
        let f = find(father,temp[0]);
        f = find(father,temp[1]);
        if(f == dstFather) {
            max = Math.max(max, temp[0], temp[1]);
        }
    }
    print(max)
}

function main() {
    var n = parseInt(readline(), 10);
    let nums = []
    for(let i = 0; i < n; i++) {
        var x = readline()
        .trim()
        .split(' ')
        .map((y) => parseInt(y, 10));
        nums.push(x);
    }
    begin(n, nums);
    
}