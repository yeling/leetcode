import java.util.*;

// 注意类名必须为 Main, 不要有任何 package xxx 信息
public class leetcode1234 {
    static boolean find = false;

    public static void main(String[] args) {
        // int [] nums = new int[]{5,14,13,8,12};
        String s = "QWER";
        Solution sol = new Solution();
        System.out.println(sol.balancedString(s));

    }

    static class Solution {
        //都小于1/4时为True
        public boolean check(int [] preCnt, int dst) {
            char [] cnt = new char[]{'Q','W','E','R'};
            for(int i = 0; i < 4; i++) {
                if(preCnt[cnt[i]] > dst) {
                    return false;
                }
            }
            return true;
        }
        public int balancedString(String s) {
            int n = s.length();
            int left = 0, right = 0;
            int ans = n;
            int dst = n / 4;
            int [] preCnt = new int['Z'];
            for(int i = 0; i < s.length(); i++) {
                preCnt[s.charAt(i)]++;
            }
            
            while(right < n) {
                preCnt[s.charAt(right)]--;
                System.out.println(" " + left + " " + right);
                 while(check(preCnt, dst) && left < n) {
                    ans = Math.min(ans, right - left + 1);
                    preCnt[s.charAt(left)]++;
                    left++;
                }
                right++;
            }
            return ans;
        }
    }
}
