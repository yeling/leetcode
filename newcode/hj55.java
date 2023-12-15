package newcode;
// package leetcode.newcode;
import java.util.Scanner;

// 注意类名必须为 Main, 不要有任何 package xxx 信息
public class hj55 {
    static boolean find = false;
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        // 注意 hasNext 和 hasNextLine 的区别
        int n = in.nextInt();
        System.out.println(solve(n));
        in.close();
    }

    public static int solve(int n) {
        int ans = 0;
        for(int i = 7; i <= n; i++) {
            if(i%7 == 0) {
                ans += 1;
            } else {
                String temp = Integer.toString(i);
                if(temp.indexOf("7") != -1) {
                    ans += 1;
                }
            }
        }
        return ans;
    }
}
    