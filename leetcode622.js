/*
* auther yeling
* 622. 设计循环队列
* 
*/

/**
 * @param {number} k
 */
var MyCircularQueue = function(k) {
    this.cache = new Array(k);
    this.head = 0;
    this.tail = 0;
    this.size = 0;

};

/** 
 * @param {number} value
 * @return {boolean}
 */
MyCircularQueue.prototype.enQueue = function(value) {
    if(this.size == this.cache.length) {
        return false;
    }
    this.cache[this.tail] = value;
    this.tail++;
    if(this.tail == this.cache.length) {
        this.tail = 0;
    }
    this.size++;
    return true;
};

/**
 * @return {boolean}
 */
MyCircularQueue.prototype.deQueue = function() {
    if(this.size == 0) {
        return false;
    }
    this.head++;
    if(this.head == this.cache.length) {
        this.head = 0;
    }
    this.size--;
    return true;
};

/**
 * @return {number}
 */
MyCircularQueue.prototype.Front = function() {
    if(this.size == 0) {
        return -1;
    }
    return this.cache[this.head];

};

/**
 * @return {number}
 */
MyCircularQueue.prototype.Rear = function() {
    if(this.size == 0) {
        return -1;
    }
    let pos = this.tail == 0 ? this.cache.length - 1 : this.tail - 1;
    return this.cache[pos];
};

/**
 * @return {boolean}
 */
MyCircularQueue.prototype.isEmpty = function() {
    return this.size == 0;
};

/**
 * @return {boolean}
 */
MyCircularQueue.prototype.isFull = function() {
    return this.size == this.cache.length;
};

k = 2;
var obj = new MyCircularQueue(k)
var param_1 = obj.enQueue(1)
obj.enQueue(2)
// obj.enQueue(3)
obj.deQueue()
obj.enQueue(3)
obj.deQueue()
obj.enQueue(3)
obj.deQueue()
obj.enQueue(3)
obj.deQueue()
var param_3 = obj.Front()

console.log(param_3);

// var param_2 = obj.deQueue()
// var param_3 = obj.Front()
// var param_4 = obj.Rear()
// var param_2 = obj.deQueue()
// var param_5 = obj.isEmpty()
// var param_6 = obj.isFull()
//console.log(`${param_1}  ${param_2} ${param_3} ${param_4} ${param_5} ${param_6}`)
