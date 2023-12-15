/*
* auther yeling
* 
* 
*/

/**
 * @param {number[]} pref
 * @return {number[]}
 */
var findArray = function(pref) {
    let n = pref.length;
    let res = [];
    for(let i = 0; i < n; i++) {
        if(i == 0) {
            res.push(pref[i])
        } else {
            res.push(pref[i]^pref[i - 1]);            
        }
        
    }
    return res;
};

pref = [5,2,0,3,1]
// pref = [13]
console.log(findArray(pref));
