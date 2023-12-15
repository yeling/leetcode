import java.io.FileInputStream;
import java.util.*;

// 注意类名必须为 Main, 不要有任何 package xxx 信息
public class abc289c {
    static boolean find = false;
    public static void main(String[] args) {
        Scanner in = null;
        try {
            in = new Scanner(new FileInputStream("input.txt"));
        } catch(Exception e) {
            in = null;
        }
        if(in == null) {
            in = new Scanner(System.in);
        }
        // 注意 hasNext 和 hasNextLine 的区别
        int n = in.nextInt();
        int m = in.nextInt();
        List<List<Integer>> all = new ArrayList<>();
        for(int i = 0; i < m; i++) {
            int c = in.nextInt();
            List<Integer> temp = new ArrayList<>();
            for(int j = 0; j < c; j++) {
                temp.add(in.nextInt());
            }
            all.add(temp);
        }
        solve(n, m, all);
    }

    public static void solve(int n, int m, List<List<Integer>> all) {
        int ans = 0;
        // System.out.println(1<<m);
        for(int i = 1; i < (1<<m); i++) {
            // System.out.println(i);
            boolean [] temp = new boolean[n + 1];
            for(int j = 0; j < m; j++) {
                // System.out.println("" + i + j + " "+(1 << m) +" " +  (i&j)+ flag);
                if((i & (1 <<j)) != 0) {
                    for(Integer curr : all.get(j)) {
                        temp[curr] = true;
                    }
                }
            }
            boolean check = true;
            for(int k = 1; k <= n; k++) {
                check = check & temp[k];
            }
            if(check) {
                ans += 1;
            }
        }
        System.out.println(ans);
    }
    
}
    