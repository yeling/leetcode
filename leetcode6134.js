/*
* auther yeling
* 
* 
*/

/**
 * @param {number[]} edges
 * @param {number} node1
 * @param {number} node2
 * @return {number}
 */
var closestMeetingNode2 = function (edges, node1, node2) {

    let path1 = new Set();
    let path2 = new Set();
    let pathMap1 = new Map();
    let pathMap2 = new Map(); 
    path1.add(node1);
    pathMap1.set(node1,1)
    path2.add(node2);
    pathMap2.set(node2,1);

    let head1 = node1;
    let head2 = node2;
    let size1 = 1;
    let size2 = 1;
    let find1 = false;
    let find2 = false;
    
    let res = [];
    while (true) {
        // console.log(path1)
        // console.log(path2)
        size1 = path1.size;
        size2 = path2.size;
        pathMap1.set(head1,path1.size);
        if (path2.has(head1)) {
            find2 = true;
            res.push(head1);
        }
        if (path1.has(head2)) {
            find1 = true;
            res.push(head2);
        }
        if(find1 && find2 > 0) {
            break;
        }
        if (edges[head1] != -1 && path1.has(edges[head1]) == false && find1 == false) {
            head1 = edges[head1];
            path1.add(head1);
            pathMap1.set(head1,path1.size);
        }
        if (edges[head2] != -1 && path2.has(edges[head2]) == false && find2 == false) {
            head2 = edges[head2];
            path2.add(head2);
            pathMap2.set(head2,path2.size);
        }
        if (size1 == path1.size && size2 == path2.size) {
            break;
        }
    }
    if(res.length == 1) {
        return res[0];
    } else if(res.length == 2) {
        return Math.min(res[0],res[1]);
        // let len1 = pathMap1.get(res[0]) + pathMap2.get(res[0]);
        // let len2 = pathMap1.get(res[1]) + pathMap2.get(res[1]);
        // if(len1 > len2) {
        //     return res[1];
        // } else {
        //     return res[0];
        // }

    }
};

var closestMeetingNode = function (edges, node1, node2) {
    let path1 = new Set();
    let path2 = new Set();
    path1.add(node1);
    path2.add(node2);

    let head1 = node1;
    let head2 = node2;
    let size1 = 1;
    let size2 = 1;
    let res = [];
    while (true) {
        size1 = path1.size;
        size2 = path2.size;
        if (path2.has(head1)) {
            ret = head1;
            res.push(head1);  
        }
        if (path1.has(head2)) {
            ret = head2;
            res.push(head2); 
        }
        if(res.length > 0) {
            break;
        }
        if (edges[head1] != -1 && path1.has(edges[head1]) == false) {
            head1 = edges[head1];
            path1.add(head1); 
        }

        if (edges[head2] != -1 && path2.has(edges[head2]) == false) {
            head2 = edges[head2];
            path2.add(head2);
        }
        if (size1 == path1.size && size2 == path2.size) {
            break;
        }
    }
    if(res.length == 1) {
        return res[0];
    } else if(res.length == 2){
        return Math.min(res[0],res[1]);
    } else {
        return -1;
    }
};

edges = [2,2,3,-1], node1 = 0, node2 = 1
// edges = [1,2,-1],node1 = 0,node2 = 2
edges = [5,-1,3,4,5,6,-1,-1,4,3],node1 = 0, node2 = 0
// edges = [4,4,4,5,1,2,2] ,node1 = 1 ,node2 = 1;
//
edges = [4,4,8,-1,9,8,4,4,1,1],node1 = 5,node2 = 6;

// edges = [4,3,0,5,3,-1], node1 =  4,node2 = 0;

console.log(closestMeetingNode(edges,node1,node2));