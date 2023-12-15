/*
* auther yeling
* 
* 
*/

/**
 * @param {string} expression
 * @return {boolean}
 */
//69 / 75
var parseBoolExpr = function (expression) {
    //! & | 
    //{'(', ')', '&', '|', '!', 't', 'f', ','} 
    let stack = [];
    for (let i = 0; i < expression.length; i++) {
        let temp = expression.charAt(i);
        if (temp == ')') {
            let sub = [];
            let head = stack.pop();
            while (head == 't' || head == 'f') {
                sub.push(head);
                head = stack.pop();
            }
            let op = stack.pop();
            let res = sub[0] == 't' ? true : false;
            if(op == '!') {
                res = !res;
            } else {
                for (let j = 1; j < sub.length; j++) {
                    let curr = sub[j] == 't' ? true : false;
                    switch (op) {
                        case '&':
                            res &= curr;
                            break;
                        case '|':
                            res |= curr;
                            break;
                    }
                }
            }
            stack.push(res ? 't' : 'f');
        } else if (temp != ',') {
            stack.push(temp);
        }
    }
    return stack.pop() == 't' ? true : false;

};

expression = '|(&(t,f,t),!(t))'
expression = '&(t,t,t)'
console.log(parseBoolExpr(expression));



