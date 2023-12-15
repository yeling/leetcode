import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.*;

// 注意类名必须为 Main, 不要有任何 package xxx 信息
public class nowcoder51663c {
    
    public static void main(String[] args) {
        FastScanner in = new FastScanner(System.in);
        // 注意 hasNext 和 hasNextLine 的区别
        int xa = in.nextInt();
        int ya = in.nextInt();
        int xb = in.nextInt();
        int yb = in.nextInt();
        solve(xa, ya, xb, yb);
    }

    public static void solve(int xa, int ya, int xb, int yb) {
        
        if(xa > xb) {
            int temp = xa;
            xa = xb;
            xb = temp;
            temp = ya;
            ya = yb;
            yb = temp;
        }
        int ans = 0;
        for(int i = xa; i <= xb; i++) {
            if(i == 0) {
                ans++;
            } else {
                if(ya * (xb - xa) == (yb - ya) * (xa - i)) {
                    ans++;
                }
            }
        }
        System.out.println(ans);
    }

    private static class FastScanner {

        private BufferedReader reader = null;
        private StringTokenizer tokenizer = null;

        public FastScanner(InputStream in) {
            reader = new BufferedReader(new InputStreamReader(in));
            tokenizer = null;
        }

        public String next() {
            if (tokenizer == null || !tokenizer.hasMoreTokens()) {
                try {
                    tokenizer = new StringTokenizer(reader.readLine());
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            }
            return tokenizer.nextToken();
        }

        public String nextLine() {
            if (tokenizer == null || !tokenizer.hasMoreTokens()) {
                try {
                    return reader.readLine();
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            }

            return tokenizer.nextToken("\n");
        }

        public long nextLong() {
            return Long.parseLong(next());
        }

        public int nextInt() {
            return Integer.parseInt(next());
        }

        public double nextDouble() {
            return Double.parseDouble(next());
        }

        public int[] nextIntArray(int n) {
            int[] a = new int[n];
            for (int i = 0; i < n; i++) {
                a[i] = nextInt();
            }
            return a;
        }

        public long[] nextLongArray(int n) {
            long[] a = new long[n];
            for (int i = 0; i < n; i++) {
                a[i] = nextLong();
            }
            return a;
        }
    }
}