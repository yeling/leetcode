/*
* auther yeling
* 
* 
*/

/**
 * @param {number} n
 * @param {number[][]} queries
 * @return {number[]}
 */
var productQueries2 = function (n, queries) {
    let MOD = 10 ** 9 + 7;
    let res = [];

    let cur = 1;
    let powers = new Array();
    while (n > 0) {
        if (n % 2 == 1) {
            powers.push(cur);
        }
        n = Math.floor(n / 2);
        cur *= 2;
    }
    //console.log(powers);


    for (let i = 0; i < queries.length; i++) {
        let left = queries[i][0];
        let right = queries[i][1];
        let curr = powers[left];
        for(let j = left + 1; j <= right; j++) {
            curr = (curr * powers[j])%MOD;
        }
        res.push(curr);
    }
    return res;
};


var productQueries = function (n, queries) {
    let MOD = 10 ** 9 + 7;
    let res = [];

    let cur = 1;
    let powers = new Array();
    while (n > 0) {
        if (n % 2 == 1) {
            powers.push(cur);
        }
        n = Math.floor(n / 2);
        cur *= 2;
    }
    //console.log(powers);

    for (let i = 0; i < queries.length; i++) {
        let left = queries[i][0];
        let right = queries[i][1];
        let curr = powers[left];
        for(let j = left + 1; j <= right; j++) {
            curr = (curr * powers[j])%MOD;
        }
        res.push(curr);
    }
    return res;
};

n = 15, queries = [[0, 1], [2, 2], [0, 3]]
console.log(productQueries(n, queries));