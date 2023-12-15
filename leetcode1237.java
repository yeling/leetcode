import java.util.*;

// 注意类名必须为 Main, 不要有任何 package xxx 信息
public class leetcode1237 {
    static boolean find = false;

    public static void main(String[] args) {
        // int [] nums = new int[]{5,14,13,8,12};
        int[] nums = new int[] { 7, 52, 2, 4 };
        Solution sol = new Solution();
        System.out.println(sol.findTheArrayConcVal(nums));

    }

    static class Solution {
        public List<List<Integer>> findSolution(CustomFunction customfunction, int z) {
            List<List<Integer>> ans = new ArrayList<>();
            for(int i = 1; i <= 1000; i++) {
                for(int j = 1; j <= 1000; j++) {
                    int temp = customfunction.f(i,j);
                    if(temp == z) {
                        List<Integer> curr = new ArrayList<>();
                        curr.add(i);
                        curr.add(j);
                        ans.add(curr);
                    } else if ( temp > z) {
                        break;
                    }
                }
            }
            return ans;
        }
    }
}
