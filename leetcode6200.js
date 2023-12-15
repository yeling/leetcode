/*
* auther yeling
* 
* 
*/

/**
 * @param {number} n
 * @param {number[][]} logs
 * @return {number}
 */
var hardestWorker = function(n, logs) {    
    let maxTime = 0;
    let id = Number.MAX_SAFE_INTEGER;
    for(let i = 0; i < logs.length; i++) {
        let currTime = 0
        if(i == 0) {
            currTime = logs[i][1];
        } else {
            currTime = logs[i][1] - logs[i - 1][1];
        }
        if(currTime > maxTime) {
            maxTime = currTime;
            id = logs[i][0];          
        } else if(currTime == maxTime){
            if(id > logs[i][0]) {
                id = logs[i][0];
            }
        }
    }
    return id;
};



n = 10, logs = [[0,3],[2,5],[0,9],[1,15],[2,21]]
n = 26, logs = [[1,1],[3,7],[2,12],[7,17]]
console.log(hardestWorker(n,logs));