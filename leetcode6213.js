/*
* auther yeling
* 
* 
*/

/**
 * @param {number} n
 */
var LUPrefix = function(n) {
    this.used = new Array(n + 1).fill(false);
    this.max = 0;
};

/** 
 * @param {number} video
 * @return {void}
 */
LUPrefix.prototype.upload = function(video) {
    this.used[video] = true;
    if(video == this.max + 1) {
        for(let i = video; i < this.used.length; i++) {
            if(this.used[i] == false) {
                break;
            } else {
                this.max = i;
            }
        }
    }
};

/**
 * @return {number}
 */
LUPrefix.prototype.longest = function() {
    return this.max;
};

/**
 * Your LUPrefix object will be instantiated and called as such:
 * var obj = new LUPrefix(n)
 * obj.upload(video)
 * var param_2 = obj.longest()
 */