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

function begin(n, nums, str) {
    //print(`${n} ${nums} ${str}`);
    
    let cache = new Map();
    for(let i = 0; i < n; i++) {
        let all = cache.get(nums[i]);
        if(all == null) {
            all = [];
        }
        all.push(i);
        cache.set(nums[i], all);
    }
    let keys =  Array.from(cache.keys());
    let find = true;
    for(let i = 0; i < keys.length; i++) {
        let all = cache.get(keys[i]);
        let dst = str.charAt(all[0]);
        for(let j = 1; j < all.length; j++) {
            if(str.charAt(all[j]) != dst) {
                find = false;
                break;
            }
        }
        if(find == false) {
            break;
        }
    }
    if(find) {
        print('YES');
    } else {
        print('NO');
    }
}
function main() {
    var caseNum = parseInt(readline(), 10);
    for (var i = 0; i < caseNum; i++) {
        var n = parseInt(readline(), 10);
        var x = readline()
            .trim()
            .split(' ')
            .map((y) => parseInt(y, 10));

        var str = readline().trim()
        begin(n, x, str);
    }
}
