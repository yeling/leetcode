/*
*315. 计算右侧小于当前元素的个数
*输入：nums = [5,2,6,1]
*输出：[2,1,1,0] 
*NAC
*/
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var countSmaller = function(nums) {
    let result = new Array(nums.length);
    result.fill(0);
    for(let i = result.length - 2; i >= 0; i--) {
        for(let j = i + 1; j < result.length; j++) {
            if(nums[j] < nums[i]) {
                result[i]++;
            }
        }
    }
    return result;
};

var countSmaller3 = function(nums) {
    let result = new Array(nums.length);
    result.fill(0);
    for(let i = result.length - 2; i >= 0; i--) {
        for(let j = i + 1; j < result.length; j++) {
            if(nums[j] < nums[i]) {
                result[i]++;
            } else if(nums[j] == nums[i]) {
                result[i] += result[j];
                break;
            }
        }
    }
    return result;
};

var countSmaller2 = function(nums) {
    let result = new Array(nums.length);
    result.fill(0);
    let sortArray = new Array(nums.length);
    for(let i = result.length - 2; i >= 0; i--) {
        for(let j = i + 1; j < result.length; j++) {
            if(nums[j] < nums[i]) {
                result[i]++;
            } else if(nums[j] == nums[i]) {
                result[i] += result[j];
                break;
            }
        }
    }
    return result;
};

var searchInsert = function(nums,target) {
    let left = 0,right = nums.length - 1,insertPos = 0;
    if(target < nums[0]) {
        return 0;
    }
    if(target > nums[nums.length - 1]) {
        return nums.length;
    }
    while (left <= right) {
        let mid = Math.floor(left + (right - left) / 2);
        if (nums[mid] < target) {
            if (nums[mid + 1] > target) {
                insertPos = mid + 1;
                break;
            }
            left = mid + 1;
        } else if (nums[mid] > target) {
            if (nums[mid - 1] < target) {
                insertPos = mid;
                break;
            }
            right = mid - 1;
        } else {
            insertPos = mid;
            while (insertPos > 0 && nums[insertPos] == nums[insertPos - 1]) {
                insertPos--;
            }
            break;
        }
    }
    return insertPos;
}

//找到插入位置
var searchInsert2 = function(nums,target) {
    let left = 0,right = nums.length - 1;
    while(left <= right) {
        let mid = Math.floor(left + (right - left)/2);
        //console.log(`l ${left} r ${right} m ${mid}`)
        if(nums[mid] > target) {
            right = mid - 1;
        } else if(nums[mid] <= target) {
            left = mid + 1;
        }
    }
    return left;
}

let nums = [5,2,6,1];
// nums = [-1,-1];
nums = [7,2,6,1,3];
//console.log(nums)
// let result = countSmaller(nums);
// console.log(result)
// result = countSmaller2(nums);
// console.log(result)
let testN = [1,2,5,8];
let target = 10;
console.log(`${testN} ${target}`)
console.log(searchInsert(testN,target))
console.log('searchInsert2 ' + searchInsert2(testN,target))
