/*
* auther yeling
* 
* 
*/


/**
 * @param {string} expression
 * @return {string}
 */
var fractionAddition = function (expression) {
    // a/b + c/d
    let calc = function (a, b, c, d, isAdd) {
        console.log(`calc ${a} ${b} ${c} ${d} ${isAdd}`)
        a = Number.parseInt(a);
        b = Number.parseInt(b);
        c = Number.parseInt(c);
        d = Number.parseInt(d);
        let e, f;
        f = b * d;

        e = a * d;
        if (isAdd) {
            e += b * c;
        } else {
            e -= b * c;
        }
        let g = gcd(e, f);
        if (g != 1) {
            e = e / g;
            f = f / g;
        }
        let sign = '';
        if (e < 0 || f < 0) {
            sign = '-';
        }
        return [sign + Math.abs(e), Math.abs(f).toString()];
    }
    // console.log(calc(-1, 2, 1, 2, true));

    let a = '', b = '', c = '', d = '', isAdd;
    let state = 1;// 1 a 2 b 3 c 4 d
    let result = [];
    for (let i = 0; i < expression.length; i++) {
        switch (expression.charAt(i)) {
            case '/':
                if (state == 1) {
                    state = 2;
                } else if (state == 3) {
                    state = 4;
                }
                break;
            case '+':
                if (state == 2) {
                    isAdd = true;
                    state = 3;
                } else if (state == 4) {
                    result = calc(a, b, c, d, isAdd);
                    a = result[0];
                    b = result[1];
                    c = '';
                    d = '';
                    state = 3;
                    isAdd = true;
                }
                break;
            case '-':
                if (state == 1) {
                    a += expression.charAt(i);
                } else if (state == 2) {
                    state = 3;
                    isAdd = false;
                } else if (state == 3) {
                    c += expression.charAt(i);
                } else if (state == 4) {
                    result = calc(a, b, c, d, isAdd);
                    a = result[0];
                    b = result[1];
                    c = '';
                    d = '';
                    state = 3;
                    isAdd = false;
                }
                break;
            default:
                if (state == 1) {
                    a += expression.charAt(i);
                } else if (state == 2) {
                    b += expression.charAt(i);
                } else if (state == 3) {
                    c += expression.charAt(i);
                } else if (state == 4) {
                    d += expression.charAt(i);
                }
                break;
        }
    }
    if (c.length == 0 || d.length == 0) {
        result = [a, b];
    } else {
        result = calc(a, b, c, d, isAdd);
    }
    //console.log(result);
    return result[0] + "/" + result[1];

};

var gcd = function (a, b) {
    if (b == 0) {
        return a;
    }
    return gcd(b, a % b);
}

expression = "-1/2+1/2-1/3"
expression = "-4/7-3/4+2/3"
expression = "-7/3"
console.log(fractionAddition(expression));

