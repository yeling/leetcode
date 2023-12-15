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

function begin(grid) {
    var row = new Array(8).fill(0);
    var col = new Array(8).fill(0);
    var i = 0;
    for(i = 7; i >= 0; i--) {
        for(var j = 0; j < 8; j++) {
            if(grid[i][j] == 'R') {
                row[i]++;                
            } else if(grid[i][j] == 'B') {                
                col[j]++;
            }
        }
    }
    for( i = 0; i < 8; i++) {
        if(row[i] == 8 ) {
            print("R");
            break;
        }
        if(col[i] == 8) {
            print("B");
            break;
        }
    }
}

function main() {
    var caseNum = parseInt(readline(), 10);
    for (var i = 0; i < caseNum; i++) {
        readline();
        var grid = [];
        for(var j = 0; j < 8; j++) {
            var x = readline()
            .trim()
            .split('');
            grid.push(x);
        }
        begin(grid);
    }
}