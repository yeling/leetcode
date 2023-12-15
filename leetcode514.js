/*
* auther yeling
* 514. 自由之路
* 
*/

/**
 * @param {string} ring
 * @param {string} key
 * @return {number}
 */
var findRotateSteps = function (ring, key) {
    let m = ring.length;
    let n = key.length;
    let pos = new Array(26).fill(0).map(() => new Array());
    let dp = new Array(n).fill(0).map(() => new Array(m).fill(m * n));
    for (let i = 0; i < m; i++) {
        pos[ring.charCodeAt(i) - 'a'.charCodeAt(0)].push(i);
    }
    for (let i = 0; i < n; i++) {
        let keyIndex = key.charCodeAt(i) - 'a'.charCodeAt(0);
        let ps = pos[keyIndex];
        if (i == 0) {
            for (let j = 0; j < ps.length; j++) {
                dp[i][ps[j]] = Math.min(dp[i][ps[j]], ps[j]);
                dp[i][ps[j]] = Math.min(dp[i][ps[j]], m - ps[j]);
                dp[i][ps[j]]++;
            }
        } else {
            let lastps = pos[key.charCodeAt(i - 1) - 'a'.charCodeAt(0)];
            for (let j = 0; j < ps.length; j++) {
                let minStep = m * n;
                for (let k = 0; k < lastps.length; k++) {
                    if (ps[j] >= lastps[k]) {
                        minStep = Math.min(minStep, dp[i - 1][lastps[k]] + ps[j] - lastps[k]);
                        minStep = Math.min(minStep, dp[i - 1][lastps[k]] + m - ps[j] + lastps[k]);
                    } else {
                        minStep = Math.min(minStep, dp[i - 1][lastps[k]] + lastps[k] - ps[j]);
                        minStep = Math.min(minStep, dp[i - 1][lastps[k]] + m - lastps[k] + ps[j]);
                    }
                }
                dp[i][ps[j]] = minStep + 1;
            }
        }
        //console.log(dp[i]);
    }
    //console.log('' + dp);
    let min = m * n;
    let ps = pos[key.charCodeAt(n - 1) - 'a'.charCodeAt(0)];
    for (let j = 0; j < ps.length; j++) {
        min = Math.min(min, dp[n - 1][ps[j]]);
    }
    return min;
};

// ring = "godding", key = "gd"
ring = "godding", key = "godding"
// ring = "god", key = "god"
console.log(findRotateSteps(ring, key));