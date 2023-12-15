import java.util.Scanner;

// 注意类名必须为 Main, 不要有任何 package xxx 信息
public class Main {
    static boolean find = false;
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        // 注意 hasNext 和 hasNextLine 的区别
        String str = "CCCAAGTCTTCCAATCGTGCCCCCCAATTGAGTCTCGCTCCCCAGGTGAGATACATCAGAAGC";
        int n = 63;
        str = in.nextLine();
        n = in.nextInt();
        solve(str, n);

        in.close();
    }

    public static void solve(String str, int n) {
        double max = -1;
        String ans = "";
        for(int i = 0; i <= str.length() - n; i++) {
            String now = str.substring(i, i + n);
            double cnt = 0;
            for(int j = 0; j < now.length(); j++) {
                if(now.charAt(j) == 'G' || now.charAt(j) == 'C') {
                    cnt++;
                }
            }
            if(cnt/now.length() > max || max == -1) {
                max = cnt/now.length();
                ans = now;
            }
        }
        System.out.println(ans);
    }

    
}
    