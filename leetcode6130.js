/*
* auther yeling
* 双向MAP
* 超时
*/


var NumberContainers = function() {
    this.indexMap = new Map();
    this.numberMap = new Map();
};

/** 
 * @param {number} index 
 * @param {number} number
 * @return {void}
 */
NumberContainers.prototype.change = function(index, number) {
    let preNumber = this.indexMap.get(index);
    if(preNumber == number) {
        return ;
    }
    if(preNumber != null) {
        let prelistSet = this.numberMap.get(preNumber);
        prelistSet.delete(index);
    } 
    this.indexMap.set(index,number);
    let listSet  = this.numberMap.get(number);
    if(listSet == null) {
        listSet = new Set();
        this.numberMap.set(number,listSet);
    }
    listSet.add(index);
};

/** 
 * @param {number} number
 * @return {number}
 */
NumberContainers.prototype.find = function(number) {
    let listSet  = this.numberMap.get(number);
    if(listSet == null || listSet.size == 0) {
        return -1;
    } 
    let minIndex = Number.MAX_VALUE;
    listSet.forEach(value => {
        minIndex = Math.min(minIndex,value);
    });
    return minIndex;
};

/**
 * Your NumberContainers object will be instantiated and called as such:
 * var obj = new NumberContainers()
 * obj.change(index,number)
 * var param_2 = obj.find(number)
 */