/*
* auther yeling
* 488. 祖玛游戏
* 
*/

/**
 * @param {string} board
 * @param {string} hand
 * @return {number}
 */
//暴力回朔 34 / 57 个通过测试用例
//35 / 57 个通过测试用例
//47 / 57 个通过测试用例
//55 / 57 个通过测试用例 超时7s

var findMinStep2 = function (board, hand) {
    //RYBGW
    let balls = ['R', 'Y', 'B', 'G', 'W'];
    let ret = -1;
    let hands = new Array(5).fill(0);
    for (let i = 0; i < hand.length; i++) {
        switch (hand.charAt(i)) {
            case 'R':
                hands[0]++;
                break;
            case 'Y':
                hands[1]++;
                break;
            case 'B':
                hands[2]++;
                break;
            case 'G':
                hands[3]++;
                break;
            case 'W':
                hands[4]++;
                break;
        }
    }

    let combine = function (board) {
        let find = true;
        while (find == true) {
            find = false;
            let sc = 0, curr = board[board.length - 1];
            for (let i = board.length - 1; i >= 0; i--) {
                if (board[i] == curr) {
                    sc++;
                } else {
                    if (sc >= 3) {
                        find = true;
                        board = board.substring(0, i + 1) + board.substring(i + 1 + sc);
                    }
                    sc = 1;
                    curr = board[i];
                }
            }
            if (sc >= 3) {
                find = true;
                board = board.substring(sc);
            }
        }
        return board;
    }

    let count = 0;
    let cache = new Set();
    let cacheMap = new Map();
    let dfs = function (board, hands, preLen) {
        if (ret != -1 && preLen >= ret) {
            return;
        }
        let key = board + hands.join('')
        if (cache.has(key)) {
            return;
        }
        cache.add(key);

        //console.log(key);
        //console.log(`dfs ${count++} ${board} ${hands} ${preLen}`);
        board = combine(board);
        if (board.length == 0) {
            if (ret == -1) {
                ret = preLen;
            } else {
                ret = Math.min(ret, preLen);
            }
            return;
        }
        let leftBall = 0;
        hands.forEach(element => {
            leftBall += element;
        });
        if (leftBall == 0) {
            return;
        }

        //每种球的总数大于3
        let bKinds = new Array(5).fill(0);
        for (let i = 0; i < board.length; i++) {
            switch (board.charAt(i)) {
                case 'R':
                    bKinds[0]++;
                    break;
                case 'Y':
                    bKinds[1]++;
                    break;
                case 'B':
                    bKinds[2]++;
                    break;
                case 'G':
                    bKinds[3]++;
                    break;
                case 'W':
                    bKinds[4]++;
                    break;
            }
        }

        //每种球的总数大于3，不能为1，2
        let needAdd = [];
        for (let i = 0; i < hands.length; i++) {
            if (bKinds[i] + hands[i] < 3 && bKinds[i] > 0) {
                return;
            }
            if (bKinds[i] == 1) {
                needAdd.push(balls[i]);
            }
        }

        let newBoard = '';
        //board里面只有1个这种类型的球，需要加1个进来
        let newHands = hands.slice();
        for (let i = 0; i <= board.length; i++) {
            newBoard += board.charAt(i);
            if (needAdd.length > 0 && board[i] == needAdd[0]) {
                newBoard += board.charAt(i);
                needAdd.length = 0;
                preLen++;
                newHands[balls.indexOf(board.charAt(i))]--;
            }
        }
        board = combine(newBoard);
        if (board.length == 0) {
            if (ret == -1) {
                ret = preLen;
            } else {
                ret = Math.min(ret, preLen);
            }
            return;
        }


        //RYBGW
        for (let j = 0; j < newHands.length; j++) {
            for (let i = 0; i <= board.length; i++) {
                if (j == board[i]) {
                    continue;
                }
                let newBoard = board.substring(0, i);
                if (newHands[j] > 0) {
                    newBoard += balls[j];
                    newHands[j]--;
                    newBoard += board.substring(i);
                    dfs(newBoard, newHands, preLen + 1);
                    //console.log(newBoard);
                    newHands[j]++;
                }
            }
        }
    }

    dfs(board, hands, 0);
    return ret;
};

var findMinStep3 = function (board, hand) {
    //RYBGW
    let ret = -1;
    //let hands = new Array(5).fill(0);
    let hands = {
        'R': 0,
        'Y': 0,
        'B': 0,
        'G': 0,
        'W': 0
    }
    for (let i = 0; i < hand.length; i++) {
        hands[hand.charAt(i)]++;
    }

    let combine = function (board) {
        let find = true;
        while (find == true) {
            find = false;
            let sc = 0, curr = board[board.length - 1];
            for (let i = board.length - 1; i >= 0; i--) {
                if (board[i] == curr) {
                    sc++;
                } else {
                    if (sc >= 3) {
                        find = true;
                        board = board.substring(0, i + 1) + board.substring(i + 1 + sc);
                    }
                    sc = 1;
                    curr = board[i];
                }
            }
            if (sc >= 3) {
                find = true;
                board = board.substring(sc);
            }
        }
        return board;
    }

    let cache = new Set();
    let count = 0;
    let dfs = function (board, hands, preLen) {
        if (ret != -1 && preLen >= ret) {
            return;
        }
        //RYBGW
        let key = board + hands['R'] + hands['Y'] + hands['B'] + hands['G'] + hands['W'];
        if (cache.has(key)) {
            return;
        }
        cache.add(key);

        //console.log(key);
        //console.log(`dfs ${count++} ${board} ${JSON.stringify(hands)} ${preLen}`);
        board = combine(board);
        if (board.length == 0) {
            if (ret == -1) {
                ret = preLen;
            } else {
                ret = Math.min(ret, preLen);
            }
            return;
        }
        let leftBall = 0;
        for (let item in hands) {
            leftBall += hands[item];
        }
        if (leftBall == 0) {
            return;
        }

        //每种球的总数大于3
        let bKinds = {
            'R': 0,
            'Y': 0,
            'B': 0,
            'G': 0,
            'W': 0
        }

        for (let i = 0; i < board.length; i++) {
            bKinds[board.charAt(i)]++;
        }

        //每种球的总数大于3，不能为1，2
        let needAdd = [];
        for (i in hands) {
            if (bKinds[i] + hands[i] < 3 && bKinds[i] > 0) {
                return;
            }
            if (bKinds[i] == 1) {
                needAdd.push(i);
            }
        }
        let newBoard = '';
        //board里面只有1个这种类型的球，需要加1个进来
        //只能加一个进来
        let newHands = {
            'R': hands['R'],
            'Y': hands['Y'],
            'B': hands['B'],
            'G': hands['G'],
            'W': hands['W'],
        }
        for (let i = 0; i <= board.length; i++) {
            newBoard += board.charAt(i);
            if (needAdd.length > 0 && board[i] == needAdd[0]) {
                newBoard += board.charAt(i);
                needAdd.length = 0;
                preLen++;
                newHands[board.charAt(i)]--;
            }
        }
        board = combine(newBoard);
        if (board.length == 0) {
            if (ret == -1) {
                ret = preLen;
            } else {
                ret = Math.min(ret, preLen);
            }
            return;
        }


        //RYBGW
        //增加剪枝条件，如果插入位置和待插入的颜色一致，只在后面插入
        for (let j in newHands) {
            for (let i = 0; i <= board.length; i++) {
                if (j == board[i]) {
                    continue;
                }
                let newBoard = board.substring(0, i);
                if (newHands[j] > 0) {
                    newBoard += j;
                    newHands[j]--;
                    newBoard += board.substring(i);
                    dfs(newBoard, newHands, preLen + 1);
                    //console.log(newBoard);
                    newHands[j]++;
                }
            }
        }
    }

    dfs(board, hands, 0);
    return ret;
};


//改成bfs
var findMinStep = function (board, hand) {
    //RYBGW
    let balls = ['R', 'Y', 'B', 'G', 'W'];
    let ret = -1;
    let hands = new Array(5).fill(0);
    for (let i = 0; i < hand.length; i++) {
        switch (hand.charAt(i)) {
            case 'R':
                hands[0]++;
                break;
            case 'Y':
                hands[1]++;
                break;
            case 'B':
                hands[2]++;
                break;
            case 'G':
                hands[3]++;
                break;
            case 'W':
                hands[4]++;
                break;
        }
    }

    let combine = function (board) {
        let find = true;
        while (find == true) {
            find = false;
            let sc = 0, curr = board[board.length - 1];
            for (let i = board.length - 1; i >= 0; i--) {
                if (board[i] == curr) {
                    sc++;
                } else {
                    if (sc >= 3) {
                        find = true;
                        board = board.substring(0, i + 1) + board.substring(i + 1 + sc);
                    }
                    sc = 1;
                    curr = board[i];
                }
            }
            if (sc >= 3) {
                find = true;
                board = board.substring(sc);
            }
        }
        return board;
    }

    //bfs
    let stack = [];
    

}


board = "RR", hand = "RB"
//140675 4889
// board = "RRGGBBY", hand = "RGBY"
// board = "WRRBBWW", hand = "RBW"
// board = "RBYYBBRRB", hand = "YRBGB"

board = "WWGWGW", hand = "GWBWR"

// board = "RRWWRRBBRR", hand = "WB"
// board = "WWGGWGW", hand = "WBWR"
//7.290s
board = "RRGGBBYYWWRRGGBB", hand = "RGBYW"
// board = "BGBBYRYYRBRWYBRR",hand = "YWYRB"

// board = "YYRGWRBYGGBGBGWY" , hand = "BWGRY"
board = "YYRGWRBYGGBGBGWY",hand = "BWGRY"

// let balls = ['R', 'Y', 'B', 'G', 'W'];

console.time('findMinStep')
console.timeLog('findMinStep')
console.log(findMinStep2(board, hand))
console.timeEnd('findMinStep')
