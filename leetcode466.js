/*
* auther yeling
* 
* 
*/

/**
 * @param {string} s1
 * @param {number} n1
 * @param {string} s2
 * @param {number} n2
 * @return {number}
 */
//WA
var getMaxRepetitions2 = function(s1, n1, s2, n2) {
    let tables = new Array(26).fill(0);
    for(let i = 0; i < s1.length; i++) {
        tables[s1.charCodeAt(i) - 'a'.charCodeAt(0)] = 1;
    }
    //console.log(tables);
    for(let j = 0; j < s2.length; j++) {
        if(tables[s2.charCodeAt(j) - 'a'.charCodeAt(0)] == 0) {
            return 0;
        }
    }
    let indexArray = new Array(s2.length).fill(-1);
    let maxIndex = 0;
    let sIndex = 0;
    for(let i = 0; i < s2.length; i++) {
        while(sIndex < s1.length) {
            if(s1.charAt(sIndex) == s2.charAt(i)) {
                indexArray[i] = sIndex;
                maxIndex = Math.max(maxIndex,sIndex);
                break;
            }
            sIndex++;
            if(sIndex == s1.length) {
                sIndex = 0;
            }
        }
    }
    console.log(indexArray);




    return 100;
};

//暴力解法 5秒 居然过了
var getMaxRepetitions = function(s1, n1, s2, n2) {
    let i = 0; j = 0,sIndex = 0,s2Index = 0,s2Count = 0;
    let sum = 0;
    while(i < n1) {
        while(s2Index < s2.length && i < n1){
            while(sIndex < s1.length && i < n1) {
                if(s1.charAt(sIndex) == s2.charAt(s2Index)) {
                    sIndex++;
                    s2Index++;
                    if(sIndex == s1.length) {
                        i++;
                        sIndex = 0;
                        //console.log('i++1');
                    }
                    break;
                }
                sIndex++;
                if(sIndex == s1.length) {
                    i++;
                    sIndex = 0;
                    //console.log('i++2');
                }
            }
            
        }
        if(s2Index == s2.length) {
            s2Count++;
            s2Index = 0;
        }
        if(s2Count == n2) {
            sum++;
            s2Count = 0;
        }
    }
    return sum;
}

s1 = "acb", n1 = 4, s2 = "ab", n2 = 2
s1 = "bbaa",n1 = 2, s2 = "b",n2 = 1
console.log(getMaxRepetitions(s1,n1,s2,n2));