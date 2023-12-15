import java.util.*;

import javafx.scene.shape.QuadCurve;

// 注意类名必须为 Main, 不要有任何 package xxx 信息
public class leetcode6356 {
    static boolean find = false;

    public static void main(String[] args) {
        // int [] nums = new int[]{5,14,13,8,12};
        // String s = "101101";
        // int [][] queries = new int[][]{
        //     new int[]{0,5},
        //     new int[]{1,2}
        // };
        String s = "10";
        int [][] queries = new int[][]{
            new int[]{4,4}
        };
        Solution sol = new Solution();
        int [][] ans = sol.substringXorQueries(s, queries);
        for(int i = 0; i < ans.length; i++) {
            System.out.println(Arrays.toString(ans[i]));
        }
        

    }

    static class Solution {
        public int[][] substringXorQueries(String s, int[][] queries) {
            int n = queries.length;
            int [][] ans = new int[n][2];
            //val start pos
            HashMap<String,Integer> cache = new HashMap<>();
            for(int i = 0; i < s.length(); i++) {
                if(s.charAt(i) == '0') {
                    if(cache.get("0") == null) {
                        cache.put("0", i);
                    }
                    continue;
                }
                for(int j = i + 1; j < i + 31 & j <= s.length(); j++) {
                    String sub = s.substring(i, j);
                    if(cache.get(sub) == null) {
                        cache.put(sub, i);
                    }
                }
            }

            for(int i = 0; i < n; i++) {
                int first = queries[i][0];
                int second = queries[i][1];
                int dst = first ^ second;
                String temp = Integer.toBinaryString(dst);
                System.out.println(temp);
                Integer pos = cache.get(temp);
                if(pos == null) {
                    ans[i][0] = -1;
                    ans[i][1] = -1;
                } else {
                    ans[i][0] = pos;
                    ans[i][1] = pos + temp.length() - 1;
                }
            }

            // for(int i = 0; i < n; i++) {
            //     int first = queries[i][0];
            //     int second = queries[i][1];
            //     int dst = first ^ second;
            //     String temp = Integer.toBinaryString(dst);
            //     System.out.println(temp);
            //     int pos = s.indexOf(temp);
            //     if(pos == -1) {
            //         ans[i][0] = -1;
            //         ans[i][1] = -1;
            //     } else {
            //         ans[i][0] = pos;
            //         ans[i][1] = pos + temp.length() - 1;
            //     }
            // }
            return ans;
        }
    }
}
