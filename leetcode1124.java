import java.util.*;

// 注意类名必须为 Main, 不要有任何 package xxx 信息
public class leetcode1124 {
    static boolean find = false;

    public static void main(String[] args) {
        // int [] nums = new int[]{5,14,13,8,12};
        // int[] hours = new int[] { 9, 9, 6, 0, 6, 6, 9 };
        int [] hours =new int[] {6,6,9};
        Solution sol = new Solution();
        System.out.println(sol.longestWPI(hours));

    }

    static class Solution {
        public int longestWPI(int[] hours) {
            int n = hours.length;
            int [] pre = new int[hours.length + 1];
            for(int i = 0; i < n; i++) {
                pre[i + 1] = pre[i];
                if(hours[i] > 8) {
                    pre[i + 1]++;
                } else {
                    pre[i + 1]--;
                }
            }
            Map<Integer,Integer> cache = new HashMap<>();
            int ans = 0;
            for(int i = 0; i < n; i++) {
                if(pre[i + 1] > 0) {
                    ans = Math.max(ans, i + 1);
                } else {
                    Integer left = cache.get(pre[i + 1] - 1);
                    if(left != null) {
                        ans = Math.max(ans, i - left);
                    }
                }
                if(cache.get(pre[i + 1]) == null) {
                    cache.put(pre[i + 1], i);
                }
            }
            return ans;
        }

        //30 / 98 
        //42 / 98
        public int longestWPI2(int[] hours) {
            int ans = 0;
            int left = 0, right = 0;
            int big = 0, small = 0;
            while (right < hours.length) {
                if (hours[right] > 8) {
                    big++;
                } else {
                    small++;
                }
                if (big > small) {
                    ans = Math.max(ans, right - left + 1);
                } else {
                    while (small >= big & left <= right) {
                        if (hours[left] > 8) {
                            big--;
                        } else {
                            small--;
                        }
                        left++;
                    }
                }
                right++;
            }

            return ans;
        }
    }
}
