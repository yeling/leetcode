/*
* auther yeling
* 729. 我的日程安排表 I
* 
*/

var MyCalendar = function () {
    this.allRange = new Array();
};

/** 
 * @param {number} start 
 * @param {number} end
 * @return {boolean}
 */
MyCalendar.prototype.book = function (start, end) {
    for (let i = 0; i < this.allRange.length; i++) {
        let temp = this.allRange[i];
        if (temp.start < end && temp.end > start) {
            return false;
        }
    }
    this.allRange.push({ start, end });
    return true;
};

/**
 * Your MyCalendar object will be instantiated and called as such:
 * var obj = new MyCalendar()
 * var param_1 = obj.book(start,end)
 */
var obj = new MyCalendar();
var param_1 = obj.book(10, 20);
console.log(obj.book(10, 20));
console.log(obj.book(20,25));