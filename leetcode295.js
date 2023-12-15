/*
* auther yeling
* 295. 数据流的中位数
* 堆排序
*/

var MedianFinder = function() {
    this.nums = [];
};

/** 
 * @param {number} num
 * @return {void}
 */
MedianFinder.prototype.addNum = function(num) {
    let left = 0, right = this.nums.length - 1;
    let target = num;
    while(left <= right) {
        let mid = left + Math.floor((right - left)/2);
        if(target < this.nums[mid]) {
            right = mid - 1;
        } else if(target >= this.nums[mid]) {
            left = mid + 1;
        }
    }
    this.nums.splice(left,0,num);
};

/**
 * @return {number}
 */
MedianFinder.prototype.findMedian = function() {
    let len = this.nums.length;
    let ret = 0;
    if(len%2 == 0) {
        ret = (this.nums[len/2] + this.nums[len/2 -1])/2;
    } else {
        ret = this.nums[Math.floor(len/2)];
    }
    return ret;
};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * var obj = new MedianFinder()
 * obj.addNum(num)
 * var param_2 = obj.findMedian()
 */

 var obj = new MedianFinder()
 obj.addNum(1)
 obj.addNum(2)
//  obj.addNum(3)
 var param_2 = obj.findMedian()
 console.log(`rest ` + param_2)