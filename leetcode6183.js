/*
* auther yeling
* 
* 
*/

var TreeNode = function(val) {
    this.val = val;
    this.count = 0;
    this.child = new Array();
}

var buildTreeNode = function() {
    let root = new TreeNode();
    return root;
}

var insertNode = function(root,word) {
    let tempHead = root;
    for(let i = 0; i < word.length; i++) {
        let temp = word.charAt(i);
        let find = false;
        for(let j = 0; j < tempHead.child.length; j++) {
            if(tempHead.child.at(j).val == temp) {
                tempHead.child.at(j).count++;
                tempHead = tempHead.child.at(j);
                find = true;
                break;
            }
        }
        if(find == false) {
            let curr = new TreeNode(temp);
            curr.count = 1;
            tempHead.child.push(curr);
            tempHead = curr;
        }

    }
}

var calcTreeNode = function(root,word) {
    let tempHead = root;
    let count = 0;
    for(let i = 0; i < word.length; i++) {
        let temp = word.charAt(i);
        let find = false;
        for(let j = 0; j < tempHead.child.length; j++) {
            if(tempHead.child.at(j).val == temp) {
                count += tempHead.child.at(j).count;
                tempHead = tempHead.child.at(j);
                find = true;
                break;
            } 
        }
        if(find == false) {
            break;
        }
    }
    return count;
}


/**
 * @param {string[]} words
 * @return {number[]}
 */
var sumPrefixScores = function(words) {
    let root = buildTreeNode();
    for(let i = 0; i < words.length; i++) {
        insertNode(root, words[i]);
    }
    let res = new Array(words.length).fill(0);
    for(let i = 0; i < words.length; i++) {
        res[i] = calcTreeNode(root, words[i]);
    }
    return res;
};

words = ["abc","ab","bc","b"];
words = ["abcd"]
console.log(sumPrefixScores(words));
