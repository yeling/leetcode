/*
* auther yeling
* 2197. 替换数组中的非互质数
* 
*/

/**
 * @param {number[]} nums
 * @return {number[]}
 */
//60 / 71 
//69 / 71 
var replaceNonCoprimes2 = function(nums) {

    var gcd = function (a, b) {
        if (b == 0) {
            return a;
        }
        return gcd(b, a % b);
    }

    let res = [];
    let n = nums.length;
    let curr = null;
    for(let i = 0; i < n; i++) {
        if(curr == null) {
            curr = nums[i];
        } else {
            let common = gcd(curr, nums[i]);
            if(common == 1) {
                //这个值变化之后，往前计算
                for(let j = res.length - 1; j >= 0; j--) {
                    let com2 = gcd(curr, res[j]);
                    if(com2 == 1) {
                        break;
                    } else {
                        curr = (curr/com2) * res[j];
                        res.pop();
                    }
                }
                res.push(curr);
                curr = nums[i];
            } else {
                curr = (curr/common) * nums[i];
            }
        }
        //console.log(curr);
    }    
    res.push(curr);
    return res;
};

//TLE
var replaceNonCoprimes3 = function(nums) {
    var gcd = function (a, b) {
        if (b == 0) {
            return a;
        }
        return gcd(b, a % b);
    }    

    let res = nums;
    let n = nums.length;
    let curr = null;
    let index = 0;    
    while(index <= res.length) {
        if(curr == null) {
            curr = res[index];
            res.splice(index,1);            
        } else {
            if(index == res.length) {
                //最后一位，往前计算                
                for(let j = index - 1; j >= 0; j--) {
                    let com2 = gcd(curr, res[j]);
                    if(com2 == 1) {
                        index = j + 1;                        
                        break;
                    } else {
                        curr = (curr/com2) * res[j];
                        res.splice(j,1);
                        index = j;
                    }
                }                
                res.splice(index,0,curr);
                break;
            } else {
                let common = gcd(curr, res[index]);            
                if(common == 1) {
                    //这个值变化之后，往前计算
                    for(let j = index - 1; j >= 0; j--) {
                        let com2 = gcd(curr, res[j]);
                        if(com2 == 1) {
                            index = j + 1;
                            break;
                        } else {
                            curr = (curr/com2) * res[j];
                            res.splice(j,1);
                            index = j;
                        }
                    }
                    res.splice(index,0,curr);
                    index++;
                    curr = res[index];
                    res.splice(index,1);
                } else {
                    curr = (curr/common) * res[index];
                    res.splice(index,1);               
                }
            }
            
        }
        // console.log(curr);
        // console.log(res);
    }    
    return res;
};

var replaceNonCoprimes = function(nums) {
    
    var gcd = function (a, b) {
        if (b == 0) {
            return a;
        }
        return gcd(b, a % b);
    }

    let res = new Array();
    let n = nums.length;    
    for(let i = 0; i < n; i++) {
        res.push(nums[i]);
        while(res.length > 1) {
            let a = res[res.length - 1];
            let b = res[res.length - 2];
            let com = gcd(a,b);            
            if(com == 1) {
                break;
            } else {
                res.pop();
                res[res.length - 1] = (a/com) * b;
            }
        }
        
    }        
    return res;
};

// nums = [6,4,3,2,7,6,2];
// nums = [2,2,1,1,3,3,3];
nums = [287,41,49,287,899,23,23,20677,5,825]; //[2009,20677,825]
nums = [8303,361,8303,361,437,361,8303,8303,8303,6859,19,19,361,70121,70121,70121,70121,70121,70121,70121,70121,70121,70121,70121,70121,70121,70121,70121,70121,1271,31,961,31,7,2009,7,2009,2009,49,7,7,8897,1519,31,1519,217]
//
nums = [11,9,3,9,3,9,3,9,3,3,3,3,3,33,33,3,3,3,9,3,3,9,3,33,3,33,9,33,33,33,9,3,3,9,3,3,9,3,3,33,33,9,3,33,9,3,33,3,3,33,9,3,9,33,3,3,9,9,33,3,3,3485,85,3485,17,85,5,205,5,1025,85,85,205,205,25,5,425,85,5,425,5,1025,5,205,5,425,17,289]



label = 'replaceNonCoprimes'
console.time(label);
console.log(nums.length);
console.log(replaceNonCoprimes(nums));
console.timeLog(label, 'maxScore2');
// console.log(replaceNonCoprimes(nums));
console.timeEnd(label);
