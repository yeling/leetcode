/*
* auther yeling
* 735. 行星碰撞
* 
*/

/**
 * @param {number[]} asteroids
 * @return {number[]}
 */
var asteroidCollision2 = function(asteroids) {
    let stack = new Array();
    let i = 0;
    while(i < asteroids.length) {
        if(stack.length == 0) {
            stack.push(asteroids[i]);
        } else {
            let temp = stack.at(-1);
            if(temp * asteroids[i] > 0 || temp < 0) {
                stack.push(asteroids[i]);
            } else {
                while(stack.length > 0) {
                    if(Math.abs(temp) > Math.abs(asteroids[i])) {
                        break;
                    } else if(Math.abs(temp) == Math.abs(asteroids[i])) {
                        stack.pop();
                        break;
                    } else if(Math.abs(temp) < Math.abs(asteroids[i])) {
                        stack.pop();
                        temp = stack.at(-1);
                        if(temp == null) {
                            stack.push(asteroids[i]);
                            break;
                        }
                    }
                }
            }
        }
        i++;
    }
    return stack;

};

var asteroidCollision = function(asteroids) {
    let stack = new Array();
    let i = 0;
    while(i < asteroids.length) {
        if(stack.length == 0) {
            stack.push(asteroids[i]);
            i++;
        } else {
            let temp = stack.at(-1);
            if(temp < 0 || ( temp > 0 && asteroids[i] > 0)) {
                stack.push(asteroids[i]);
                i++;
            } else {
                if(Math.abs(temp) > Math.abs(asteroids[i])) {
                    i++;
                } else if(Math.abs(temp) == Math.abs(asteroids[i])) {
                    stack.pop();
                    i++;
                } else if(Math.abs(temp) < Math.abs(asteroids[i])) {
                    stack.pop();
                }
            }
        }
    }
    return stack;

};

let asteroids = [10,6,-15];
// asteroids = [-2,-1,1,2];
// asteroids = [-2,-2,1,-2];
console.log(asteroids);
console.log(asteroidCollision(asteroids));