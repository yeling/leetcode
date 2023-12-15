import java.util.*;

// 注意类名必须为 Main, 不要有任何 package xxx 信息
public class leetcode6361 {
    static boolean find = false;

    public static void main(String[] args) {
        int [] nums = new int[]{1,4,3};
        // int[] nums = new int[] { 1,4,7,8,5 };
        // int[] nums = new int[] { 59,27,9,81,33};
        // int[] nums = new int[] { 21,13,21,72,35,52,74};
        Solution sol = new Solution();
        System.out.println(sol.minimizeSum(nums));

    }

    static class Solution {
        //62 / 69 个通过测试用例
        public int minimizeSum(int[] nums) {
            Arrays.sort(nums);
            int n = nums.length;
            int ans = nums[n - 1] - nums[2];
            ans = Math.min(ans, nums[n - 2] - nums[1]);
            ans = Math.min(ans, nums[n - 3] - nums[0]);
            return ans;
        }
        public int minimizeSum2(int[] nums) {
            Arrays.sort(nums);
            int l = 0, r = nums.length - 1;
            if(nums[r] - nums[l+1] > nums[r - 1] - nums[l]) {
                r--;
            } else {
                l++;
            }
            if(nums[r] - nums[l+1] > nums[r - 1] - nums[l]) {
                r--;
            } else {
                l++;
            }
            return nums[r] - nums[l];
        }
    }
}
