import java.util.*;

// 注意类名必须为 Main, 不要有任何 package xxx 信息
public class leetcode6360 {
    static boolean find = false;

    public static void main(String[] args) {
        // int [] nums = new int[]{5,14,13,8,12};
        int[] nums = new int[] { 1,2,3,4,7,8};
        Solution sol = new Solution();
        System.out.println(sol.minImpossibleOR(nums));

    }

    static class Solution {
        public int minImpossibleOR(int[] nums) {
            Arrays.sort(nums);
            int check = 1;
            for(int i = 0; i < nums.length; i++) {
                if(nums[i] == check) {
                    check = check << 1;
                } else if(nums[i] > check) {
                    break;
                }
            }
            return check;
        }
    }
}
