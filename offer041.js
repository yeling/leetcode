/*
* auther yeling
* 剑指 Offer II 041. 滑动窗口的平均值
* 
*/

/**
 * Initialize your data structure here.
 * @param {number} size
 */
var MovingAverage = function (size) {
    this.size = size;
    this.cache = new Array();
    this.sum = 0;
};

/** 
 * @param {number} val
 * @return {number}
 */
MovingAverage.prototype.next = function (val) {
    if (this.cache.length < this.size) {
        this.cache.push(val);
        this.sum += val;
        return this.sum/this.cache.length;
    } else {
        let pre = this.cache.shift();
        this.cache.push(val);
        this.sum = this.sum - pre + val;
        return this.sum/this.cache.length;
    }
};

/**
 * Your MovingAverage object will be instantiated and called as such:
 * var obj = new MovingAverage(size)
 * var param_1 = obj.next(val)
 */

let movingAverage = new MovingAverage(3);
console.log(`${movingAverage.next(1)}`); // 返回 1.0 = 1 / 1
console.log(`${movingAverage.next(10)}`); // 返回 5.5 = (1 + 10) / 2
console.log(`${movingAverage.next(3)}`); // 返回 4.66667 = (1 + 10 + 3) / 3
console.log(`${movingAverage.next(5)}`); // 返回 6.0 = (10 + 3 + 5) / 3
 