/*
* auther yeling
* 
* 
*/

/**
 * @param {number[][]} intervals
 * @return {number}
 */
var minGroups = function(intervals) {
    let res = new Array();
    intervals.sort((a,b) => {
        if(a[0] == b[0]) {
            return a[1] - b[1];
        } else {
            return a[0] - b[0];
        }
    });
    //console.log(intervals.join(' '));
    for(let i = 0; i < intervals.length; i++) {
        let find = false;
        let curr = intervals[i];
        for(let j = 0; j < res.length; j++) {
            if(res[j] < curr[0]) {
                find = true;
                res[j] = curr[1];
                break;
            }
        }
        if(find == false) {
            res.push(curr[1]);
        }
        //console.log(res);
    }
    return res.length;
};



intervals = [[5,10],[6,8],[1,5],[2,3],[1,10]]
console.log(minGroups(intervals));

