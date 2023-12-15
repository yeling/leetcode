/*
* auther yeling
* 640. 求解方程
* 状态机
* 
*/

/**
 * @param {string} equation
 * @return {string}
 */
//54 / 59
var solveEquation = function (equation) {
    const NO = 'No solution';
    const INFINITE = 'Infinite solutions';
    //x 在左边，y 在右边
    let part = equation.split('=');
    if (part.length != 2) {
        return NO;
    }
    //console.log(part);
    let last = '';
    let lnum = 0;
    let lx = 0;
    let isadd = true;
    for (let i = 0; i < part[0].length; i++) {
        switch (part[0].charAt(i)) {
            case '+':
                if(isadd) {
                    lnum += Number(last);
                } else {
                    lnum -= Number(last);
                }
                isadd = true;
                last = '';
                break;
            case '-':
                if(isadd) {
                    lnum += Number(last);
                } else {
                    lnum -= Number(last);
                }
                isadd = false;
                last = '';
                break;
            case 'x':
                let delta = 1;
                if(last.length > 0) {
                    delta = Number(last);
                } 
                if(isadd) {
                    lx += delta;
                } else {
                    lx -= delta;
                }
                last = '';
                break;
            default:
                last += part[0].charAt(i);
                if(i == part[0].length - 1) {
                    if(isadd) {
                        lnum += Number(last);
                    } else {
                        lnum -= Number(last);
                    }
                    last = ''
                }
                
        }
        console.log(`${lx} ${lnum}`);
    }

    if(part[1].startsWith('-')) {
        isadd = false;
    } else {
        isadd = true;
    }
    
    for (let i = 0; i < part[1].length; i++) {
        switch (part[1].charAt(i)) {
            case '+':
                if(isadd) {
                    lnum -= Number(last);
                } else {
                    lnum += Number(last);
                }
                isadd = true;
                last = '';
                break;
            case '-':
                if(isadd) {
                    lnum -= Number(last);
                } else {
                    lnum += Number(last);
                }
                isadd = false;
                last = '';
                break;
            case 'x':
                let delta = 1;
                if(last.length > 0) {
                    delta = Number(last);
                } 
                if(isadd) {
                    lx -= delta;
                } else {
                    lx += delta;
                }
                last = '';
                break;
            default:
                last += part[1].charAt(i);
                if(i == part[1].length - 1) {
                    if(isadd) {
                        lnum -= Number(last);
                    } else {
                        lnum += Number(last);
                    }
                    last = ''
                }
                
        }
        //console.log(`${lx} ${lnum}`);
    }
    if(lx == 0) {
        if(lnum == 0) {
            return INFINITE;
        } else {
            return NO;
        }
    } else {
        return 'x=' + (0 - lnum/lx);
    }
};
equation = "x+5-3+x=6+x-2"
// equation = 'x=x'
// equation = '2x=x'
// equation = "2=-x"
console.log(solveEquation(equation));
