// package newcode;
// package leetcode;
import java.util.Arrays;
import java.util.Scanner;

// 注意类名必须为 Main, 不要有任何 package xxx 信息
public class leetcode1798 {
    static boolean find = false;
    public static void main(String[] args) {
        int [] coins = new int[]{1,1,1,5};
        Solution solution = new Solution();
        System.out.println(solution.getMaximumConsecutive(coins));
    }

    
}

class Solution {
    public int getMaximumConsecutive(int[] coins) {
        Arrays.sort(coins);
        int ans = 0;
        for(int i = 0; i < coins.length; i++) {
            if(ans + 1 >= coins[i]) {
                ans += coins[i];
            }
        }
        return ans + 1;
    }
}