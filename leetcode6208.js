/*
* auther yeling
* 
* 
*/

/**
 * @param {string} time
 * @return {number}
 */
var countTime = function(time) {

    let allSum = [];
    for(let i = 0; i < 1440; i++) {
        let temp = '';
        temp+=Math.floor(Math.floor(i/60)/10);
        temp+=Math.floor(i/60)%10;
        temp+=':';
        temp+=Math.floor(Math.floor(i%60)/10);
        temp+=Math.floor(Math.floor(i%60)%10);
        allSum.push(temp);
    }
    //console.log(allSum);

    let res = 0;
    for(let i = 0; i < allSum.length; i++) {
        let find = true;
        for(let j = 0; j < 5; j++) {
            if(time.charAt(j) != '?' && time.charAt(j) != allSum[i].charAt(j)) {
                find = false;
                break;
            }
        }
        if(find) {
            res++;
        }
    }
    return res;
};

time = "?5:00"
time = "0?:0?"
time = "??:??"
console.log(countTime(time));