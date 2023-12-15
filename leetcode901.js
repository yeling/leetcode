/*
* auther yeling
* 
* 
*/

var StockSpanner = function() {
    this.nums = new Array();
    this.res = new Array();
};

/** 
 * @param {number} price
 * @return {number}
 */
StockSpanner.prototype.next = function(price) {
    this.nums.push(price);
    let index = this.nums.length - 1;
    let ret = 1;
    index--;
    while(index >= 0) {
        if(this.nums[index] <= price) {
            ret += this.res[index];
            index = index - this.res[index];
        } else {
            break;
        }
    }
    this.res.push(ret);
    return ret;
};

/**
 * Your StockSpanner object will be instantiated and called as such:
 * var obj = new StockSpanner()
 * var param_1 = obj.next(price)
 */

 var obj = new StockSpanner() 
 let nums = [100, 80, 60, 70, 60, 75, 85];
 let res = [];
 for(let i = 0; i < nums.length; i++) {
    res.push(obj.next(nums[i]));
 }
 console.log(res);

 let mine = [27,2,2,2,27];
 console.log(27||2);
