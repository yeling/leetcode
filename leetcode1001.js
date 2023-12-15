/*
* auther yeling
* 1001. 网格照明
* 
*/

/**
 * @param {number} n
 * @param {number[][]} lamps
 * @param {number[][]} queries
 * @return {number[]}
 */
var gridIllumination = function (n, lamps, queries) {
    let row = new Map();
    let col = new Map();
    let line1 = new Map();
    let line2 = new Map();
    let allLamps = new Map();
    for (let i = 0; i < lamps.length; i++) {
        let item = row.get(lamps[i][1]);
        if(allLamps.get(lamps[i][0] * n + lamps[i][1]) != null) {
            continue;
        }
        allLamps.set(lamps[i][0] * n + lamps[i][1], 1);
        if (item == null) {
            item = 0;
        }
        item++;
        row.set(lamps[i][1], item);

        item = col.get(lamps[i][0]);
        if (item == null) {
            item = 0;
        }
        item++;
        col.set(lamps[i][0], item);

        item = line1.get(lamps[i][1] - lamps[i][0]);
        if (item == null) {
            item = 0;
        }
        item++;
        line1.set(lamps[i][1] - lamps[i][0], item);

        item = line2.get(lamps[i][1] + lamps[i][0]);
        if (item == null) {
            item = 0;
        }
        item++;
        line2.set(lamps[i][1] + lamps[i][0], item);
    }
    // console.log(row);
    // console.log(col);
    // console.log(line1);
    // console.log(line2);
    let res = [];
    for (let i = 0; i < queries.length; i++) {
        let item = row.get(queries[i][1]);
        if (item == null) {
            item = col.get(queries[i][0]);
        }
        if (item == null) {
            item = line1.get(queries[i][1] - queries[i][0]);
        }
        if (item == null) {
            item = line2.get(queries[i][1] + queries[i][0]);
        }
        res.push(item == null ? 0 : 1);
        //close light
        let delta = [-1, 0, 1];
        for (let j = 0; j < delta.length; j++) {
            for (let k = 0; k < delta.length; k++) {
                let x = queries[i][0] + delta[j];
                let y = queries[i][1] + delta[k];
                if (x >= 0 && x <= n - 1 && y >= 0 && y <= n - 1) {  
                    if(allLamps.get(x * n + y) != null) {
                        //close light
                        allLamps.delete(x * n + y);
                        let item = row.get(y);
                        if (item != null) {
                            item--;
                            if(item == 0) {
                                row.delete(y);
                            } else {
                                row.set(y, item);
                            }
                        }
                        item = col.get(x);
                        if (item != null) {
                            item--;
                            if(item == 0) {
                                col.delete(x);
                            } else {
                                col.set(x, item);
                            }
                        }

                        item = line1.get(y - x);
                        if (item != null) {
                            item--;
                            if(item == 0) {
                                line1.delete(y - x);
                            } else {
                                line1.set(y - x, item);
                            }
                        }

                        item = line2.get(y + x);
                        if (item != null) {
                            item--;
                            if(item == 0) {
                                line2.delete(y + x);
                            } else {
                                line2.set(y + x, item);
                            }
                        }

                    }
                }
            }
        }
    }
    return res;
};

n = 5, lamps = [[0, 0], [4, 4]], queries = [[1, 1], [1, 0]]
// n = 5, lamps = [[0,0],[4,4]], queries = [[1,1],[1,1]]
n = 5, lamps = [[0,0],[0,4]], queries = [[0,4],[0,1],[1,4]]
n = 6
lamps = [[2,5],[4,2],[0,3],[0,5],[1,4],[4,2],[3,3],[1,0]]
queries = [[4,3],[3,1],[5,3],[0,5],[4,4],[3,3]]
//[1,0,1,1,0,1]
console.log(gridIllumination(n, lamps, queries));
