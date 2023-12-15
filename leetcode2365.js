/*
* auther yeling
* 
* 
*/

/**
 * @param {number[]} tasks
 * @param {number} space
 * @return {number}
 */
// 53 / 61 个通过测试用例 超时
var taskSchedulerII2 = function (tasks, space) {
    let n = tasks.length;
    let cache = new Array();
    let sum = 0;
    let index = 0;
    while (index < n) {
        //console.log(cache);
        let find = false;
        for (let j = 0; j < cache.length; j++) {
            if (tasks[index] == cache[j]) {
                find = true;
                break;
            }
        }
        if (find) {
            //rest
            sum++;
            cache.push(0);
            if (cache.length > space) {
                cache.shift();
            }
        } else {
            sum++;
            cache.push(tasks[index]);
            if (cache.length > space) {
                cache.shift();
            }
            index++;
        }
    }
    return sum;
};

var taskSchedulerII3 = function (tasks, space) {
    let n = tasks.length;
    let cache = new Array();
    let taskType = new Map();
    let sum = 0;
    let index = 0;
    while (index < n) {
        //console.log(cache);
        let size = taskType.get(tasks[index]);
        if (size != null) {
            let findIndex = 0;
            for (let j = cache.length - 1; j >= 0; j--) {
                if (tasks[index] == cache[j]) {
                    findIndex = j;
                    find = true;
                    break;
                }
            }
            //rest
            sum += findIndex + 1;
            for (let i = 0; i < findIndex + 1; i++) {
                cache.push(0);
                if (cache.length > space) {
                    let type = cache.shift();
                    if (type != 0) {
                        let size = taskType.get(type);
                        size--;
                        if (size == 0) {
                            taskType.delete(type);
                        } else {
                            taskType.set(type, size);
                        }
                    }
                }
            }
        } else {
            sum++;
            cache.push(tasks[index]);
            taskType.set(tasks[index], 1);

            if (cache.length > space) {
                let type = cache.shift();
                if (type != 0) {
                    let size = taskType.get(type);
                    size--;
                    if (size == 0) {
                        taskType.delete(type);
                    } else {
                        taskType.set(type, size);
                    }
                }
            }
            index++;
        }
    }
    return sum;
};

var taskSchedulerII4 = function (tasks, space) {
    let n = tasks.length;
    let cache = new Array();
    let sum = 0;
    let index = 0;
    while (index < n) {
        console.log(cache);
        let find = false;
        let findIndex = 0;
        for (let j = cache.length - 1; j >= 0; j--) {
            if (tasks[index] == cache[j]) {
                findIndex = j;
                find = true;
                break;
            }
        }
        if (find) {
            //rest
            sum += findIndex + 1;
            for (let i = 0; i < findIndex + 1; i++) {
                cache.push(0);
                if (cache.length > space) {
                    cache.shift();
                }
            }
        } else {
            sum++;
            cache.push(tasks[index]);
            if (cache.length > space) {
                cache.shift();
            }
            index++;
        }
    }
    return sum;
};

var taskSchedulerII = function (tasks, space) {
    let n = tasks.length;
    let cache = new Map();
    let sum = 0;
    let index = 0;
    while (index < n) {
        if (cache.has(tasks[index]) == false) {
            sum++;
        } else {
            let pre = cache.get(tasks[index]);
            if (sum - pre > space) {
                sum++;
            } else {
                sum = pre + space + 1;
            }
        }
        cache.set(tasks[index], sum);
        index++;
    }
    return sum;
};

tasks = [5, 8, 8, 5], space = 2
// tasks = [1,2,1,2,3,1], space = 3
// tasks = [4,10,10,9,10,4,10,4], space =8

tasks = [318204991,287789205,480133588,568010540,764872424,458191253,569820556,967827094,32718209,933225625,361858270,614117739,445623884,68371675,894522481,155784383,786336698,539137871,45582009,809265305,279043681,780464024,559921920,29782662,389609904,506428863,412307280];
space = 38692
console.time('taskSchedulerII')
console.log(taskSchedulerII(tasks, space));
console.timeLog('taskSchedulerII')
console.log(taskSchedulerII3(tasks, space));
console.timeEnd('taskSchedulerII')