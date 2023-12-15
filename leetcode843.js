/*
* auther yeling
* 
* 
*/


/**
 * // This is the master's API interface.
 * // You should not implement it, or speculate about its implementation
 * function Master() {
 *
 *     @param {string} word
 *     @return {integer}
 *     this.guess = function(word) {
 *         ...
 *     };
 * };
 */

function Master(secret) {
    this.secret = secret;
    //@param {string} word
    //@return {integer}
    this.guess = function(word) {
        console.log(`guess ${word}`)
        let res = 0;
        for(let i = 0; i < word.length; i++) {
            if(word.charAt(i) == this.secret.charAt(i)) {
                res++;
            }
        }
        return res;
    };
};
/**
 * @param {string[]} words
 * @param {Master} master
 * @return {void}
 */
 var findSecretWord2 = function(words, master) {
    let leftArray = words;
    let count = 0;

    let calc = (src,dst) => {
        let res = 0;
        for(let i = 0; i < src.length; i++) {
            if(src.charAt(i) == dst.charAt(i)) {
                res++;
            }
        }
        return res;
    }

    while(count <= 10) {
        console.log(`count ${count++} ${leftArray}`);
        let cache = new Array(6).fill(0).map(() => new Array(26).fill(0));
        for(let i = 0; i < leftArray.length; i++) {
            for(let j = 0; j < 6; j++) {
                cache[j][leftArray[i].charCodeAt(j) - 97]++;
            }
        }
        // console.log(cache.join('\n'));
        //[index, value]
        let most = new Array(6).fill(0).map(() => new Array(2).fill(0));
        for(let i = 0; i < 6; i++) {
            for(let j = 0; j < 26; j++) {
                if(cache[i][j] > most[i][1]) {
                    most[i][1] = cache[i][j];
                    most[i][0] = j;
                }
            }
        }
        // console.log(most.join(' '));
        let dstWord = most.map((value) => String.fromCharCode(97 + value[0])).join('');
        console.log(dstWord);

        let possible = new Array(leftArray.length).fill(0);
        for(let i = 0; i < leftArray.length; i++) {
            possible[i] = calc(leftArray[i], dstWord);
        }
        // console.log(possible);
        let curr = master.guess(dstWord);
        let nextArray = [];
        for(let i = 0; i < leftArray.length; i++) {
            if(possible[i] == curr) {
                nextArray.push(leftArray[i]);
            }
        }
        if(nextArray.length == 1) {
            let ps1 = master.guess(nextArray[0])
            console.log(`find1 ${nextArray} ${ps1}`);
            break;
        } else if(nextArray.length == 2) {
            let ps1 = master.guess(nextArray[0]);
            if(ps1 != 6) {
                ps1 = master.guess(nextArray[1]);
            }
            console.log(`find2 ${nextArray} ${ps1}`);
            break;
        } 
        leftArray = nextArray;
    }

};

//guess的word，必须在words中
//11 / 12
var findSecretWord = function(words, master) {
    let leftArray = words;
    let count = 0;
    let n = words.length;

    let calc = (src,dst) => {
        let res = 0;
        for(let i = 0; i < src.length; i++) {
            if(src.charAt(i) == dst.charAt(i)) {
                res++;
            }
        }
        return res;
    }

    let dp = new Array(n).fill(0).map(() => new Array(n).fill(0));
    for(let i = 0; i < n; i++) {
        for(let j = 0; j < n; j++) {
            dp[j][i] = dp[i][j] = calc(words[i],words[j]);
        }
    }
    console.log(`${dp.join('\n')}`);

    let used = new Array(n).fill(false);
    while(count <= 20) {
        count++
        //console.log(`count ${count} ${used}`);
        let srcIndex = -1;
        let possible = [];
        for(let i = 0; i < n; i++) {
            if(used[i] == false) {
                possible.push(i);
            }
        } 
        if(possible.length == 1) {
            let curr = master.guess(leftArray[possible[0]]);
            break;
        }
        //选择和最大的
        let max = 0;
        let sump = new Array(possible.length).fill(0);
        for(let i = 0; i < possible.length; i++) {
            for(let j = 0; j < possible.length; j++) {
                if(i != j) {
                    sump[i]+= dp[possible[i]][possible[j]];   
                }
            }
        }
        for(let i = 0; i < possible.length; i++) {
            if(sump[i] >= max) {
                max = sump[i];
                srcIndex = possible[i];
            }
        }
        
        console.log(`${count} srcIndex ${leftArray[srcIndex]} possible ${possible.length}`)
        if(srcIndex == -1) {
            break;
        }
        let curr = master.guess(leftArray[srcIndex]);
        console.log(`guess result ${curr}`);
        if(curr == 6) {
            break;
        }
        for(let i = 0; i < n; i++) {
            if(dp[i][srcIndex] != curr) {
                used[i] = true;
            }
        }
    }

};

secret = "abcczz", wordlist = ["acckzz","ccbazz","eiowzz","abcczz"]

// secret = "ccoyyo"
// wordlist = ["wichbx","oahwep","tpulot","eqznzs","vvmplb","eywinm","dqefpt","kmjmxr","ihkovg","trbzyb","xqulhc","bcsbfw","rwzslk","abpjhw","mpubps","viyzbc","kodlta","ckfzjh","phuepp","rokoro","nxcwmo","awvqlr","uooeon","hhfuzz","sajxgr","oxgaix","fnugyu","lkxwru","mhtrvb","xxonmg","tqxlbr","euxtzg","tjwvad","uslult","rtjosi","hsygda","vyuica","mbnagm","uinqur","pikenp","szgupv","qpxmsw","vunxdn","jahhfn","kmbeok","biywow","yvgwho","hwzodo","loffxk","xavzqd","vwzpfe","uairjw","itufkt","kaklud","jjinfa","kqbttl","zocgux","ucwjig","meesxb","uysfyc","kdfvtw","vizxrv","rpbdjh","wynohw","lhqxvx","kaadty","dxxwut","vjtskm","yrdswc","byzjxm","jeomdc","saevda","himevi","ydltnu","wrrpoc","khuopg","ooxarg","vcvfry","thaawc","bssybb","ccoyyo","ajcwbj","arwfnl","nafmtm","xoaumd","vbejda","kaefne","swcrkh","reeyhj","vmcwaf","chxitv","qkwjna","vklpkp","xfnayl","ktgmfn","xrmzzm","fgtuki","zcffuv","srxuus","pydgmq"]

secret = "hamada"
wordlist = ["hamada","khaled"]
secret = "ccoyyo"
wordlist = ["ccoyyo","wichbx","oahwep","tpulot","eqznzs","vvmplb","eywinm","dqefpt","kmjmxr","ihkovg","trbzyb","xqulhc","bcsbfw","rwzslk","abpjhw","mpubps","viyzbc","kodlta","ckfzjh","phuepp","rokoro","nxcwmo","awvqlr","uooeon","hhfuzz","sajxgr","oxgaix","fnugyu","lkxwru","mhtrvb","xxonmg","tqxlbr","euxtzg","tjwvad","uslult","rtjosi","hsygda","vyuica","mbnagm","uinqur","pikenp","szgupv","qpxmsw","vunxdn","jahhfn","kmbeok","biywow","yvgwho","hwzodo","loffxk","xavzqd","vwzpfe","uairjw","itufkt","kaklud","jjinfa","kqbttl","zocgux","ucwjig","meesxb","uysfyc","kdfvtw","vizxrv","rpbdjh","wynohw","lhqxvx","kaadty","dxxwut","vjtskm","yrdswc","byzjxm","jeomdc","saevda","himevi","ydltnu","wrrpoc","khuopg","ooxarg","vcvfry","thaawc","bssybb","ajcwbj","arwfnl","nafmtm","xoaumd","vbejda","kaefne","swcrkh","reeyhj","vmcwaf","chxitv","qkwjna","vklpkp","xfnayl","ktgmfn","xrmzzm","fgtuki","zcffuv","srxuus","pydgmq"]



console.log(wordlist.length);

findSecretWord(wordlist, new Master(secret));

