/*
* auther yeling
* 871. 最低加油次数
* 贪心算法，在油耗尽前，选择最好的
*/

/**
 * @param {number} target
 * @param {number} startFuel
 * @param {number[][]} stations
 * @return {number}
 */
var minRefuelStops1 = function (target, startFuel, stations) {
    let stop = -1;
    let maxPos = startFuel;
    let index = 0;
    if (maxPos >= target) {
        return 0;
    }
    while (maxPos < target && index < stations.length) {
        let nextPos = maxPos;
        //console.log(`index ${index} nextPos ${nextPos}`);
        if (stations[index][0] <= maxPos) {
            while (index < stations.length && stations[index][0] <= maxPos) {
                let tempPos = maxPos + stations[index][1];
                nextPos = Math.max(nextPos, tempPos);
                console.log(`index ${index} nextPos ${nextPos}`);
                index++;
            }
            if (stop == -1) {
                stop = 1;
            } else {
                stop++;
            }
            maxPos = nextPos;
        } else {
            break;
        }
    }
    if (maxPos < target) {
        return -1;
    } else {
        return stop;
    }
};

var minRefuelStops = function (target, startFuel, stations) {
    minStop = -1;
    dfs(target, stations, startFuel, 0 ,0);
    return minStop;
}

//120 / 198 个通过测试用例
let minStop = 0;
let cache = new Map();
let dfsCount = 0;
var dfs = function (target, stations, maxPos, index, stop) {
    dfsCount++;
    console.log(`${dfsCount} dfs maxPos ${maxPos} stop ${stop} index ${index}`);
    // let cacheStep = cache.get(index)
    // if(cacheStep != null && cacheStep < stop) {
    //     return cacheStep;
    // }
    if(minStop != -1 && stop > minStop) {
        return;
    }
    if(maxPos >= target) {
        if(minStop == -1) {
            minStop = stop;
        } else {
            minStop = Math.min(minStop,stop);
        }
    }
    if(index == stations.length) {
        return ;
    }
    if (maxPos < stations[index][0]) {
        return;
    }
    
    dfs(target, stations, maxPos, index + 1,stop);
    dfs(target, stations, maxPos + stations[index][1], index + 1, stop + 1); 
    cache.set(index,minStop);
}

//114 / 198 个通过测试用例
var dfs2 = function (target, stations, maxPos, index, stop) {
    //console.log(`dfs maxPos ${maxPos} stop ${stop} index ${index}`);
    
    if(maxPos >= target) {
        return stop;
    }
    if(index == stations.length) {
        return -1;
    }
    if (maxPos < stations[index][0]) {
        return -1;
    }

    let ret1 = dfs2(target, stations, maxPos, index + 1,stop);
    let ret2 = dfs2(target, stations, maxPos + stations[index][1], index + 1, stop + 1); 
    //console.log(`ret1 ${ret1} ret2 ${ret2}`)
    if(ret1 == -1) {
        return ret2;
    }
    if(ret2 == -1) {
        return ret1;
    }
    return Math.min(ret1,ret2);
}

let target = 100, startFuel = 10, stations = [[10, 60], [20, 30], [30, 30], [60, 40]];
// target = 100
// startFuel = 50
// stations = [[25,30]]

// target = 1000
// startFuel = 10
//stations = [[7,217],[10,211],[17,146],[21,232],[25,310],[48,175],[53,23],[63,158],[71,292],[96,85],[100,302],[102,295],[116,110],[122,46],[131,20],[132,19],[141,13],[163,85],[169,263],[179,233],[191,169],[215,163],[224,231],[228,282],[256,115],[259,3],[266,245],[283,331],[299,21],[310,224],[315,188],[328,147],[345,74],[350,49],[379,79],[387,276],[391,92],[405,174],[428,307],[446,205],[448,226],[452,275],[475,325],[492,310],[496,94],[499,313],[500,315],[511,137],[515,180],[519,6],[533,206],[536,262],[553,326],[561,103],[564,115],[582,161],[593,236],[599,216],[611,141],[625,137],[626,231],[628,66],[646,197],[665,103],[668,8],[691,329],[699,246],[703,94],[724,277],[729,75],[735,23],[740,228],[761,73],[770,120],[773,82],[774,297],[780,184],[791,239],[801,85],[805,156],[837,157],[844,259],[849,2],[860,115],[874,311],[877,172],[881,109],[888,321],[894,302],[899,321],[908,76],[916,241],[924,301],[933,56],[960,29],[979,319],[983,325],[988,190],[995,299],[996,97]]
target = 1000
startFuel = 36
stations = [[7,13],[10,11],[12,31],[22,14],[32,26],[38,16],[50,8],[54,13],[75,4],[85,2],[88,35],[90,9],[96,35],[103,16],[115,33],[121,6],[123,1],[138,2],[139,34],[145,30],[149,14],[160,21],[167,14],[188,7],[196,27],[248,4],[256,35],[262,16],[264,12],[283,23],[297,15],[307,25],[311,35],[316,6],[345,30],[348,2],[354,21],[360,10],[362,28],[363,29],[367,7],[370,13],[402,6],[410,32],[447,20],[453,13],[454,27],[468,1],[470,8],[471,11],[474,34],[486,13],[490,16],[495,10],[527,9],[533,14],[553,36],[554,23],[605,5],[630,17],[635,30],[640,31],[646,9],[647,12],[659,5],[664,34],[667,35],[676,6],[690,19],[709,10],[721,28],[734,2],[742,6],[772,22],[777,32],[778,36],[794,7],[812,24],[813,33],[815,14],[816,21],[824,17],[826,3],[838,14],[840,8],[853,29],[863,18],[867,1],[881,27],[886,27],[894,26],[917,3],[953,6],[956,3],[957,28],[962,33],[967,35],[972,34],[984,8],[987,12]]

console.log(minRefuelStops(target, startFuel, stations));