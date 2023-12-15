import java.util.*;

// 注意类名必须为 Main, 不要有任何 package xxx 信息
public class leetcode6354 {
    static boolean find = false;

    public static void main(String[] args) {
        // int [] nums = new int[]{5,14,13,8,12};
        int [][] grid = new int[][] {new int[]{1,1,1}
        , new int[]{1,0,1}, new int[]{1,1,1}};
        Solution sol = new Solution();
        System.out.println(sol.largest1BorderedSquare(grid));

    }

    static class Solution {
        public int largest1BorderedSquare(int[][] grid) {
            int n = grid.length;
            int [][] preCol = new int[n][n];
            int [][] preRow = new int[n][n];
            for(int i = 0; i < n; i++) {
                for(int j = 0; j < n; j++) {
                    
                }
            } 
            return 0;
        }
    }   
}
