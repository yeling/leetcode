/*
* auther yeling
* 342. 4的幂
* 
*/


var isPowerOfFour = function(n) {
    let max = Math.pow(2,31);
    let curr = 1;
    while(curr < max) {
        console.log(curr);
        curr *= 4;
    }
    //return 1073741824%n == 0;
    return (n > 0) && (1073741824%n == 0);
};
// isPowerOfFour();

var isPowerOfFour = function(n) {
    if(n < 1) {
        return false;
    }
    let temp = n;
    while(temp%4 == 0) {
        temp = temp/4;
    }
    if(temp == 1) {
        return true;
    } else {
        return false;
    }
}
console.log(isPowerOfFour(5));
console.log(isPowerOfFour(1));
console.log(isPowerOfFour(16));
console.log(isPowerOfFour(-128));