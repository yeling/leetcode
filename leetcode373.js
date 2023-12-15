/*
* auther yeling
* 
* 
*/
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @param {number} k
 * @return {number[][]}
 */
var kSmallestPairs = function (nums1, nums2, k) {
    let res = [];
    let al = 0, ar = 0, bl = 0, br = 0;
    let DIRS = [[0, 1], [-1, 0], [0, -1], [1, 0]];
    res.push([nums1[0],nums2[0]]);
    while (k > 1 && (ar < nums1.length || br < num2.length)) {
        let min = Number.MAX_VALUE;
        let select = 1;
        if (al < nums1.length - 1 && al < ar &&min > nums1[al + 1] + nums2[br]) {
            min = nums1[al + 1] + nums2[br];
            select = 1;
        }

        if (ar < nums1.length - 1 && min > nums1[ar + 1] + nums2[bl]) {
            min = nums1[ar + 1] + nums2[bl];
            select = 2;
        }

        if (bl < nums2.length - 1 && bl < br &&min > nums1[ar] + nums2[bl + 1]) {
            min = nums1[ar] + nums2[bl + 1];
            select = 3;
        }

        if (br < nums2.length - 1 && min > nums1[al] + nums2[br + 1]) {
            min = nums1[al] + nums2[br + 1];
            select = 4;
        }
        switch (select) {
            case 1:
                res.push([nums1[al + 1], nums2[br]]);
                al++;
                br = bl + 1;
                break;
            case 2:
                res.push([nums1[ar + 1], nums2[bl]]);
                ar++;
                br = bl + 1;
                break;
            case 3:
                res.push([nums1[ar], nums2[bl + 1]]);
                bl++;
                ar = al + 1;
                break;
            case 4:
                res.push([nums1[al], nums2[br + 1]]);
                br++;
                ar = al + 1;
                break;
        }
        k--;
    }
    return res;
};

nums1 = [1, 7, 11], nums2 = [2, 4, 6], k = 10;
console.log(nums1);
console.log(nums2);
console.log(kSmallestPairs(nums1, nums2, k).join(' '));