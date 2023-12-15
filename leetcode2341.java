import java.util.*;

// 注意类名必须为 Main, 不要有任何 package xxx 信息
public class leetcode2341 {
    static boolean find = false;

    public static void main(String[] args) {
        // int [] nums = new int[]{5,14,13,8,12};
        int[] nums = new int[] { 1,3,2,1,3,2,2 };
        Solution sol = new Solution();
        System.out.println(Arrays.toString(sol.numberOfPairs(nums)));

    }

    static class Solution {
        public int[] numberOfPairs(int[] nums) {
            int ans = 0;
            HashMap<Integer,Integer> cache = new HashMap<>();
            for(int v:nums) {
                if(cache.containsKey(v)) {
                    ans++;
                    cache.remove(v);
                } else {
                    cache.put(v, 1);
                }
                
            }
            return new int[]{ans, cache.size()};
        }
    }
}
