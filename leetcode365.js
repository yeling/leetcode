/*
* auther yeling
* 
* 
*/
/**
 * @param {number} jug1Capacity
 * @param {number} jug2Capacity
 * @param {number} targetCapacity
 * @return {boolean}
 */
let count = 0;
//12 / 28
//15 / 28 个通过测试用例
//模拟
var canMeasureWater1 = function (jug1Capacity, jug2Capacity, targetCapacity) {
    let dfs = function (jug1, jug2, target, c1, c2, preMap) {
        // if(count++ > 30) {
        //     return false;
        // }
        count++;
        console.log(`${count} c1 ${c1} c2 ${c2}`);
        if (c1 == target || c2 == target || c1 + c2 == target) {
            return true;
        }

        for (let i = 0; i < preMap.length; i++) {
            if (preMap[i].c1 == c1 && preMap[i].c2 == c2) {
                return false;
            }
        }

        let ret = false;
        //jug1加满
        if (c1 < jug1) {
            preMap.push({ c1, c2 });
            ret = dfs(jug1, jug2, target, jug1, c2, preMap);
            preMap.pop();
            if (ret) {
                return ret;
            }
        }
        //jug2加满
        if (c2 < jug2) {
            preMap.push({ c1, c2 });
            ret = dfs(jug1, jug2, target, c1, jug2, preMap);
            preMap.pop();
            if (ret) {
                return ret;
            }
        }

        //jug1清空
        if (c1 > 0) {
            preMap.push({ c1, c2 });
            ret = dfs(jug1, jug2, target, 0, c2, preMap);
            preMap.pop();
            if (ret) {
                return ret;
            }
        }

        //jug2清空
        if (c2 > 0) {
            preMap.push({ c1, c2 });
            ret = dfs(jug1, jug2, target, c1, 0, preMap);
            preMap.pop();
            if (ret) {
                return ret;
            }
        }

        //jug1 -> jug2
        if (c1 > 0 && c2 < jug2) {
            preMap.push({ c1, c2 });
            let tc1 = c1, tc2 = c2;
            if (c1 > jug2 - c2) {
                tc1 = c1 - (jug2 - c2);
                tc2 = jug2;
            } else {
                tc1 = 0;
                tc2 = c1 + c2;
            }
            ret = dfs(jug1, jug2, target, tc1, tc2, preMap);
            preMap.pop();
            if (ret) {
                return ret;
            }
        }
        //jug2 -> jug1
        if (c2 > 0 && c1 < jug1) {
            preMap.push({ c1, c2 });
            let tc1 = c1, tc2 = c2;
            if (c2 > jug1 - c1) {
                tc2 = c2 - (jug1 - c1);
                tc1 = jug1;
            } else {
                tc2 = 0;
                tc1 = c1 + c2;
            }
            ret = dfs(jug1, jug2, target, tc1, tc2, preMap);
            preMap.pop();
            if (ret) {
                return ret;
            }
        }
        return ret;
    }
    return dfs(jug1Capacity, jug2Capacity, targetCapacity, 0, 0, new Array());
};

//12 / 28
//15 / 28 个通过测试用例
//dfs堆栈溢出，可以改成bfs试试
var canMeasureWater3 = function (jug1Capacity, jug2Capacity, targetCapacity) {
    let preMap = new Array();
    let dfs = function (jug1, jug2, target, c1, c2 , op) {
        // if(count++ > 30) {
        //     return false;
        // }
        count++;
        console.log(`${count} c1 ${c1} c2 ${c2}`);
        if (c1 == target || c2 == target || c1 + c2 == target) {
            return true;
        }

        for (let i = 0; i < preMap.length; i++) {
            if (preMap[i].c1 == c1 && preMap[i].c2 == c2) {
                return false;
            }
        }
        preMap.push({ c1, c2 });

        let ret = false;
        //jug1加满
        if (c1 < jug1) {
            ret = dfs(jug1, jug2, target, jug1, c2, 1);
            if (ret) {
                return ret;
            }
        }
        //jug2加满
        if (c2 < jug2) {
            ret = dfs(jug1, jug2, target, c1, jug2, 2);
            if (ret) {
                return ret;
            }
        }

        //jug1清空
        if (c1 > 0 && op != 1 && op != 2) {
            ret = dfs(jug1, jug2, target, 0, c2, 3);
            if (ret) {
                return ret;
            }
        }

        //jug2清空
        if (c2 > 0 && op != 2 && op != 1) {
            ret = dfs(jug1, jug2, target, c1, 0, 4);
            if (ret) {
                return ret;
            }
        }

        //jug1 -> jug2
        if (c1 > 0 && c2 < jug2) {
            let tc1 = c1, tc2 = c2;
            if (c1 > jug2 - c2) {
                tc1 = c1 - (jug2 - c2);
                tc2 = jug2;
            } else {
                tc1 = 0;
                tc2 = c1 + c2;
            }
            ret = dfs(jug1, jug2, target, tc1, tc2, 5);
            if (ret) {
                return ret;
            }
        }
        //jug2 -> jug1
        if (c2 > 0 && c1 < jug1) {
            let tc1 = c1, tc2 = c2;
            if (c2 > jug1 - c1) {
                tc2 = c2 - (jug1 - c1);
                tc1 = jug1;
            } else {
                tc2 = 0;
                tc1 = c1 + c2;
            }
            ret = dfs(jug1, jug2, target, tc1, tc2, 6);
            if (ret) {
                return ret;
            }
        }
        return ret;
    }
    return dfs(jug1Capacity, jug2Capacity, targetCapacity, 0, 0);

};

//25 / 28 ??
//没办法证明，但是结果是对的
var canMeasureWater4 = function (jug1Capacity, jug2Capacity, targetCapacity) {
    if(targetCapacity > jug1Capacity + jug2Capacity) {
        return false;
    }
   
    if(gcd(jug1Capacity,jug2Capacity) != 1) {
        if(gcd(jug1Capacity,targetCapacity) == 1) {
            return false;
        } else {
            return true;
        }
    }
    return true;
};

var canMeasureWater = function (jug1Capacity, jug2Capacity, targetCapacity) {
    if(targetCapacity > jug1Capacity + jug2Capacity) {
        return false;
    }
   
    if(targetCapacity%gcd(jug1Capacity,jug2Capacity) != 0) {
        return false;
    }
    return true;
};

var gcd = function(a,b) {
    if(b == 0) {
        return a;
    }
    return gcd(b,a%b);
}

jug1Capacity = 3, jug2Capacity = 5, targetCapacity = 4;
jug1Capacity = 100, jug2Capacity = 17, targetCapacity = 2;

jug1Capacity = 20, jug2Capacity = 4, targetCapacity = 2;

// jug1Capacity = 22003, jug2Capacity = 31237, targetCapacity = 123;
// console.log(`w3 ${canMeasureWater3(jug1Capacity, jug2Capacity, targetCapacity)}`)

console.log(`${canMeasureWater(jug1Capacity, jug2Capacity, targetCapacity)}`)

// console.log(gcd(2,5));
// console.log(gcd(8,16));