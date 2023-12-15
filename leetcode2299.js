/*
* auther yeling
* 
* 
*/

/**
 * @param {string} password
 * @return {boolean}
 */
var strongPasswordCheckerII = function(password) {
    if(password.length < 8) {
        return false;
    }
    let small = 0, big = 0, num = 0, special = 0;
    let last = null;
    let str = '!@#$%^&*()-+';

    for(let i = 0; i < password.length; i++) {
        let cur = password.charAt(i);
        if(cur <= 'z' && cur >= 'a') {
            small++;
        }
        if(cur <= 'Z' && cur >= 'A') {
            big++;
        }
        if(cur <= '9' && cur >= '0') {
            num++;
        }
        if(str.indexOf(cur) != -1) {
            special++;
        }
        if(last == null) {
            last = cur;
        } else if(last == cur) {
            return false;
        } else {
            last = cur;
        }
    }
    //console.log(`${small} ${big}`)
    if(small > 0 && big > 0 && num > 0 && special > 0) {
        return true;
    } else {
        return false;
    }
};
password = "IloveLe3tcode!"
password = "Me"
console.log(strongPasswordCheckerII(password))