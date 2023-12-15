/*
* auther yeling
* 856. 括号的分数
* 
*/

/**
 * @param {string} s
 * @return {number}
 */
//28 / 86
var scoreOfParentheses = function(s) {
    let stack = new Array();
    let inside = new Array();
    for(let i = 0; i < s.length; i++) {
        let curr = s.charAt(i);
        if(curr == '(') {
            inside.push('*');
            stack.push(curr);
        } else if(curr == ')') {
            if(stack[stack.length - 1] == '(' || !Number.isNaN(stack[stack.length - 1])) {
                let last = stack.pop();
                if(last == '(') {
                    stack.push(1);
                } else {
                    let sum = last;
                    let ll = stack.pop();
                    while(!isNaN(ll)) {
                        sum += ll;
                        ll = stack.pop();
                    }
                    if(isNaN(ll)) {
                        stack.push(2 * sum);
                    } 
                }

            }
        }
        //console.log(stack);
    }
    let sum = 0;
    for(let i = 0; i < stack.length; i++) {
        sum += stack[i];
    }
    return sum;
};

s = "(()(()))"
s = "(()()(()()()))"
s = "()()"

console.log(scoreOfParentheses(s));
