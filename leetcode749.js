/*
* auther yeling
* 749. 隔离病毒
* 坑太多了
*/

/**
 * @param {number[][]} isInfected
 * @return {number}
 */
//13 / 32 54,56
//22 / 32 68,59
//30 / 32 40,38

var containVirus = function (isInfected) {
    //father数组初始化
    let m = isInfected.length;
    let n = isInfected[0].length;
    let father = new Array(m * n);
    let wall = new Array(2 * m * n);
    wall.fill(0);
    //计算每个点的边界，边界也需要合并传递
    let border = new Map();
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            father[i * n + j] = i * n + j;
        }
    }
    //查找father
    var find = function (father, u) {
        if (father[u] != u) {
            father[u] = find(father, father[u]);
            //
            let fu = u, fv = father[u];
            let fvborder = border.get(fv);
            let fuborder = border.get(fu);
            if (fvborder == null) {
                fvborder = [];
                border.set(fv, fvborder);
            }
            if (fuborder == null) {
                fuborder = []
            }
            fvborder.push(...fuborder);
            border.delete(fu);
        }
        return father[u];
    }

    //合并
    var join = function (father, u, v) {

        let fu = find(father, u);
        let fv = find(father, v);
        if (fu != fv) {
            father[fu] = fv;
            let fvborder = border.get(fv);
            let fuborder = border.get(fu);
            if (fvborder == null) {
                fvborder = [];
                border.set(fv, fvborder);
            }
            if (fuborder == null) {
                fuborder = []
            }
            fvborder.push(...fuborder);
            border.delete(fu);
        }
        //console.log(`join ${u} ${v} ${father}`);
    }

    let DIRS = [[0, 1], [-1, 0], [0, -1], [1, 0]];

    let count = 0;
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (isInfected[i][j] == 1) {
                //先计算边界
                for (let k = 0; k < DIRS.length; k++) {
                    if (i + DIRS[k][0] >= 0 && i + DIRS[k][0] < m
                        && j + DIRS[k][1] >= 0 && j + DIRS[k][1] < n
                        && isInfected[i + DIRS[k][0]][j + DIRS[k][1]] == 0) {
                        let borderList = border.get(i * n + j);
                        if (borderList == null) {
                            borderList = [];
                            border.set(i * n + j, borderList);
                        }
                        switch (DIRS[k].toString()) {
                            case '-1,0':
                                borderList.push(n * i + j);
                                break;
                            case '0,-1':
                                borderList.push(m * n + n * i + j);
                                break;
                            case '1,0':
                                borderList.push(n * (i + 1) + j);
                                break;
                            case '0,1':
                                borderList.push(m * n + n * i + j + 1);
                                break;
                        }
                    }
                }
                for (let k = 0; k < DIRS.length; k++) {
                    if (i + DIRS[k][0] >= 0 && i + DIRS[k][0] < m
                        && j + DIRS[k][1] >= 0 && j + DIRS[k][1] < n
                        && isInfected[i + DIRS[k][0]][j + DIRS[k][1]] == 1) {
                        join(father, i * n + j, (i + DIRS[k][0]) * n + j + DIRS[k][1]);
                    }
                }
            }
        }
    }
    //这里是节点合并
    for (let i = 0; i < father.length; i++) {
        find(father, i);
    }
    //console.log(father);
    //console.log(border);

    while (border.size > 0) {
        //最大的边界，加墙，不是活跃边界，边界最大的，并不是威胁最大的，还需要求一下
        let maxWall = 0;
        let maxFather = 0;
        border.forEach((value, key) => {
            
            let nextList = value;
            let nextSet = new Set();
            for (let i = 0; i < nextList.length; i++) {
                let next = nextList[i];
                if (next >= m * n) {
                    let x = Math.floor((next - m * n) / n);
                    let y = (next - m * n) % n;
                    if (isInfected[x][y] == 0 && isInfected[x][y - 1] == 1) {
                        nextSet.add(x * m + y);
                    } else if (isInfected[x][y] == 1 && isInfected[x][y - 1] == 0) {
                        nextSet.add(x * m + y - 1);
                    }
                } else {
                    let x = Math.floor((next / n)) - 1;
                    let y = next % n;
                    if (isInfected[x][y] == 0 && isInfected[x + 1][y] == 1) {
                        nextSet.add(x * m + y);
                    } else if (isInfected[x][y] == 1 && isInfected[x + 1][y] == 0) {
                        nextSet.add((x+1) * m + y);
                    }
                }
            }
            if (nextSet.size > maxWall) {
                maxWall = nextSet.size;
                maxFather = key;
            }
        });
        if (maxWall == 0) {
            break;
        }
        count += border.get(maxFather).length;
        let newWall = 0;
        border.get(maxFather).forEach((wallIndex) => {
            if (wall[wallIndex] == 0) {
                newWall++;
            }
            wall[wallIndex] = 1;
        })
        border.delete(maxFather);
        //console.log(`newWall  ${newWall} maxWall  ${maxWall} maxFather ${maxFather}`)
        //其他位置，感染下一个位置
        let newPosArray = new Array();
        border.forEach((value, key) => {
            let nextList = value;
            for (let i = 0; i < nextList.length; i++) {
                let next = nextList[i];
                if (next >= m * n) {
                    let x = Math.floor((next - m * n) / n);
                    let y = (next - m * n) % n;
                    if (isInfected[x][y] == 0 && isInfected[x][y - 1] == 1) {
                        isInfected[x][y] = 1;
                        newPosArray.push({ f: { x: x, y: y - 1 }, c: { x: x, y: y } });
                    } else if (isInfected[x][y] == 1 && isInfected[x][y - 1] == 0) {
                        isInfected[x][y - 1] = 1;
                        newPosArray.push({ f: { x: x, y: y }, c: { x: x, y: y - 1 } });
                    }
                } else {
                    let x = Math.floor((next / n)) - 1;
                    let y = next % n;
                    if (isInfected[x][y] == 0 && isInfected[x + 1][y] == 1) {
                        isInfected[x][y] = 1;
                        newPosArray.push({ f: { x: x + 1, y: y }, c: { x: x, y: y } });
                    } else if (isInfected[x][y] == 1 && isInfected[x + 1][y] == 0) {
                        isInfected[x + 1][y] = 1;
                        newPosArray.push({ f: { x: x, y: y }, c: { x: x + 1, y } });
                    }
                }
            }
        });
        //清除border，重新计算border
        border.clear();
        //console.log(border);

        for (let i = 0; i < newPosArray.length; i++) {
            //先计算边界
            let x = newPosArray[i].c.x;
            let y = newPosArray[i].c.y;
            for (let k = 0; k < DIRS.length; k++) {
                if (x + DIRS[k][0] >= 0 && x + DIRS[k][0] < m
                    && y + DIRS[k][1] >= 0 && y + DIRS[k][1] < n
                    && isInfected[x + DIRS[k][0]][y + DIRS[k][1]] == 0) {
                    let borderList = border.get(x * n + y);
                    if (borderList == null) {
                        borderList = [];
                        border.set(x * n + y, borderList);
                    }
                    switch (DIRS[k].toString()) {
                        case '-1,0':
                            borderList.push(n * x + y);
                            break;
                        case '0,-1':
                            borderList.push(m * n + n * x + y);
                            break;
                        case '1,0':
                            borderList.push(n * (x + 1) + y);
                            break;
                        case '0,1':
                            borderList.push(m * n + n * x + y + 1);
                            break;
                    }
                }
            }
            //join(father,newPosArray[i].c.x*n + newPosArray[i].c.y,newPosArray[i].f.x*n + newPosArray[i].f.y);
            for (let k = 0; k < DIRS.length; k++) {
                if (x + DIRS[k][0] >= 0 && x + DIRS[k][0] < m
                    && y + DIRS[k][1] >= 0 && y + DIRS[k][1] < n
                    && isInfected[x + DIRS[k][0]][y + DIRS[k][1]] == 1) {
                    //避免穿墙
                    switch (DIRS[k].toString()) {
                        case '-1,0':
                            if (wall[n * x + y] != 0) {
                                continue;
                            }
                            break;
                        case '0,-1':
                            if (wall[m * n + n * x + y] != 0) {
                                continue;
                            }
                            break;
                        case '1,0':
                            if (wall[n * (x + 1) + y] != 0) {
                                continue;
                            }
                            break;
                        case '0,1':
                            if (wall[m * n + n * x + y + 1] != 0) {
                                continue;
                            }
                            break;
                    }
                    join(father, newPosArray[i].c.x * n + newPosArray[i].c.y, (newPosArray[i].c.x + DIRS[k][0]) * n + newPosArray[i].c.y + DIRS[k][1]);
                }
            }
        }
        for (let i = 0; i < father.length; i++) {
            find(father, i);
        }
        //console.log(father);
    }
    return count;
};

isInfected = [[0, 1, 0, 0, 0, 0, 0, 1], [0, 1, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0]]

isInfected = [[1, 1, 1], [1, 0, 1], [1, 1, 1]];

isInfected = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 1, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]];

isInfected = [[0, 0, 1, 1, 1, 0, 1, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1, 0, 1], [0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 1, 0, 1, 0, 0, 0], [1, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 1, 0, 1, 1, 0, 0, 0], [1, 0, 0, 0, 0, 1, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 1, 0, 0, 0, 0, 0, 0, 1, 0], [1, 1, 0, 0, 0, 1, 0, 1, 0, 0]]

isInfected = [[0, 1, 0, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0, 0, 1, 0], [0, 0, 0, 1, 1, 0, 0, 1, 1, 0], [0, 1, 0, 0, 1, 0, 1, 1, 0, 1], [0, 0, 0, 1, 0, 1, 0, 1, 1, 1], [0, 1, 0, 0, 1, 0, 0, 1, 1, 0], [0, 1, 0, 1, 0, 0, 0, 1, 1, 0], [0, 1, 1, 0, 0, 1, 1, 0, 0, 1], [1, 0, 1, 1, 0, 1, 0, 1, 0, 1]]
// console.log(isInfected);
console.log(`${containVirus(isInfected)}`);

// let dir = [1, 0];
// console.log(`${dir.toString()} ${dir.toString() === '1,0'}`);