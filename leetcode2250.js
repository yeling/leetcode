/*
* auther yeling
* 2250. 统计包含每个点的矩形数目
* 
*/

/**
 * @param {number[][]} rectangles
 * @param {number[][]} points
 * @return {number[]}
 */
//暴力 TLE 46 / 47 个通过测试用例
var countRectangles = function(rectangles, points) {
    let n = rectangles.length;
    let m = points.length;
    let res = [];
    for(let i = 0; i < m; i++) {
        let curr = points[i];
        let count = 0;
        for(let j = 0; j < n; j++) {
            if(curr[0] <= rectangles[j][0] && curr[1] <= rectangles[j][1]) {
                count++;
            }
        }
        res.push(count);
    }
    return res;
};

//只针对x进行二分 TLE
var countRectangles2 = function(rectangles, points) {
    let n = rectangles.length;
    let m = points.length;
    let res = [];
    rectangles.sort((a,b) => {
        if(a[0] == b[0]) {
            return a[1] - b[1];
        } else {
            return a[0] - b[0];
        }
    })
    //console.log(rectangles.join(' '));
    for(let i = 0; i < m; i++) {
        let curr = points[i];        
        let left = 0, right = n - 1;
        while(left <= right) {
            let mid = left + Math.floor((right - left)/2);
            if(curr[0] <= rectangles[mid][0]) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        let count = 0;
        for(let j = left; j < n; j++) {
            if(curr[1] <= rectangles[j][1]) {
                count++;
            }
        }
        //console.log(`left ${left} right ${right}`);
        res.push(count);
    }
    return res;
};
rectangles = [[1,1],[2,2],[3,3]], points = [[1,3],[2,1]];
// rectangles = [[1,2],[2,3],[2,5]], points = [[2,1],[1,4]];

rectangles = [[7,1],[2,6],[1,4],[5,2],[10,3],[2,4],[5,9]]
points = [[10,3],[8,10],[2,3],[5,4],[8,5],[7,10],[6,6],[3,6]]

console.log(rectangles.join(' '))
console.log(points.join(' '))
console.log(countRectangles(rectangles,points));
console.log('countRectangles2');
console.log(countRectangles2(rectangles,points));

