/*
* auther yeling
* 
* 
*/

var equalFrequency2 = function(word) {
    let table = new Array(26).fill(0);
    for(let i = 0; i < word.length; i++) {
        table[word.charCodeAt(i) - 97]++;
    }
    let one = 0;
    let two = 0;
    for(let i = 0; i < 26; i++) {
        if(table[i] != 0) {
            if(one == 0 || one == table[i]) {
                one = table[i];
            } else if(two == 0 || two == table[i]) {
                two = table[i];
            } else {
                return false;
            }
        }
    }
    if(one == 1 && two == 0) {
        return true;
    }
    if(one == 2 && word.length == 2) {
        return true;
    }
    if(Math.abs(one - two) == 1) {
        return true;
    }
    return false;
};
//35 / 37 个通过测试用例
//36 / 37 个通过测试用例
var equalFrequency3 = function(word) {
    let table = new Array(26).fill(0);
    for(let i = 0; i < word.length; i++) {
        table[word.charCodeAt(i) - 97]++;
    }
    let cache = new Map();
    for(let i = 0; i < 26; i++) {
        if(table[i] != 0) {
            let v = cache.get(table[i]);
            if(v == null){
                v = 0;
            }
            v++;
            cache.set(table[i],v);
        }
    }   
    console.log(cache);
    if(cache.size > 2) {
        return false;
    }
    if(cache.size == 1) {
        if(cache.get(1) != null) {
            return true;
        } 
        let values = Array.from(cache.values());
        if(values[0] == 1) {
            return true;
        }
        return false;
        
    }
    if(cache.size == 2) {
        let keys = Array.from(cache.keys());
        //console.log(keys);
        if(Math.abs(keys[0] - keys[1]) == 1 
            &&(cache.get(keys[0]) == 1 || cache.get(keys[1]) == 1)) {
            return true;
        }

    }
    return false;
};

var equalFrequency = function(word) {
    let table = new Array(26).fill(0);
    for(let i = 0; i < word.length; i++) {
        table.fill(0);
        for(let j = 0; j < word.length; j++) {
            if(i != j) {
                table[word.charCodeAt(j) - 97]++;
            }
        }
        let cache = new Map();
        for(let i = 0; i < 26; i++) {
            if(table[i] != 0) {
                let v = cache.get(table[i]);
                if(v == null){
                    v = 0;
                }
                v++;
                cache.set(table[i],v);
            }
        }
        if(cache.size == 1) {
            return true;
        }  
    }
    return false;
}

word = "aabbc"
word = "ddaccb"
word = "bbccdddeee"
word = "aaaa"
console.log(equalFrequency3(word));
console.log(equalFrequency(word));