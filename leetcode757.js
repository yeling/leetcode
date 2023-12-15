/*
* auther yeling
* 757. 设置交集大小至少为2
* 贪心算法
*/

/**
 * @param {number[][]} intervals
 * @return {number}
 */
//103 / 116
var intersectionSizeTwo = function (intervals) {
    //去除子集问题，如果一个大的集合包含另一一个，将大的集合去除
    let m = intervals.length;
    let need = new Array(m).fill(true);
    for (let i = 0; i < intervals.length; i++) {
        if (need[i] == false) {
            continue;
        }
        for (let j = i + 1; j < intervals.length; j++) {
            //i集合大于j
            if (intervals[i][0] <= intervals[j][0] && intervals[i][1] >= intervals[j][1]) {
                need[i] = false;
                break;
            }
            //
            if (intervals[j][0] <= intervals[i][0] && intervals[j][1] >= intervals[i][1]) {
                need[j] = false;
            }
        }
    }
    console.log(need);
    let iv2 = new Array();
    intervals.forEach((item, index) => {
        if (need[index] == true) {
            iv2.push(item);
        }
    })
    console.log(iv2.join(' '));
    iv2.sort((a, b) => {
        return a[0] - b[0];
    })
    console.log(iv2.join(' '));

    let sum = 0, first = iv2[0][1] - 1, second = iv2[0][1];
    sum += 2;
    for (let i = 1; i < iv2.length; i++) {
        //两个点都不想交
        if(first < iv2[i][0] && second < iv2[i][0]) {
            sum += 2;
            first = iv2[i][1] - 1;
            second = iv2[i][1];
        } else if(first < iv2[i][0] && second >= iv2[i][0]) {
            sum++;
            //只有second相交
            first = second;
            second = iv2[i][1];
        }
        //console.log(`${first} ${second}`)
    }
    return sum;

};

intervals = [[1, 2], [2, 3], [2, 4], [4, 5]]
intervals = [[4,14],[6,17],[7,14],[14,21],[4,7]]
// intervals = [[3, 5], [1, 3], [1, 4], [2, 5]]
console.log(intersectionSizeTwo(intervals));