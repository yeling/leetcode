/*
* auther yeling
* 
* 
*/

/**
 * @param {number} n
 * @param {number[][]} meetings
 * @return {number}
 */
var mostBooked = function(n, meetings) {
    meetings.sort((a,b) => {
        return a[0] - b[0];
    })

    let res = new Array(n).fill(0);
    let endTime = new Array(n).fill(0);
    let time = 0;
    let index = 0;
    while(index < meetings.length) {
        //清空会议室
        for(let i = 0; i < n; i++) {
            if(endTime[i] <= meetings[index][0]) {
                endTime[i] = 0;
            }
        }
        //find empty
        let dst = -1;
        for(let i = 0; i < n; i++) {
            if(endTime[i] == 0) {
                dst = i;
                break;
            }
        }
        //有空会议室
        if(dst != -1) {
            if(time < meetings[index][0]) {
                time = meetings[index][0];
            }
            endTime[dst] = time + meetings[index][1] - meetings[index][0];
            res[dst]++;
            index++;
        } else {
            //没有空会议室，找到最小的时间空出来
            let min = endTime[0];
            let minPos = 0;
            for(let i = 0; i < n; i++) {
                if(endTime[i] < min) {
                    min = endTime[i];
                    minPos = i;
                }
            }
            //
            time = min;
            endTime[minPos] = 0;
        }
        console.log(endTime);
        console.log(time);
        //
    }

    let max = 0;
    let maxPos = 0;
    for(let i = 0; i < n; i++) {
        if(res[i] > max) {
            max = res[i];
            maxPos = i;
        }
    }
    return maxPos;
};

n = 3, meetings = [[1,20],[2,10],[3,5],[4,9],[6,8]];
n = 2, meetings = [[0,10],[1,5],[2,7],[3,4]];
n = 4,
meetings = [[18,19],[3,12],[17,19],[2,13],[7,10]]

console.log(mostBooked(n,meetings));
