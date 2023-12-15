import java.util.*;

// 注意类名必须为 Main, 不要有任何 package xxx 信息
public class leetcode6354 {
    static boolean find = false;

    public static void main(String[] args) {
        // int [] nums = new int[]{5,14,13,8,12};
        int[] nums = new int[] { 7, 52, 2, 4 };
        Solution sol = new Solution();
        System.out.println(sol.findTheArrayConcVal(nums));

    }

    static class Solution {
        public long findTheArrayConcVal(int[] nums) {
            long ans = 0;
            int l = 0, r = nums.length - 1;
            while (l < r) {
                long cur = Long.parseLong(Integer.toString(nums[l]) + Integer.toString(nums[r]));
                ans += cur;
                l++;
                r--;
            }
            if (l == r) {
                ans += nums[r];
            }
            return ans;
        }
    }
}
