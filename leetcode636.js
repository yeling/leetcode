/*
* auther yeling
* 
* 
*/

/**
 * @param {number} n
 * @param {string[]} logs
 * @return {number[]}
 */
var exclusiveTime = function(n, logs) {
    let res = new Array(n).fill(0);
    let stack = new Array();
    logs.forEach((item) => {
        //console.log(res);
        let cur = item.split(':');
        let funcId = Number(cur[0]);
        let time = Number(cur[2]);
        if(cur[1] == 'start') {
            //前面一个暂停，时间累加
            let head = stack.pop();
            if(head != null) {
                res[head[0]] += time - head[1];
                stack.push(head);
            }
            stack.push([funcId,time]);
        } else if(cur[1] == 'end') {
            let head = stack.pop();
            if(head[0] == funcId) {
                res[funcId] += time - head[1] + 1;
            }
            //栈中的重新设置开始时间
            if(stack.length > 0) {
                stack.at(stack.length - 1)[1] = time + 1;
            }
        }

    })
    return res;
};

n = 2, logs = ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"];
logs = ["0:start:0","0:start:2","0:end:5","1:start:7","1:end:7","0:end:8"];

console.log(exclusiveTime(n,logs));
