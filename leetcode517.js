/*
* auther yeling
* 
* 
*/

/**
 * @param {number[]} machines
 * @return {number}
 */
//43 / 120
//65 / 120
var findMinMoves2 = function (machines) {
    let n = machines.length;
    let sum = 0;
    for (let i = 0; i < n; i++) {
        sum += machines[i];
    }
    if (sum % n != 0) {
        return -1;
    }
    let ave = sum / n;
    let step = 0;
    while (true) {
        let end = true;
        let moveOut = false;
        for (let i = 0; i < n; i++) {
            if (machines[i] < ave && i + 1 < n) {
                if (machines[i + 1] > 0) {
                    machines[i + 1]--;
                    machines[i]++;
                    moveOut = true;
                    end = false;
                }
            } else if (machines[i] > ave && i + 1 >= 0) {
                if (moveOut == false) {
                    machines[i]--;
                    machines[i + 1]++;
                    moveOut = false;
                    end = false;
                }
            }
        }
        if (end == true) {
            break;
        } else {
            step++;
        }
        console.log(machines);
    }

    return step;
};

//45 / 120
//51 / 120
var findMinMoves = function (machines) {
    let n = machines.length;
    let sum = 0;
    for (let i = 0; i < n; i++) {
        sum += machines[i];
    }
    if (sum % n != 0) {
        return -1;
    }
    if(n == 1) {
        return 0;
    }
    let ave = sum / n;
    let ops = new Array(n).fill(0);
    let max = 0;
    for(let  i = 0; i < n; i++) {
        if(machines[i] < ave) {
            ops[i + 1] +=  ave - machines[i];
            machines[i+1] -= ave - machines[i];
            machines[i] = ave;
            
        } else if(machines[i] > ave) {
            ops[i] +=  machines[i] - ave;
            machines[i+1] += machines[i] - ave;
            machines[i] = ave; 
        }
        max = Math.max(max,ops[i]);
    }
    return max;
};

// machines = [1, 0, 5];
machines = [0,3,0];
machines = [0,0,0,4]
//machines = [100000, 0, 100000, 0, 100000, 0, 100000, 0, 100000, 0, 100000, 0];

// machines = [10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0];
console.log(machines);
console.log(findMinMoves(machines));