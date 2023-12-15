/*
* auther yeling
* 1656. 设计有序流
* 
*/

/**
 * @param {number} n
 */
var OrderedStream = function(n) {
    this.cache = new Array(n).fill(0);
    this.ptr = 1;
};

/** 
 * @param {number} idKey 
 * @param {string} value
 * @return {string[]}
 */
OrderedStream.prototype.insert = function(idKey, value) {
    this.cache[idKey - 1] = value;
    let res = [];
    if(idKey == this.ptr) {
        while(this.ptr < this.cache.length && this.cache[this.ptr] != 0) {
            res.push(this.cache[this.ptr]);
            this.ptr++;
        }
    }
    return res;
};

/**
 * Your OrderedStream object will be instantiated and called as such:
 * var obj = new OrderedStream(n)
 * var param_1 = obj.insert(idKey,value)
 */
