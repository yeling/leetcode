import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.*;

// 注意类名必须为 Main, 不要有任何 package xxx 信息
public class agc061a {
    static boolean find = false;

    public static void main(String[] args) {
        FastScanner in = new FastScanner(System.in);
        // 注意 hasNext 和 hasNextLine 的区别
        
        
        
        // solve(3,1);
        for(int i = 2;i  < 18; i++) {
            solve(i,1);
        }
        // solve(6,1);
        // solve2(6,1);
        // solve(6,1);
        // solve(7,1);
        // solve(8,1);
        // solve(9,1);
        // solve(10,1);
        // solve2(6,1);
        // solve(6,1);
        // solve(7,1);
        // solve(8,1);

        // int caseNum = in.nextInt();
        // for(int i = 0; i < caseNum; i++) {
        //     int n = in.nextInt();
        //     int k = in.nextInt();
        //     int [] org = new int[n + 1];
        //     for(int j = 1; j <= n; j++) {
        //         org[j] = j;
        //     }
        //     dfs( 1, n, org);
        //     System.out.println(org[k]);
        // }
        
    }
    public static void solve2(int n, int k) {
        int [] org = new int[n + 1];
        for(int j = 1; j <= n; j++) {
            org[j] = j;

        }
        LinkedList<int []> stack = new LinkedList<>();
        stack.add(new int[]{1,n});
        int cnt = 0;
        while(stack.size() > 0) {
            cnt ++ ;
            int [] curr = stack.pop();
            int l = curr[0], r = curr[1];
            if(curr[0] + 1 == curr[1]) {
                int temp = org[r];
                org[r] = org[l];
                org[l] = temp;
            } else {
                stack.push(new int[] {l + 1, r});
                stack.push(new int[] {l, r - 1});
            }
        }
        System.out.println(n + " " + org[k] + " " + cnt);
        System.out.println(Arrays.toString(org));
    }

    public static void solve(int n, int k) {
        int [] org = new int[n + 1];
        for(int j = 1; j <= n; j++) {
            org[j] = j;

        }
        dfs( 1, n, org);
        System.out.println(n + " " + org[k]);
        System.out.println(Arrays.toString(org));
    }

    public static void dfs(int l, int r, int [] org) {
        // System.out.println(l + " " + r);
        if(r == l + 1) {
            // System.out.println("change " + l + " " + r);
            int temp = org[r];
            org[r] = org[l];
            org[l] = temp;
            return;
        } else {
            dfs(l, r - 1, org);
            dfs(l + 1,r, org);
        }
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
