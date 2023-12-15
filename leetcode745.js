/*
* auther yeling
* 745. 前缀和后缀搜索
* 字典树 ,JAVA版本的过了，双字典树，后面查找的时候用了双指针
*/


var TreeNode = function(val) {
    this.val = val;
    this.pos = new Array();
    this.child = new Array();
}

var buildTreeNode = function() {
    let root = new TreeNode();
    return root;
}

var insertNode = function(root,word,position) {
    let tempHead = root;
    for(let i = 0; i < word.length; i++) {
        let temp = word.charAt(i);
        let find = false;
        for(let j = 0; j < tempHead.child.length; j++) {
            if(tempHead.child.at(j).val == temp) {
                tempHead = tempHead.child.at(j);
                //tempHead.pos.length = 0;
                tempHead.pos.push(position);
                find = true;
                break;
            } 
        }
        if(find == false) {
            let curr = new TreeNode(temp);
            curr.pos.push(position);
            tempHead.child.push(curr);
            tempHead = curr;
        }
    }
}

var findTreeNode = function(root,pref) {
    let tempHead = root;
    let res = new Array();
    for(let i = 0; i < pref.length; i++) {
        let temp = pref.charAt(i);
        let find = false;
        res.length = 0;
        for(let j = 0; j < tempHead.child.length; j++) {
            if(tempHead.child.at(j).val == temp) {
                res.push(...tempHead.child.at(j).pos);
                tempHead = tempHead.child.at(j);
                find = true;
                break;
            } 
        }
        if(find == false) {
            res.push(-1);
            break;
        }
    }
    return res;
}

/**
 * @param {string[]} words
 */
var WordFilter = function(words) {
    this.preRoot = buildTreeNode();
    this.suffRoot = buildTreeNode();
    words.forEach((item,index) => {
        insertNode(this.preRoot,item,index);
        let reverse = '';
        for(let i =  item.length - 1; i >= 0; i--) {
            reverse += item.charAt(i);
        }
        insertNode(this.suffRoot,reverse,index);
    });
    //console.log(this.root);
};

/** 
 * @param {string} pref 
 * @param {string} suff
 * @return {number}
 */
//4 / 17 个通过测试用例 超时 ，需要构造包含前缀和后缀的树
//12 / 17 个通过测试用例
WordFilter.prototype.f = function(pref, suff) {
    let posPref = findTreeNode(this.preRoot,pref);
    let suffTemp = '';
    for(let i = suff.length - 1; i >= 0; i--) {
        suffTemp += suff.charAt(i);
    }
    let posSuff = findTreeNode(this.suffRoot,suffTemp);
    console.log(`posPref ${posPref} posSuff ${posSuff}`);

    let res = new Array();
    for(let i = 0; i < posPref.length; i++) {
        for(let j = 0; j < posSuff.length; j++) {
            if(posPref[i] == posSuff[j]) {
                res.push(posPref[i]);
            }
        }
    }
    if(res.length == 0) {
        return -1;
    } else {
        return res.pop();
    }
};

/**
 * Your WordFilter object will be instantiated and called as such:
 * var obj = new WordFilter(words)
 * var param_1 = obj.f(pref,suff)
 */

let wordFilter = new WordFilter(["abbba","abba"]);

let pre = "ab";
let suff = "ba";

wordFilter = new WordFilter(["fs","fsxtja"]);
pre = "fs";
suff = "fs";

console.log(wordFilter.f(pre, suff)); // 返回 0 ，因为下标为 0 的单词：前缀 prefix = "a" 且 后缀 suff = "e" 。
