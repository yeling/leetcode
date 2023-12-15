/*
* auther yeling
* 710. 黑名单中的随机数
* 没有AC
*/
/**
 * @param {number} n
 * @param {number[]} blacklist
 */
var Solution = function(n, blacklist) {
    let nums = new Array(n);
    nums.fill(true);
    for(let i = 0; i < blacklist.length; i++) {
        nums[blacklist[i]] = false;
    }
    this.realNums = []
    //console.log(nums);
    nums.forEach((item,index) => {
        if(item) {
            this.realNums.push(index);
        }
    })



};

/**
 * @return {number}
 */
Solution.prototype.pick = function() {
    let len = this.realNums.length;
    let index = Math.floor(Math.random() * len);
    return this.realNums[index];
};

/**
 * Your Solution object will be instantiated and called as such:
 * var obj = new Solution(n, blacklist)
 * var param_1 = obj.pick()
 */

let n = 7;
let blacklist = [2,3,5];
var obj = new Solution(n, blacklist);
console.log(obj.pick());
console.log(obj.pick());
console.log(obj.pick());
console.log(obj.pick());
