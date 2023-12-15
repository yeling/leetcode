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

function begin2(n, str) {
    // print(`${n} ${str}`);
    //s1去除前导0后的s
    let s1 = '';
    for (let i = 0; i < str.length; i++) {
        if (str.charAt(i) == '0' && s1.length == 0) {
            continue;
        } else {
            s1 += str.charAt(i);
        }
    }
    if(s1.length == 0) {
        s1 = '0';
    }
    //计算s2 s2需要和s1末位对其，然后高位尽可能的matcher need，只需要计算startPos之前的位置
    // print(s1);

    let need = '';
    let startPos = -1;
    for (let i = 0; i < s1.length; i++) {
        if (s1.charAt(i) == '0') {
            if(startPos == -1) {
                startPos = i;
            }
            need += '1';
        } else if (need.length > 0) {
            need += '*';
        }
    }
    if(need.length == 0) {
        print(s1);
        return;
    }
    //print(need);

    
    let maxLen = 0;
    let maxPos = 0;
    for (let i = 0; i < startPos; i++) {
        let tempLen = 0;
        for (let j = 0; j < need.length; j++) {
            if(s1.charAt(i + j) == need.charAt(j) || need.charAt(j) == '*') {
                tempLen++;
                continue;
            } else {
                break;
            }
        }        
        if(tempLen > maxLen) {
            maxLen = tempLen;
            maxPos = i;
        }        
        print(`${i} ${maxLen} ${tempLen}`);
    }
    let res = [];
    for (let i = 0; i < s1.length; i++) {
        if( i < startPos + maxLen) {
            res.push(1);
        } else {
            res.push(Number(s1.charAt(i)) | Number(s1.charAt(i - (startPos + 1))));
        }
    }
    print(res.join(''));
}


function begin(n, str) {
    // print(`${n} ${str}`);
    //s1去除前导0后的s
    let startPos = -1;
    for (let i = 0; i < str.length; i++) {
        if (str.charAt(i) != '0') {
            startPos = i;
            break;        
        } 
    }
    if(startPos == -1) {
        print('0');
        return;
    }
    let s1 = str.split('').slice(startPos).map((value) => parseInt(value));
    print(s1);
    
    
}
function main() {
    var n = parseInt(readline(), 10);
    var x = readline().trim();
    begin(n, x);
}