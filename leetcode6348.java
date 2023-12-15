// package newcode;
// package leetcode;
// import java.util.Scanner;
import java.util.Comparator;
import java.util.PriorityQueue;

// 注意类名必须为 Main, 不要有任何 package xxx 信息
public class leetcode6348 {
    static boolean find = false;
    public static void main(String[] args) {
       
        int [] gifts = new int[]{25,64,9,4,100};
        int k = 4;

        Solution solution = new Solution();
        System.out.println(solution.pickGifts(gifts, k));
    }

    
}

class Solution {
    public long pickGifts(int[] gifts, int k) {
        long ans = 0;
        PriorityQueue<Integer> stack = new PriorityQueue<>(new Comparator<Integer>() {
            @Override
            public int compare(Integer a, Integer b) {
                return b - a;
            }
        });
        for(int i = 0; i < gifts.length; i++) {
            stack.add(gifts[i]);
        }
        for(int j = 0; j < k; j++) {
            int cur = stack.poll();
            stack.add((int)Math.sqrt(cur));
        }
        ans = 0;
        while(!stack.isEmpty()) {
            ans += stack.poll();
        }
        return ans;
    }
}