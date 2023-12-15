/*
* auther yeling
* 
* 
*/

/**
 * @param {string} s
 * @param {number[]} distance
 * @return {boolean}
 */
var checkDistances = function(s, distance) {
    let cache = new Map();
    for(let i = 0; i < s.length; i++) {
        let curr = s.charAt(i);
        //console.log(cache);
        if(cache.has(curr) == false) {
            cache.set(curr, i);
        } else {
            let dis = i - cache.get(curr) - 1;
            //console.log(`${dis}`)
            let pos = s.charCodeAt(i) - 'a'.charCodeAt(0);
            if(distance[pos] != dis) {
                return false;
            }
        }
    }
    return true;
};

s = "abaccb";
distance = [1,3,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0];

s = "aa", distance = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

console.log('a'.charCodeAt(0))
console.log(checkDistances(s,distance));