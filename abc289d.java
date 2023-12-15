import java.util.*;

// 注意类名必须为 Main, 不要有任何 package xxx 信息
public class abc289d {
    static boolean find = false;
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        // 注意 hasNext 和 hasNextLine 的区别
        int n = in.nextInt();
        int [] ns = new int[n];
        for(int i = 0; i < n; i++) {
            ns[i] = in.nextInt();
        }
        int m = in.nextInt();
        int [] ms = new int[m];
        for(int i = 0; i < n; i++) {
            ms[i] = in.nextInt();
        }
        int x = in.nextInt();
        solve(n, ns, m, ms, x);

    }

    public static void solve(int n, int [] ns, int m, int [] ms, int x) {
        
    }
}
    