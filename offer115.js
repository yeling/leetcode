/*
* auther yeling
* 剑指 Offer II 115. 重建序列
* 图入度的概念
*/
/**
 * @param {number[]} nums
 * @param {number[][]} sequences
 * @return {boolean}
 */

var sequenceReconstruction = function(nums, sequences) {
    let n = nums.length;
    let degree = new Array(n + 1).fill(0);
    let backList = new Array(n + 1).fill(0);
    backList.forEach((value,index) => {
        backList[index] = new Array(); 
    })
    for(let i = 0; i < sequences.length; i++) {
        for(let j = 1; j < sequences[i].length; j++) {
            degree[sequences[i][j]]++;
            backList[sequences[i][j-1]].push(sequences[i][j]);
        }
    }
    //console.log(degree);
    let index = 0
    while(index < nums.length) {
        console.log(`${index} ${degree}`);
        let zeroList = new Array();
        for(let i = index; i <= n; i++) {
            if(degree[nums[i]] == 0) {
                zeroList.push(nums[i]);
            }
        }
        if(zeroList.length > 1 || zeroList[0] != nums[index]) {
            return false;
        }
        let back = backList[nums[index]];
        for(let i = 0; i < back.length; i++) {
            degree[back[i]]--;
        }
        index++;
    }
    return true;
};

nums = [1,2,3], sequences = [[1,2],[1,3]]
console.log(sequenceReconstruction(nums,sequences));
