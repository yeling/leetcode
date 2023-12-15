/*
* auther yeling
* https://codeforces.com/problemset/problem/1286/A
* 
*/
const { readline, print, testOutput } = require('@ip-algorithmics/codeforces-io');


function begin() {

    let numberOfLines = parseInt(readline(), 10);
    for (let i = 0; i < numberOfLines; i++) {
        let x = readline()
            .trim()
            .split(',')
            .map((y) => parseInt(y, 10));

        if ((x[0] < 90 && x[0] > -90) || (x[1] < 90 && x[1] > -90)) {
            print(x[0] + ',' + x[1]);
            break;
        }
    }
    testOutput(); // Result Passed
}

begin();