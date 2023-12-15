/*
* auther yeling
* 736. Lisp 语法解析
* 状态机 NOT-AC
*/

/**
 * @param {string} expression
 * @return {number}
 */
var evaluate = function (expression) {
    return dfs(expression, new Array());
};

var dfs = function (expression, vars) {
    let val = 0;
    let currOp = null;
    let index = 0;
    let nextIndex = 0;
    let letState = 0; //0 需要变量， 1 需要表达式，0->1 1->0 如果是0的时候，给了表达式let值 计算let的值
    let currVarMap = null;
    let currVar = ''
    while (index < expression.length) {
        if (expression.charAt(index) == '(') {
            nextIndex = findEndIndex(expression, index);
            console.log(`${index} ${nextIndex}`)
            val = dfs(expression.substring(index + 1, nextIndex), vars);
            index = nextIndex;
        } else {
            let op = expression.substring(index, index + 3);
            if (op == 'let' || op == 'add' || op == 'mul') {
                currOp = op;
                index += 3;
            } else {
                if (currOp != null) {
                    switch (currOp) {
                        case 'let':
                            if (letState == 0) {
                                //需要变量的时候，给了表达式计算结束
                                if (expression.charAt(index) == '(') {
                                    nextIndex = findEndIndex(expression, index);
                                    console.log(`${index} ${nextIndex}`)
                                    let val3 = dfs(expression.substring(index + 1, nextIndex), vars);
                                    //TODO
                                    if(currVar != null) {
                                        currVarMap.push(currVar,val3);
                                        currVar  = null;
                                    } else {
                                        val = val3;
                                    }
                                    currOp = null;
                                    index = nextIndex;
                                } else {
                                    let spaceIndex = expression.indexOf(' ', index + 1);
                                    let varName = expression.substring(index, spaceIndex).trim();
                                    letState = 1;
                                    if (currVarMap == null) {
                                        currVarMap = new Map();
                                        vars.push(currVarMap);
                                    }
                                    currVar = varName;
                                    currVarMap.set(varName, 'unknown');
                                    index = spaceIndex;
                                }
                            } else if(letState == 1) {
                                //需要表达式
                                if (expression.charAt(index) == '(') {
                                    nextIndex = findEndIndex(expression, index);
                                    console.log(`${index} ${nextIndex}`)
                                    let val2 = dfs(expression.substring(index + 1, nextIndex), vars);
                                    currVarMap.set(currVar,val2);
                                    currVar = null;
                                    index = nextIndex;
                                } else {
                                    //let 后面是变量或者数字
                                    let spaceIndex = expression.indexOf(' ', index + 1);
                                    let varName = expression.substring(index, spaceIndex).trim();
                                    if(Number.parseInt(varName) != NaN) {
                                        currVarMap.set(currVar,Number.parseInt(varName));
                                    } else {
                                        currVarMap.set(currVar,currVarMap.get(varName));
                                    }
                                    currVar = null;
                                }
                                letState = 0;
                            }
                            break;
                    }
                }
            }
        }
        index++;
    }
    return val;
};

var findEndIndex = function (expression, index) {
    let stack = new Array();
    while (index < expression.length) {
        if (expression.charAt(index) == '(') {
            stack.push('(');
        } else if (expression.charAt(index) == ')') {
            stack.pop();
        }
        if (stack.length == 0) {
            break;
        }
        index++;
    }
    return index;
}



let expression = "(let x 2 (mult x (let x 3 y 4 (add x y))))";
expression = "(let x 3 x 2 x)";
console.log(evaluate(expression));