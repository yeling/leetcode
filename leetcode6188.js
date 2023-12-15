/*
* auther yeling
* 
* 
*/


/**
 * @param {string[]} names
 * @param {number[]} heights
 * @return {string[]}
 */
var sortPeople = function(names, heights) {
    let pair = names.map((value, index) => [value, heights[index]]);
    console.log(pair.join(' '));

    pair.sort((a,b) => b[1] - a[1]);

    console.log(pair.join(' '));

    let res = pair.map((value) => value[0]);
    return res;
};

names = ["Alice","Bob","Bob"], heights = [155,185,150]
names = ["Mary","John","Emma"]
heights = [180,165,170]
console.log(sortPeople(names, heights));

