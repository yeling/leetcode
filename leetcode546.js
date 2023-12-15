/*
* auther yeling
* 546. 移除盒子
* 
*/

/**
 * @param {number[]} boxes
 * @return {number}
 */
// 8 / 63 个通过测试用例 BFS超时
var removeBoxes2 = function(boxes) {
    let stack = new Array();
    stack.push([boxes,0]);
    let cache = new Map();
    let max = boxes.length;
    while(stack.length > 0) {
        let len = stack.length;
        for(let i = 0; i < len; i++) {
            let [temp,sum] = stack.shift();
            let last = null;
            for(let j = 0; j < temp.length; j++) {
                if(last == null) {
                    last = j;
                } else if(temp[last] == temp[j]) {
                    continue;
                } else if(temp[last] != temp[j]) {
                    stack.push([temp.slice(0,last).concat(temp.slice(j)), sum + (j - last) * (j - last)]);
                    max = Math.max(max,sum + (j - last) * (j - last));
                    last = j;
                }
            }
            if(temp.length > 1) {
                stack.push([temp.slice(0,last), sum + (temp.length - last) * (temp.length - last)]);
            }
            max = Math.max(max,sum + (temp.length - last) * (temp.length - last)); 
        }
        //console.log(stack.join('a'));
    }
    return max;
};

//20 / 63 个通过测试用例 没有内存
var removeBoxes3 = function(boxes) {
    let stack = new Array();
    stack.push([boxes,0]);
    let cache = new Map();
    let max = boxes.length;
    while(stack.length > 0) {
        let len = stack.length;
        for(let i = 0; i < len; i++) {
            let [temp,sum] = stack.shift();
            if(cache.has(temp.join('')) && cache.get(temp.join('') > sum)) {
                continue;
            }
            //1个的先消除
            let single = new Map();
            for(let j = 0; j < temp.length; j++) {
                if(single.has(temp[j]) == false) {
                    single.set(temp[j],1);
                } else {
                    single.set(temp[j],single.get(temp[j]) + 1);
                }
            }
            for(let j = temp.length - 1; j >= 0; j--) {
                if(single.get(temp[j]) == 1) {
                    sum++;
                    temp.splice(j,1);
                }
            }
            let last = null;
            for(let j = 0; j < temp.length; j++) {
                if(last == null) {
                    last = j;
                } else if(temp[last] == temp[j]) {
                    continue;
                } else if(temp[last] != temp[j]) {
                    stack.push([temp.slice(0,last).concat(temp.slice(j)), sum + (j - last) * (j - last)]);
                    max = Math.max(max,sum + (j - last) * (j - last));
                    cache.set(temp.slice(0,last).concat(temp.slice(j)).join(''),max);
                    last = j;
                }
            }
            max = Math.max(max,sum + (temp.length - last) * (temp.length - last)); 
            if(temp.length > 1) {
                stack.push([temp.slice(0,last), sum + (temp.length - last) * (temp.length - last)]);
                cache.set(temp.slice(0,last), sum + (temp.length - last) * (temp.length - last),max);
            }
        }
        //console.log(stack.join('a'));
    }
    return max;
};
//DP问题
var removeBoxes = function(boxes) {
    
};

boxes = [1,3,2,2,2,3,4,3,1]
// boxes = [1,2,3,4,5,6,7,8]
//boxes = [1,2,2,1,1,1,2,1,1,2,1,2,1,1,2,2,1,1,2,2,1,1,1,2,2,2,2,1,2,1,1,2,2,1,2,1,2,2,2,2,2,1,2,1,2,2,1,1,1,2,2,1,2,1,2,2,1,2,1,1,1,2,2,2,2,2,1,2,2,2,2,2,1,1,1,1,1,2,2,2,2,2,1,1,1,1,2,2,1,1,1,1,1,1,1,2,1,2,2,1]
// boxes = [1,2,2,1,1,1,2,1,1,2,1,2,1,1,2,2]
// boxes = [1,2,2]
console.time('removeBoxes')
console.log(removeBoxes3(boxes));
console.timeEnd('removeBoxes');

console.time('removeBoxes')
console.log(removeBoxes(boxes));
console.timeEnd('removeBoxes');