/*
* auther yeling
* 
* //最终大佬使用了回朔来解决最佳抵消次数
*/

var minTransfers = function (distributions) {
    let station = new Map();
    //station 记录current from减去 to加上
    distributions.forEach(item => {
        let currFrom = station.get(item[0]);
        if (currFrom == null) {
            currFrom = 0;
        }
        station.set(item[0], currFrom - item[2]);
        let currTo = station.get(item[1]);
        if (currTo == null) {
            currTo = 0;
        }
        station.set(item[1], currTo + item[2]);
    });

    //console.log(station);
    //贪心算法，//贪心算法，每次抵消的为0是最佳选择 否则每次将最大正最大，负最大抵消
    //贪心算法 两个数相加为0时最佳选择，否则三个数是最佳选择（3个数字移动两次），
    //33 / 38 个通过测试用例
    //否则（4个数字移动三次）
    let leftArray = new Array();
    station.forEach((value) => {
        if (value != 0) {
            leftArray.push(value);
        }
    })
    if (leftArray.length == 0) {
        return 0;
    }

    let count = 0;
    while (leftArray.length > 0) {
        leftArray.sort((a, b) => {
            return a - b;
        })
        console.log(leftArray);
        let find = false;
        //正负抵消
        let l = 0; r = leftArray.length - 1;
        while (l < r) {
            if (leftArray[l] + leftArray[r] == 0) {
                leftArray[l] = 0;
                leftArray[r] = 0;
                l++;
                r--;
                count++;
            } else if (leftArray[r] > -leftArray[l]) {
                r--;
            } else if (leftArray[r] < -leftArray[l]) {
                l++;
            }
        }

        let left = 0; right = leftArray.length - 1;
        while (left < right && leftArray[left] != 0 && leftArray[right] != 0) {
            leftArray[left] += leftArray[right];
            leftArray[right] = 0;
            count++;
            if (leftArray[left] != 0 || leftArray[right] != 0) {
                break;
            } else {
                left++;
                right--;
            }
        }
        let newArray = new Array();
        leftArray.forEach((item) => {
            if (item != 0) {
                newArray.push(item);
            }
        })
        leftArray = newArray;
    }
    return count;
};

//最终大佬使用了回朔来解决
var minTransfers2 = function (distributions) {
    let station = new Map();
    //station 记录current from减去 to加上
    distributions.forEach(item => {
        let currFrom = station.get(item[0]);
        if (currFrom == null) {
            currFrom = 0;
        }
        station.set(item[0], currFrom - item[2]);
        let currTo = station.get(item[1]);
        if (currTo == null) {
            currTo = 0;
        }
        station.set(item[1], currTo + item[2]);
    });

    //console.log(station);
    //贪心算法，//贪心算法，每次抵消的为0是最佳选择 否则每次将最大正最大，负最大抵消
    //贪心算法 两个数相加为0时最佳选择，否则三个数是最佳选择（3个数字移动两次），
    //33 / 38 个通过测试用例
    //否则（4个数字移动三次）
    let leftArray = new Array();
    station.forEach((value) => {
        if (value != 0) {
            leftArray.push(value);
        }
    })
    if (leftArray.length == 0) {
        return 0;
    }

    let count = 0;
    while (leftArray.length > 0) {
        leftArray.sort((a, b) => {
            return a - b;
        })
        //计算第一个数字最佳几个数能够抵消他
        while(dm < leftArray.length - 1) {

        }

        let newArray = new Array();
        leftArray.forEach((item) => {
            if (item != 0) {
                newArray.push(item);
            }
        })
        leftArray = newArray;
    }
    return count;
};



// let distributions = [[0,1,5],[1,2,10],[2,0,5],[2,1,1]];
//distributions = [[0,1,10],[2,0,5]];
// distributions =  [[2,0,5],[3,4,4]]
// distributions = [[0, 2, 4], [1, 2, 4], [3, 4, 5]]
//4
distributions = [[1,2,3],[1,3,3],[6,4,1],[5,4,4]]
console.log(minTransfers2(distributions));

