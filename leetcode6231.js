/*
* auther yeling
* 
* 
*/

/**
 * @param {number[]} costs
 * @param {number} k
 * @param {number} candidates
 * @return {number}
 */
//62 / 156 个通过测试用例

//132 / 156 个通过测试用例
//TLE
var totalCost2 = function(costs, k, candidates) {
    let n = costs.length;
    let sum = 0;
    let used = new Array(n).fill(false);
    for(let i = 0; i < k; i++) {
        let count = 0;
        let j = n - 1;
        let min = Number.MAX_SAFE_INTEGER;
        let minIndex = Number.MAX_SAFE_INTEGER;
        while(count < candidates && j >= 0) {
            if(used[j] == false) {
                count++;
                if(costs[j] < min) {
                    min = costs[j];
                    minIndex = j;  
                } else if(costs[j] == min) {
                    min = costs[j];
                    if(minIndex > j) {
                        minIndex = j;
                    }
                }
            }
            j--;
        }
        count = 0;
        j = 0;
        while(count < candidates && j < n) {
            if(used[j] == false) {
                count++;
                if(costs[j] < min) {
                    min = costs[j];
                    minIndex = j;  
                } else if(costs[j] == min) {
                    min = costs[j];
                    if(minIndex > j) {
                        minIndex = j;
                    }
                }
            }
            j++;
        }
        sum += min;
        used[minIndex] = true;
        // console.log(sum, min, minIndex)
    }
    return sum;
};

const {
PriorityQueue,
MinPriorityQueue,
MaxPriorityQueue,
} = require('@datastructures-js/priority-queue');
//PASS
var totalCost = function(costs, k, candidates) {
    let n = costs.length;
    let sum = 0;
    let leftStack = new MinPriorityQueue({
        compare: (a, b) => {
            if(a[1] == b[1]) {
                return a[0] - b[0];
            } else {
                return a[1] - b[1];
            }
        }
    })
    let rightStack = new MinPriorityQueue({
        compare: (a, b) => {
            if(a[1] == b[1]) {
                return a[0] - b[0];
            } else {
                return a[1] - b[1];
            }
        }
    })
    let left = 0, right = n - 1;

    for(let i = 0; i < k; i++) {
        while(leftStack.size() < candidates && left <= right) {
            leftStack.enqueue([left, costs[left]]);
            left++;
        }

        while(rightStack.size() < candidates && right >= left) {
            rightStack.enqueue([right, costs[right]]);
            right--;
        }
        
        let lt = leftStack.dequeue();
        let rt = rightStack.dequeue();
        if(lt == null) {
            sum += rt[1];
        } else if(rt == null) {
            sum += lt[1];
        }else if(rt[1] < lt[1]) {
            sum += rt[1];
            leftStack.enqueue(lt);
        } else {
            sum += lt[1];
            rightStack.enqueue(rt);
        }
        //console.log(sum);
    }
    return sum;
};

costs = [17,12,10,2,7,2,11,20,8], k = 3, candidates = 4
costs = [1,2,4,1], k = 3, candidates = 3 //4
// costs = [31,25,72,79,74,65,84,91,18,59,27,9,81,33,17,58]
// costs = [31,25,72,79,74,65,18,91,18,59,27,9,81,33,17,58]
//417 423
// k = 11
// candidates = 2
console.log(totalCost(costs, k , candidates));