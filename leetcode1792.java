import java.util.*;

// 注意类名必须为 Main, 不要有任何 package xxx 信息
public class leetcode1792 {
    static boolean find = false;

    public static void main(String[] args) {
        // int [] nums = new int[]{5,14,13,8,12};
        int[][] classes = new int[][] {
                new int[] { 1, 2 },
                new int[] { 3, 5 },
                new int[] { 2, 2 }
        };
        int extraStudents = 2;
        Solution sol = new Solution();
        System.out.println(sol.maxAverageRatio(classes, extraStudents));

    }

    static class Solution {
        public double maxAverageRatio(int[][] classes, int extraStudents) {
            
            PriorityQueue<int []> stack = new PriorityQueue<>(new Comparator<int []>(){
                @Override
                public int compare(int [] a, int [] b) {
                    long val1 = (long) (b[1] + 1) * b[1] * (a[1] - a[0]);
                    long val2 = (long) (a[1] + 1) * a[1] * (b[1] - b[0]);
                    if (val1 == val2) {
                        return 0;
                    }
                    return val1 < val2 ? 1 : -1;
                }

            });
            
            for(int i = 0; i < classes.length; i++) {
                if(classes[i][0] < classes[i][1]) {
                    stack.add(classes[i]);
                }
            }
            double ans = classes.length - stack.size();
            for(int i = 0; i < extraStudents && stack.isEmpty() == false; i++) {
                int [] temp = stack.poll();
                temp[0]++;
                temp[1]++;
                stack.add(temp);
            }
            while(stack.isEmpty() == false) {
                int [] temp = stack.poll();
                // System.out.println(Arrays.toString(temp));
                ans += (double)temp[0]/temp[1];
            }
            return ans/classes.length;
        }
    }
}
