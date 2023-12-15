/*
* auther yeling
* 6133. 分组的最大数量
* 
*/

var maximumGroups = function(grades) {
    //grades.sort((a,b) => a - b);
    let ret = 0;
    let n = grades.length;
    let sum = 0;
    while(sum <= n) {
        ret++;
        sum += ret;
        //console.log(`sum ${sum} ${ret}`);
    }
    ret--;
    return ret;
};

grades = [10,6,12,7,3,5];
grades = [8,8];
console.log(maximumGroups(grades));
