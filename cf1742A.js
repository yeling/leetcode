/*
* auther yeling
* 
* 
*/
const { readline, print, testOutput } = require('@ip-algorithmics/codeforces-io');

function begin(a,b,c) {
    if(a == b + c) {
        print("YES");
    } else if(b == a + c) {
        print("YES");
    } else if(c == a + b) {
        print("YES");
    } else {
        print("NO");
    }
}

var caseNum = parseInt(readline(), 10);
for (var i = 0; i < caseNum; i++) {
    var x = readline()
        .trim()
        .split(' ')
        .map((y) => parseInt(y, 10));
        begin(x[0], x[1], x[2]);
}
//testOutput(); // Result Passed