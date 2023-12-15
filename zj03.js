/*
* auther yeling
* zj-future03. 快递中转站选址
* 
*/

/**
 * @param {number[][]} area
 * @return {number}
 */
//暴力，可以计算中心点来解决
var buildTransferStation = function(area) {
    let station = new Array();
    let m = area.length, n = area[0].length;
    for(let i = 0; i < m; i++) {
        for(let j = 0; j < n; j++) {
            if(area[i][j] == 1) {
                station.push({i,j});
            }
        }
    }

    let minDis = Number.MAX_VALUE;
    for(let i = 0; i < m; i++) {
        for(let j = 0; j < n; j++) {
            let dis = 0;
            for(let k = 0; k < station.length; k++) {
                dis += Math.abs(station[k].i - i) + Math.abs(station[k].j - j);
                if(dis > minDis) {
                    break;
                }
            }
            minDis = Math.min(minDis,dis);
        }
    }
    return minDis;
};


let area = [[0,1,0,0,0],[0,0,0,0,1],[0,0,1,0,0]];
//5
console.log(buildTransferStation(area));