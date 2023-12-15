/*
* auther yeling
* 
* 593. 有效的正方形
*/

/**
 * @param {number[]} p1
 * @param {number[]} p2
 * @param {number[]} p3
 * @param {number[]} p4
 * @return {boolean}
 */
//还需要考虑斜角
var validSquare2 = function (p1, p2, p3, p4) {

    //只能有两个x,y
    let ps = [p1, p2, p3, p4];
    ps.sort((a, b) => {
        if (a[0] == b[0]) {
            return a[1] - b[1];
        } else {
            return a[0] - b[0];
        }
    })
    console.log(ps.join(' '));
    if (ps[0][0] == ps[1][0] && ps[2][0] == ps[3][0] &&
        ps[0][1] == ps[2][1] && ps[1][1] == ps[3][1] &&
        ps[0][0] != ps[2][0] &&
        ps[0][0] - ps[2][0] == ps[0][1] - ps[1][1]) {
        return true;
    }
    return false;
};

//还需要考虑斜角
var validSquare3 = function (p1, p2, p3, p4) {

    //只能有两个x,y
    let ps = [p1, p2, p3, p4];
    ps.sort((a, b) => {
        if (a[0] == b[0]) {
            return a[1] - b[1];
        } else {
            return a[0] - b[0];
        }
    })
    console.log(ps.join(' '));
    //求边上相等
    let line = [];
    //简化成 y = ax + b; [a,b]表示一根线
    line.push([(ps[1][1] - ps[0][1])/(ps[1][0] - ps[0][0]),ps[1][1] - (ps[1][1] - ps[0][1])/(ps[1][0] - ps[0][0])*ps[1][0]]);
    line.push([(ps[2][1] - ps[1][1])/(ps[2][0] - ps[1][0]),ps[2][1] - (ps[2][1] - ps[1][1])/(ps[2][0] - ps[1][0])*ps[2][0]]);
    line.push([(ps[3][1] - ps[2][1])/(ps[3][0] - ps[2][0]),ps[3][1] - (ps[3][1] - ps[2][1])/(ps[3][0] - ps[2][0])*ps[3][0]]);
    line.push([(ps[0][1] - ps[3][1])/(ps[0][0] - ps[3][0]),ps[0][1] - (ps[0][1] - ps[3][1])/(ps[0][0] - ps[3][0])*ps[0][0]]);

    console.log(`line ${line}`);

    let degree = [];
    degree.push(Math.atan(-line[0][1]/line[0][0],line[0][1]));
    degree.push(Math.atan(-line[1][1]/line[1][0],line[1][1]));
    degree.push(Math.atan(-line[2][1]/line[2][0],line[2][1]));
    degree.push(Math.atan(-line[3][1]/line[3][0],line[3][1]));

    let deltaDegree = [];
    deltaDegree = [degree[1] - degree[0],degree[2] - degree[1], degree[3] - degree[2],degree[3] - degree[0]];
    console.log(deltaDegree);
    

    //角度均为90
    if (ps[0][0] == ps[1][0] && ps[2][0] == ps[3][0] &&
        ps[0][1] == ps[2][1] && ps[1][1] == ps[3][1] &&
        ps[0][0] != ps[2][0] &&
        ps[0][0] - ps[2][0] == ps[0][1] - ps[1][1]) {
        return true;
    }
    return false;
};

var validSquare4 = function (p1, p2, p3, p4) {

    //只能有两个x,y
    let ps = [p1, p2, p3, p4];
     //求边长相等
    let line = [];
    for(let i = 0; i < 4; i++) {
        for(let j = i + 1; j < 4; j++) {
            let dis = Math.sqrt((ps[i][1] - ps[j][1]) * (ps[i][1] - ps[j][1]) + (ps[i][0] - ps[j][0]) * (ps[i][0] - ps[j][0]));
            line.push(dis);
        }
    }
    //边长只有两种
    let lineSet = new Set();
    line.forEach((value) => {
        lineSet.add(value.toFixed(8));
    })
    console.log(line);
    let lk = Array.from(lineSet).sort((a,b)=> a - b);
    console.log(lk);
    console.log(2 * lk[0] * lk[0]);
    console.log(lk[1] * lk[1]);
    console.log(Math.abs(2 * lk[0] * lk[0] - lk[1] * lk[1]));
    let delta = Math.abs(2 * lk[0] * lk[0] - lk[1] * lk[1])
    if(lk.length == 2 && delta < 0.001) {
        return true;
    }
    return false;
};


//102 / 253 
//141 / 253
//151 / 253
//227 / 253
//252 / 253
//还需要考虑斜角，会损失精度
var validSquare = function (p1, p2, p3, p4) {

    //只能有两个x,y
    let ps = [p1, p2, p3, p4];
     //求边长相等
    let line = [];
    for(let i = 0; i < 4; i++) {
        for(let j = i + 1; j < 4; j++) {
            let dis = Math.sqrt((ps[i][1] - ps[j][1]) * (ps[i][1] - ps[j][1]) + (ps[i][0] - ps[j][0]) * (ps[i][0] - ps[j][0]));
            line.push(dis);
        }
    }
    //边长只有两种
    line.sort((a,b)=> a - b);
    if(line[0] == 0) {
        return false;
    }
    if(line[0] == line[1] && line[0] == line[2] && line[0] == line[3]
        && line[4] == line[5]) {
        return true;
    }
    return false;
};


p1 = [0, 0], p2 = [1, 1], p3 = [2, 0], p4 = [0, 1]

p1 = [1,0], p2 = [-1,0], p3  = [0,1], p4  = [0,-1]

p1 = [6987,-473],p2 = [6985,-473],p3 = [6986,-472],p4 = [6986,-474]

p1 = [1134,-2539], p2 = [492,-1255], p3 = [-792,-1897], p4 = [-150,-3181]

p1 = [3127,253], p2 = [915,1225], p3 = [1535,-367], p4 = [2507,1845]

p1 = [-10000,10000], p2 = [-10000,-10000], p3 = [10000,10000], p4 = [10000,-10000]

console.log(validSquare(p1, p2, p3, p4));

