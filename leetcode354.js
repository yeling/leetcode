/*
* auther yeling
* 354. 俄罗斯套娃信封问题
* 
*/

/**
 * @return {number}
 */
let Point = function (size, index) {
    this.in = new Array();
    this.out = new Array();
    this.index = index;
    this.size = size;
}



//79 / 87 个通过测试用例 不给内存 
var maxEnvelopes2 = function (envelopes) {
    // envelopes.sort((a,b) => {
    //     return (a[0] < b[0] && a[1] < b[1]) ? -1:0;
    // })
    // console.log(envelopes.join(' '));
    let n = envelopes.length;
    let dp = new Array(n);
    for (let i = 0; i < envelopes.length; i++) {
        dp[i] = new Point(envelopes[i], i);
    }
    for (let i = 0; i < envelopes.length; i++) {
        for (let j = i + 1; j < envelopes.length; j++) {
            if (envelopes[i][0] < envelopes[j][0] && envelopes[i][1] < envelopes[j][1]) {
                dp[i].out.push(dp[j]);
                dp[j].in.push(dp[i]);
            } else if (envelopes[i][0] > envelopes[j][0] && envelopes[i][1] > envelopes[j][1]) {
                dp[j].out.push(dp[i]);
                dp[i].in.push(dp[j]);
            }
        }
    }
    let stack = new Array();
    let count = 0;
    while (true) {
        stack.length = 0;
        for (let i = 0; i < envelopes.length; i++) {
            if (dp[i].out != null && dp[i].out.length == 0) {
                stack.push(dp[i]);
            }
        }
        if (stack.length == 0) {
            break;
        }
        count++;
        for (let i = 0; i < stack.length; i++) {
            let temp = stack[i];
            temp.out = null;//为null表示计算过了
            //这个点移除，需要将这个点in数组中对应的out数组中的该点移除
            for (let j = 0; j < temp.in.length; j++) {
                let re = temp.in[j];
                for (let k = 0; k < re.out.length; k++) {
                    if (re.out[k] == temp) {
                        re.out.splice(k, 1);
                        break;
                    }
                }
            }
        }
    }
    return count;
};

//排序之后从最大的开始计算out
//85 / 87 个通过测试用例 超时(n^2)
var maxEnvelopes3 = function (envelopes) {
    envelopes.sort((a, b) => {
        // return (a[0] < b[0] && a[1] < b[1]) ? -1 : 0;
        return a[0] - b[0];
    })
    console.log(envelopes.join(' '));
    let n = envelopes.length;
    let dp = new Array(n);
    dp.fill(1);
    let count = 1;
    let index = envelopes.length - 1;
    while (index >= 0) {
        let temp = envelopes[index];
        for (let i = 0; i < index; i++) {
            if (envelopes[i][0] < temp[0] && envelopes[i][1] < temp[1]) {
                dp[i] = Math.max(dp[i], dp[index] + 1);
                count = Math.max(count, dp[i]);
            }
        }
        index--;
    }
    return count;
};

var maxEnvelopes = function (envelopes) {
    envelopes.sort((a, b) => {
        // return (a[0] < b[0] && a[1] < b[1]) ? -1 : 0;
        return a[0] - b[0];
    })
    console.log(envelopes.join(' '));
    let n = envelopes.length;
    let dp = new Array(n);
    dp.fill(1);
    let count = 1;
    let index = envelopes.length - 1;
    while (index >= 0) {
        let temp = envelopes[index];
        //find next
        for(let i = index - 1; i >= 0; i--) {
            if (envelopes[i][0] < temp[0] &&  envelopes[i][1] < temp[1]) {
                dp[i] = Math.max(dp[i], dp[index] + 1);
                count = Math.max(count, dp[i]);
                //break;
            } 
        }
        // console.log(dp.join(' '));
        index--;
    }
    return count;
};



let envelopes = [[5, 4], [6, 4], [6, 7], [2, 3]];
envelopes = [[4, 5], [4, 6], [6, 7], [2, 3], [1, 1]];
envelopes = [[1, 2], [6, 7], [4, 6], [3, 9], [4, 5]];
envelopes = [[10, 17], [10, 19], [16, 2], [19, 18], [5, 6]];//3
// envelopes = [[10,17],[10,19],[16,2],[19,5],[5,6]];//3
envelopes = [[4,5],[4,6],[6,7],[2,3],[1,1]];
console.log(envelopes.join(' '));
console.log(`${maxEnvelopes(envelopes)}`);