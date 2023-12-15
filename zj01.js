/*
* auther yeling
* zj-future01. 信号接收
* 
*/
var canReceiveAllSignals = function(intervals) {
    //console.log(`${signals.join(' ')}`);
    intervals.sort((a,b) => {
        return a[0] - b[0];
    })
    //console.log(`${signals.join(' ')}`);
    let ret = true;
    for(let i = 0; i < intervals.length - 1; i++) {
        if(intervals[i][1] > intervals[i + 1][0]) {
            return false;
        }
    }
    return true;

};

let signals = [[9,12],[2,9]];
console.log(canReceiveAllSignals(signals));
