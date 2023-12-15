import java.util.*;

// 注意类名必须为 Main, 不要有任何 package xxx 信息
public class Main {
    static boolean find = false;
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        // 注意 hasNext 和 hasNextLine 的区别
        String s = in.nextLine();
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < s.length(); i++) {
            if(s.charAt(i) == '0') {
                sb.append('1');
            } else if(s.charAt(i) == '1') {
                sb.append('0');
            }
        }
        System.out.println(sb.toString());
        in.close();
    }
}
    