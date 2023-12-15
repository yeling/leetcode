/*
* auther yeling
* 
* 
*/

/**
 * @param {string[]} event1
 * @param {string[]} event2
 * @return {boolean}
 */
var haveConflict = function(event1, event2) {

    let getTime = (str) => {
        let now = new Date();
        //HH:MM
        let arr = str.split(':');
        now.setHours(arr[0], arr[1]);
        //console.log(now.getTime() + ' '  + now.toLocaleTimeString());
        return Math.floor(now.getTime()/1000/60);
    }

    let begin1 = getTime(event1[0]);
    let end1 = getTime(event1[1]);
    let begin2 = getTime(event2[0]);
    let end2 = getTime(event2[1]);
    //console.log(`${begin1} ${end1} ${begin2} ${end2}`);
    if(begin2 > end1 || begin1 > end2) {
        return false;
    } else {
        return true;
    }

};

event1 = ["10:05","11:00"], event2 = ["01:05","15:00"]
// event1 = ["01:00","02:00"], event2 = ["01:20","03:00"]
console.log(haveConflict(event1, event2));