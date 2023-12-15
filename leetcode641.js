/*
* auther yeling
* 641. 设计循环双端队列
* 
*/

/**
 * @param {number} k
 */
var MyCircularDeque = function(k) {
    this.cache = new Array();
    this.size = k;
};

/** 
 * @param {number} value
 * @return {boolean}
 */
MyCircularDeque.prototype.insertFront = function(value) {
    if(this.cache.length < this.size) {
        this.cache.splice(0,0,value);
        return true;
    } else {
        return false;
    }
};

/** 
 * @param {number} value
 * @return {boolean}
 */
MyCircularDeque.prototype.insertLast = function(value) {
    if(this.cache.length < this.size) {
        this.cache.push(value);
        return true;
    } else {
        return false;
    }
};

/**
 * @return {boolean}
 */
MyCircularDeque.prototype.deleteFront = function() {
    if(this.cache.length > 0 ) {
        this.cache.splice(0,1);
        return true;
    } else {
        return false;
    }
};

/**
 * @return {boolean}
 */
MyCircularDeque.prototype.deleteLast = function() {
    if(this.cache.length > 0 ) {
        this.cache.pop();
        return true;
    } else {
        return false;
    }
};

/**
 * @return {number}
 */
MyCircularDeque.prototype.getFront = function() {
    if(this.cache.length > 0 ) {
        return this.cache[0];
        
    } else {
        return -1;
    }
};

/**
 * @return {number}
 */
MyCircularDeque.prototype.getRear = function() {
    if(this.cache.length > 0 ) {
        return this.cache[this.cache.length - 1];
    } else {
        return -1;
    }
};

/**
 * @return {boolean}
 */
MyCircularDeque.prototype.isEmpty = function() {
    return this.cache.length == 0;
};

/**
 * @return {boolean}
 */
MyCircularDeque.prototype.isFull = function() {
    return this.cache.length == this.size;
};
