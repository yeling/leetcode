/*
* auther yeling
* 1175. 质数排列
*/

// mod 10^9 + 7

let mod = 1000000007;

var numPrimeArrangements = function(n) {
    let primeCount = 0;
    for(let i = 1; i <= n; i++) {
        if(isPrime(i)) {
            primeCount++;
        }
    }
    console.log(`primeCount ${primeCount}`);
    let otherCount = n -  primeCount;
    let primeSum = 1;
    while(primeCount > 1) {
        primeSum *= primeCount;
        primeCount--;
        primeSum = primeSum%mod;
    }
    while(otherCount > 1) {
        primeSum *= otherCount;
        otherCount--;
        primeSum = primeSum%mod;
    }
    return primeSum;
};

var isPrime = function(n) {
    if(n == 1) {
        return false;
    }
    let max = Math.sqrt(n);
    for(let i = 2; i <= max; i++) {
        // console.log(i)
        if(n%i == 0) {
            return false;
        }
    }
    return true;
}

// console.log(isPrime(11));
let n = 80;
console.log(numPrimeArrangements(n));