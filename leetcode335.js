/*
* auther yeling
* 335. 路径交叉
* 
*/
/**
 * @param {number[]} distance
 * @return {boolean}
 */
//模拟数据，超时
//28 / 29 个通过测试用例
var isSelfCrossing = function (distance) {
    let DIRS = [[0, 1], [-1, 0], [0, -1], [1, 0]];
    let x = 0, y = 0;
    let lines = new Array();
    lines.push([{ x: 0, y: 0 }, { x: 0, y: 0 }])
    for (let i = 0; i < distance.length; i++) {
        let dir = DIRS[i % 4];
        let dx = dir[0] * distance[i];
        let dy = dir[1] * distance[i];
        if (dy < 0 || dx < 0) {
            lines.push([{ x: x + dx, y: y + dy }, { x, y }])
        } else {
            lines.push([{ x, y }, { x: x + dx, y: y + dy }])
        }

        x = x + dx;
        y = y + dy;
        // console.log(`${x} ${y}`);
        // console.log('lines');
        // lines.forEach((item) => {
        //     console.log(JSON.stringify(item))
        // })
        let lastLine = lines[lines.length - 1];
        for (let j = lines.length - 4; j >= 0; j -= 2) {
            if (i % 2 == 1) {
                if (lastLine[0].y >= lines[j][0].y
                    && lastLine[0].y <= lines[j][1].y
                    && lines[j][0].x >= lastLine[0].x
                    && lines[j][0].x <= lastLine[1].x) {
                    return true;
                }
            } else {
                if (lastLine[0].x >= lines[j][0].x
                    && lastLine[0].x <= lines[j][1].x
                    && lines[j][0].y >= lastLine[0].y
                    && lines[j][0].y <= lastLine[1].y) {
                    return true;
                }
            }
        }
        //存储线段，线段是否相交
    }
    return false;
};

//数学方法
var isSelfCrossing2 = function (distance) {
    if (distance.length < 4) {
        return false;
    }
    for (let i = 3; i < distance.length; i++) {
        let a = 0, b = 0, c = 0, d = 0;
        if (i > 3) {
            a = distance[i - 4];
        }
        b = distance[i - 3];
        c = distance[i - 2];
        d = distance[i - 1];
        e = distance[i];
        //下面两种情况，区域只能缩小，但是区域方向增大了，则相交
        if (b == d) {
            if (e >= c - a) {
                return true;
            }
        } else if (b > d) {
            if (e >= c) {
                return true;
            } else if (i >= 5 && c > a) {
                let ma = distance[i - 5];
                if (d >= b - ma && e >= c - a) {
                    return true;
                }
            }
        }
    }
    return false;
}

let distance = [2, 1, 1, 2];
// distance = [1, 2, 3, 4];
distance = [1, 2, 3, 4, 4, 4, 8, 9];
distance = [1, 1, 2, 2, 1, 1];
console.log(`1 ${isSelfCrossing(distance)}`);
console.log(`2 ${isSelfCrossing2(distance)}`);