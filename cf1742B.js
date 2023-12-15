/*
* auther yeling
* 
* 
*/
// const { readline, print, testOutput } = require('@ip-algorithmics/codeforces-io');

function begin(nums) {
    nums.sort((a,b) => a - b);
    for(var i = 1; i < nums.length; i++) {
        if(nums[i] == nums[i-1]) {
            print("NO");
            return;
        }
    }
    print("YES");
}

var caseNum = parseInt(readline(), 10);
for (var i = 0; i < caseNum; i++) {
    var n = parseInt(readline(), 10);
    var x = readline()
        .trim()
        .split(' ')
        .map((y) => parseInt(y, 10));
        begin(x);
}

// testOutput(); // Result Passed