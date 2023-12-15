// package cf1788b;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

// 注意类名必须为 Main, 不要有任何 package xxx 信息
public class cf1788b {
    static boolean find = false;
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        // 注意 hasNext 和 hasNextLine 的区别
        int caseNum = in.nextInt();
        System.out.println("caseNum " + caseNum);
        in.nextLine();
        for(int i = 0; i < caseNum; i++) {
            int n = in.nextInt();
            solve(n);
        }
        
        in.close();
    }

    public static void solve(int n) {
        System.out.println(n);
    }

    static class FastScanner
    {
 
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer("");
 
        String next()
        {
            while (!st.hasMoreTokens()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }
 
        int nextInt()
        {
            return Integer.parseInt(next());
        }
 
        long nextLong()
        {
 
            return Long.parseLong(next());
        }
 
        double nextDouble()
        {
            return Double.parseDouble(next());
        }
 
        String nextLine() throws IOException
        {
            return br.readLine();
        }
    }
}
    