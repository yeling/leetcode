/*
* auther yeling
* 快慢指针
* 6135. 图中的最长环
* 
*/

//55 / 72 个通过测试用例
//63 / 72 个通过测试用例
var longestCycle = function(edges) {
    let n = edges.length;
    let vis = new Array(n).fill(false);
    let degree = new Array(n).fill(0);

    for(let i = 0; i < n; i++) {
        degree[edges[i]]++;
    }
    console.log(degree);

    let max = -1;
    for(let i = 0; i < n; i++) {
        //入度为0，开始查找环
        let tempSet = new Set();
        if(vis[i] == false) {
            tempSet.add(i);
            let slow = i;
            let fast = i;
            let findcircle = false;
            while(true) {
                slow = edges[slow];
                if(slow == -1) {
                    break;
                }
                if(vis[slow] == true) {
                    break;
                }
                tempSet.add(slow);
                
                fast = edges[fast];
                if(fast == -1) {
                    break;
                }
                tempSet.add(fast);
                if(vis[fast] == true) {
                    break;
                }

                fast = edges[fast];
                if(fast == -1) {
                    break;
                }
                tempSet.add(fast);
                if(vis[fast] == true) {
                    break;
                }


                if(slow == fast) {
                    findcircle = true;
                    break;
                }
            }

            if(findcircle == true) {
                let finder = i;
                while(finder != slow) {
                    finder = edges[finder];
                    slow = edges[slow];
                }
                console.log(`${finder}`);
            }

            //计算环的长度
            if(findcircle == true) {
                let calc = edges[slow];
                let len = 1;
                while(calc != slow) {
                    len++;
                    calc = edges[calc];
                }
                max = Math.max(max,len);
            }
            tempSet.forEach(item => {
                vis[item] = true;
            });
        }
    } 
    
    return max;
};

edges = [3,3,4,2,3]
edges = [1,2,0,4,5,6,3,8,9,7]
console.log(longestCycle(edges));