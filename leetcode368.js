/*
* auther yeling
* 368. 最大整除子集
* 
*/

/**
 * @param {number[]} nums
 * @return {number[]}
 */
//图论，入度的概率，拓扑排序
var largestDivisibleSubset = function(nums) {
    let n = nums.length;
    let allNum = new Map();
    let father = new Array(n).fill(0).map((value) => { return new Array()});
    let degree = new Array(n).fill(0);
    for(let i = 0; i < n; i++) {
        for(let j = i + 1; j < n; j++) {
            if(nums[j]%nums[i] == 0) {
                degree[j]++;
                father[i].push(j);
            } else if(nums[i]%nums[j] == 0) {
                degree[i]++;
                father[j].push(i);
            }
        }
    }
    //console.log(father);
    //console.log(degree);
    let depth = 0;
    let zeroDegree = new Array();
    let resPath = new Array(n).fill(0).map((value,index) => {
        let ret = new Array();
        ret.push(index);
        return ret;
    });
    while(true) {
        //console.log(degree);
        zeroDegree.length = 0;
        for(let i = degree.length - 1; i >= 0 ; i--) {
            if(degree[i] == 0 && father[i] != null) {
                zeroDegree.push(i);
                //resPath[i].push(i);
            }
        }
        if(zeroDegree.length == 0) {
            break;
        }
        depth++;
        for(let j = 0; j < zeroDegree.length; j++) {
            let temp = father[zeroDegree[j]];
            for(let k = 0; k < temp.length; k++) {
                resPath[temp[k]].length = 0;
                resPath[temp[k]].push(...resPath[zeroDegree[j]]);
                resPath[temp[k]].push(temp[k]);
                degree[temp[k]]--;
            }
            father[zeroDegree[j]] = null;
        }
        //console.log(resPath.join(' '));
    }
    //console.log(`depth ${depth}`);
    for(let i = 0; i < resPath.length; i++) {
        if(resPath[i].length == depth) {
            return resPath[i].map((value) => nums[value]);
        }
    }
    //return depth;
};

nums = [8,4,2,1]
// nums = [3,2,1]
// nums = [4,2,1,6,9,12]
console.log(`largestDivisibleSubset ${largestDivisibleSubset(nums)}`);