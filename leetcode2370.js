/*
* auther yeling
* 2370. 最长理想子序列
* 
*/

/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var longestIdealString = function (s, k) {
    //father数组初始化
    let n = s.length;
    let father = new Array(n);
    for (let i = 0; i < n; i++) {
        father[i] = i;
    }
    //查找father
    var find = function (father, u) {
        if (father[u] != u) {
            father[u] = find(father, father[u])
        }
        return father[u];
    }

    //合并
    var join = function (father, u, v) {
        let fu = find(father, u);
        let fv = find(father, v);
        if (fu != fv) {
            father[fu] = fv;
        }
    }

    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
            if (Math.abs(s.charCodeAt(i) - s.charCodeAt(j)) <= k) {
                join(father, i, j);
            }
        }
    }

    let max = 0;
    //计算连通节点数目
    let rootMap = new Map();
    for (let i = 0; i < father.length; i++) {
        //这里是节点合并
        let root = find(father, father[i])
        let count = rootMap.get(root);
        if (count == null) {
            count = 0;
        }
        max = Math.max(max, count + 1);
        rootMap.set(root, count + 1);
    }
    return max;
};

//66 / 84 个通过测试用例 超时
var longestIdealString3 = function (s, k) {
    let n = s.length;
    let inList = new Array(n).fill(0).map(() => new Array());
    let outList = new Array(n).fill(0).map(() => new Array());
    let leftList = new Array(n);
    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
            if (Math.abs(s.charCodeAt(i) - s.charCodeAt(j)) <= k) {
                inList[j].push(i);
                leftList.push(i);
                outList[i].push(j);
            }
        }
    }
    let depth = 0;

    while (true) {
        depth++;
        //入度为0的走一步
        let allIn = new Array();
        for (let i = inList.length - 1; i >= 0; i--) {
            if (inList[i].length == 0 && outList[i].length > 0) {
                allIn.push(i)
            }
        }
        if (allIn.length == 0) {
            break;
        }

        for (let i = 0; i < allIn.length; i++) {
            let pos = allIn[i];
            let out = outList[pos];
            for (let j = 0; j < out.length; j++) {
                let inL = inList[out[j]];
                for (let k = inL.length - 1; k >= 0; k--) {
                    if (inL[k] == pos) {
                        inL.splice(k, 1);
                        break;
                    }
                }
            }
            out.length = 0;
        }
    }
    return depth;
}

var longestIdealString2 = function (s, k) {
    let n = s.length;
    let inList = new Array(n).fill(0).map(() => new Array());
    let outList = new Array(n).fill(0).map(() => new Array());
    let leftList = new Array();
    for (let i = 0; i < n; i++) {
        leftList.push(i);
        for (let j = i + 1; j < n; j++) {
            if (Math.abs(s.charCodeAt(i) - s.charCodeAt(j)) <= k) {
                inList[j].push(i);
                outList[i].push(j);
            }
        }
    }
    let depth = 0;

    while (true) {
        //console.log(depth);
        depth++;
        //入度为0的走一步
        let allIn = new Array();
        //console.log(leftList);
        for (let i = leftList.length - 1; i >= 0; i--) {
            if (inList[leftList[i]].length == 0 && outList[leftList[i]].length > 0) {
                allIn.push(leftList[i])
                leftList.splice(i, 1);
            }
        }
        if (allIn.length == 0) {
            break;
        }

        for (let i = 0; i < allIn.length; i++) {
            let pos = allIn[i];
            let out = outList[pos];
            for (let j = 0; j < out.length; j++) {
                let inL = inList[out[j]];
                for (let k = inL.length - 1; k >= 0; k--) {
                    if (inL[k] == pos) {
                        inL.splice(k, 1);
                        break;
                    }
                }
            }
            out.length = 0;
        }
    }
    return depth;
}

//dp问题
//74 / 84 个通过测试用例
var longestIdealString4 = function () {
    let n = s.length;
    let dp = new Array(n).fill(1);
    let max = 1;
    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
            if (Math.abs(s.charCodeAt(i) - s.charCodeAt(j)) <= k) {
                dp[j] = Math.max(dp[j], dp[i] + 1);
                max = Math.max(max, dp[j]);
            }
        }
    }
    return max;
}

var longestIdealString5 = function () {
    let n = s.length;
    let dp = new Array(26).fill(0);
    let max = 1;
    for (let i = 0; i < n; i++) {

        let begin = Math.max(0, s.charCodeAt(i) - 97 - k);
        let end = Math.min(25, s.charCodeAt(i) - 97 + k)
        for (let j = begin; j <= end; j++) {
            dp[s.charCodeAt(i) - 97] = Math.max(dp[s.charCodeAt(i) - 97], dp[j]);
        }
        dp[s.charCodeAt(i) - 97]++;
        max = Math.max(max, dp[s.charCodeAt(i) - 97]);
        //console.log(dp);
    }
    return max;
}

s = "acfgbd", k = 2
s = "pyxygewiecdjmmjtvxriytsotiocfivweyfqnxrzqhqvdielohfyegnmzoepixbkqessuurolwyevmsxjsxoylvuuqjinpiimlbwgyyvryzuueidogvrybycjiymlaxoywtnavrfjbbcixiqxmljcxlxjbkltgtmegbecgzxrzkhpnqvpyottkxmlttllcpdqsgawuhdrrgnywzainiogswveodafsicwoafhndyynyvxyrpbxkkbyuoeynzqtqwqjnmejqsigrezxhmddyznqwjlioumwdkuhszamhtapwlxbjticsosqizoqlashrbbfecmnxbegajoectvybghyuqsigjfcydyaoczxzrbbzxwgnjodbuggthwphzqcvrotaqplafyjvajumutvjumelmhghfhdwmlenzgzkbkmqasujqelmgspqjurwmzgtiycvwxicirhgrupmanxflrwfnjtsnxmrlmcbddzxgtjcaaemghyeousztmgsemfzzumxominqbszjsupgujskihqeiraarentohkmmzzdaomgklujafmjsmaaixphqicqmiranumqmspwrgvjidzhefwrzumbfdznzwdczxtyvsjnhuiowudqzzxgnihwzszzbqnjtcaacnshesegaxnfpqrxnedqqfbmamdxlzzstevvcyqmerfdeobvirtzoxkjrirqdumpshqbzhoghwqfjraneewvgryabofqtjxtmbkeesbfnsrwnutlshjcbsjlnudeynmdqggrbshezbfrckhatfwzocdzzctvpfyzijcdwpunitolyehsegiubhhtvnpsmszuhnyburzkmqrnoudsymdshnykysevbchlxgxejvbggypsqsszwijlxaiktsydlkkevunhlzoqdragyuapsbafzfcurmnkwxwqtwdtssbbpwogukkiongtiikdnpbipqlwasecivekdtfckcddyinwjxrhqmepcguvnejmzsnswubdiawvjihqsavifpnuhylpjhywwgkpvudpyrwxssbbmdqqdellguszukzpitsyuwwtuzuefyjczqwvzqmedygttyahmysbrpgjqvxeoitibfofgqcnqtxregubhrlxpcasrjenjykikgsjllbjyqkmbbkxfdsynsxabujvhndztscanlolakoowufevynmqesoeznceexgxklqdlnuyxzqibxvkixmsebblqkyoazlveptridqavwychhiqpaacakaxhvqgclngcsclxxrhrxxamcueklfiryofgtfihkqoreczlonqkewgpfxoghlesshamrwnhmheqjjjnnnvznyecyhsvsjnvfpnzwacvghbhyvpuopexjvwkgjcbxnubntoktdgogrgbvdimwjemibqwssdddnkmyjiqvyvyjkpaxsurbspnjwijlnspptpbzpjwtsmmszkocpmliqujbwwtrravesqfxqbtoujkfoglmctqbjatjqygrcktrpxlrmzhlcnzoguklskientforrsbzvqeoiqfhbhnzknvyzkqgkwehxgqxpgerwtjhlvognddwwvhcmmijzzitdejlifowuieccbmdvfumqqicpqkdcmjgtzguhhwmbjfmaqwazfippuepchqapziaicyoxvtxjbtjhvekxfqzkboahssmkslkqkygvpvyjofenjxekgajocjtvaomgikcpqjsnwaozmfpuelagvestjxwdonndvlcuntgnakjkwwbisiqfbktdcwfbvwhniioujsgazzwvqqetrdzutqtwcdzolsridklwvirwhchbnfwgcvwazatnxwlitdifysinducobkjoebtwlqajynqruanpexdfalfodoqiwuheuzoceytsogbriiclgxtnbtnwjxltxlmgokjxpavzgj"
k = 13

// console.time('longestIdealString3')
// console.log(longestIdealString3(s,k));
// console.timeEnd('longestIdealString3')

// console.time('longestIdealString2')
// console.log(longestIdealString2(s,k));
// console.timeEnd('longestIdealString2');

console.time('longestIdealString4')
console.log(longestIdealString4(s, k));
console.timeEnd('longestIdealString4');


console.time('longestIdealString5')
console.log(longestIdealString5(s, k));
console.timeEnd('longestIdealString5');
