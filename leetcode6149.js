/*
* auther yeling
* 
* 
*/

/**
 * @param {number[]} edges
 * @return {number}
 */
var edgeScore = function(edges) {
    let n = edges.length;
    let cache = new Array(n).fill(0);
    for(let i = 0; i < n; i++) {
        cache[edges[i]] += i;
    }
    
    let pair = [];
    for(let i = 0; i < n; i++) {
        pair.push([i,cache[i]]);
    }

    pair.sort((a,b) => {
        if(b[1] == a[1]) {
            return a[0] - b[0]
        } else {
            return b[1] - a[1];
        }
    });
    //console.log(pair.join());
    return pair[0][0];
};

edges = [1,0,0,0,0,7,7,5]
console.log(edgeScore(edges));