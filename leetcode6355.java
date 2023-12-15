import java.util.*;

// 注意类名必须为 Main, 不要有任何 package xxx 信息
public class leetcode6355 {
    static boolean find = false;

    public static void main(String[] args) {
        // int [] nums = new int[]{5,14,13,8,12};
        int[] nums = new int[] { 0,1,7,4,4,5 };
        int lower = 3, upper = 6;
        Solution sol = new Solution();
        System.out.println(sol.countFairPairs(nums, lower, upper));

    }

    static class Solution {
        public long countFairPairs(int[] nums, int lower, int upper) {
            
            return 10;
        }
        
    }
}
