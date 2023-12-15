import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.*;

// 注意类名必须为 Main, 不要有任何 package xxx 信息
public class arc156a {
    static boolean find = false;

    public static void main(String[] args) {
        FastScanner in = new FastScanner(System.in);
        // 注意 hasNext 和 hasNextLine 的区别
        int caseNum = in.nextInt();
        for(int i = 0; i < caseNum; i++) {
            int size = in.nextInt();
            // in.nextLine();
            String s = in.nextLine();
            System.out.println("size " + size + s);
            int cnt = 0;
            for(int j = 0; j < s.length(); j++) {
                if(s.charAt(j) == '1') {
                    cnt++;
                }
            }
            if(cnt == 2 && s.length() == 2) {
                System.out.println(-1);
            } else if(cnt%2 == 0) {
                System.out.println((int)cnt/2);
            } else {
                System.out.println(-1);
            }

        }
        
        
    }

    public static void solve() {

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
