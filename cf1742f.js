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
//TLE Case2
function begin2(n, ops) {
    let s = new Array(26).fill(0);
    let t = new Array(26).fill(0);
    s[0] = t[0] = 1;
    for (let i = 0; i < n; i++) {
        let type = ops[i][0];
        let times = ops[i][1];
        let str = ops[i][2];
        
        if (type == 1) {
            //s
            for (let j = 0; j < str.length; j++) {
                s[str.charCodeAt(j) - 97] += times;
            }
        } else if (type == 2) {
            //t
            for (let j = 0; j < str.length; j++) {
                
                t[str.charCodeAt(j) - 97] += times;
            }
        }
        //compare
        let sStr = '';
        let tStr = '';
        for(let j = 0; j < 26; j++) {
            let temp = String.fromCharCode(j + 97)
            for(let k = 0; k < s[j]; k++) {
                sStr += temp;
            }
            temp = String.fromCharCode(25 - j + 97)
            for(let k = 0; k < t[25 - j]; k++) {
                tStr += temp;
            }
        }
        
        //print(`${sStr} ${tStr}`);
        if(sStr.localeCompare(tStr) < 0) {
            print('YES');
        } else {
            print('NO');
        }
    }

}

//TLE case3
function begin3(n, ops) {
    let s = new Array(26).fill(0);
    let t = new Array(26).fill(0);
    s[0] = t[0] = 1;
    for (let i = 0; i < n; i++) {
        let type = ops[i][0];
        let times = ops[i][1];
        let str = ops[i][2];
        
        if (type == 1) {
            //s
            for (let j = 0; j < str.length; j++) {
                s[str.charCodeAt(j) - 97] += times;
            }
        } else if (type == 2) {
            //t
            for (let j = 0; j < str.length; j++) {
                
                t[str.charCodeAt(j) - 97] += times;
            }
        }
        //compare
        let sIndex = 0;
        let si = 0;

        let tIndex = 0;
        let ti = 25;

        let index = 0;
        let smaller = false;
        while(si < 26 && ti >= 0) {
            while(sIndex > s[si] - 1) {
                si++;
                sIndex = 0;
            }
            while(tIndex > t[ti] - 1) {
                ti--;
                tIndex = 0;
            }
            
            if(si < ti) {
                smaller = true;
                print('YES');
                break;
            } else if(si == 26 && ti >= 0) {
                //si没有数据了， ti还有数据
                smaller = true;
                print('YES');
                break;
            } else if(si > ti) {
                print('NO');
                break;
            }
            index++;
            sIndex++;
            tIndex++;
        }
    }

}


function begin(n, ops) {
    let s = new Array(26).fill(0);
    let t = new Array(26).fill(0);
    s[0] = t[0] = 1;
    for (let i = 0; i < n; i++) {
        let type = ops[i][0];
        let times = ops[i][1];
        let str = ops[i][2];
        
        if (type == 1) {
            //s
            for (let j = 0; j < str.length; j++) {
                s[str.charCodeAt(j) - 97] += times;
            }
        } else if (type == 2) {
            //t
            for (let j = 0; j < str.length; j++) {
                
                t[str.charCodeAt(j) - 97] += times;
            }
        }
        //compare
        let sIndex = 0;
        let si = 0;

        let tIndex = 0;
        let ti = 25;

        let index = 0;
        let smaller = false;
        while(si < 26 && ti >= 0) {
            while(sIndex > s[si] - 1) {
                si++;
                sIndex = 0;
            }
            while(tIndex > t[ti] - 1) {
                ti--;
                tIndex = 0;
            }
            
            if(si < ti) {
                smaller = true;
                print('YES');
                break;
            } else if(si == 26 && ti >= 0) {
                //si没有数据了， ti还有数据
                smaller = true;
                print('YES');
                break;
            } else if(si > ti) {
                print('NO');
                break;
            }
            index++;
            sIndex++;
            tIndex++;
        }
    }

}
//begin(4, [[2,1,'aa'],[1,2,'a'],[2,3,'a'],[1,2,'b']]);

function main() {
    var caseNum = parseInt(readline(), 10);
    for (var i = 0; i < caseNum; i++) {
        var n = parseInt(readline().trim(), 10);
        //print(n);
        let ops = new Array();
        for (let j = 0; j < n; j++) {
            var x = readline();
            if(x == null) {
                continue;
            }
            x.trim().split(' ');
            //print(x);
            ops.push([Number(x[0]), Number(x[1]), x[2]]);
        }
        begin(n, ops);
    }
}