import java.util.*;

// 注意类名必须为 Main, 不要有任何 package xxx 信息
public class leetcode6359 {
    static boolean find = false;

    public static void main(String[] args) {
        // int [] nums = new int[]{5,14,13,8,12};
        
        Solution sol = new Solution();
        System.out.println(sol.minMaxDifference(11891));

    }

    static class Solution {
        public int minMaxDifference(int num) {
            StringBuilder big = new StringBuilder(Integer.toString(num));
            char dst = 'a';
            for(int i = 0; i < big.length(); i++) {
                if(dst == 'a' && big.charAt(i) != '9') {
                    dst = big.charAt(i);
                    big.setCharAt(i, '9');
                } else if(big.charAt(i) == dst){
                    big.setCharAt(i, '9');
                }
            }
            StringBuilder small = new StringBuilder(Integer.toString(num));
            dst = 'a';
            for(int i = 0; i < small.length(); i++) {
                if(dst == 'a') {
                    dst = small.charAt(i);
                    small.setCharAt(i, '0');   
                } else if(small.charAt(i) == dst){
                    small.setCharAt(i, '0');
                }
            }
            return Integer.parseInt(big.toString()) - Integer.parseInt(small.toString()); 

        }
    }
}
