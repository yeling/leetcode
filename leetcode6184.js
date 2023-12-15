/*
* auther yeling
* 
* 
*/

/**
 * @param {string} arriveAlice
 * @param {string} leaveAlice
 * @param {string} arriveBob
 * @param {string} leaveBob
 * @return {number}
 */
var countDaysTogether = function(arriveAlice, leaveAlice, arriveBob, leaveBob) {
    let monthDay = [0,31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
    let aA = arriveAlice.split('-').map((value) => Number(value));
    let lA = leaveAlice.split('-').map((value) => Number(value));;
    let aB = arriveBob.split('-').map((value) => Number(value));;
    let lB = leaveBob.split('-').map((value) => Number(value));
    
    let comp = (a,b) => {
        if(a[0] < b[0]) {
            return -1;
        } else if(a[0] > b[0]) {
            return 1;
        } else if(a[0] == b[0]) {
            return a[1] - b[1];
        }
    }

    if(comp(aA, lB) > 0 || comp(lA, aB) < 0) {
        return 0;
    }

    let begin = aA;
    let end = lA;
    if(comp(begin, aB) < 0) {
        begin = aB;
    }
    if(comp(end, lB) > 0) {
        end = lB;
    }
    let sum = 0;
    if(begin[0] == end[0]) {
        sum = end[1] - begin[1] + 1;
    } else {
        for(let i = begin[0]; i <= end[0]; i++) {
            if(i == begin[0]) {
                sum += monthDay[i] - begin[1] + 1;
            } else if(i == end[0]) {
                sum += end[1];
            } else {
                sum += monthDay[i];
            }
        }
    }
    return sum;

    

};


arriveAlice = "9-01", leaveAlice = "10-31", arriveBob = "9-01", leaveBob = "12-31"
// arriveAlice = "08-15", leaveAlice = "08-18", arriveBob = "08-16", leaveBob = "08-19"
console.log(countDaysTogether(arriveAlice,leaveAlice, arriveBob, leaveBob));


