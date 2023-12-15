package newcode;
import java.util.Arrays;
// package leetcode.newcode;
import java.util.Scanner;

// 注意类名必须为 Main, 不要有任何 package xxx 信息
public class hj17 {
    
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        // 注意 hasNext 和 hasNextLine 的区别
        
        String test = "A10;S20;W10;D30;X;A1A;B10A11;;A10;";
        // test = in.nextLine();

        solve(test);
        in.close();

    }

    public static void solve(String src) {
        //A表示向左移动，D表示向右移动，W表示向上移动，S表示向下移动
        int [] pos = new int[2];
        String [] arr = src.split("\\;");
        System.out.println(Arrays.toString(arr));
        for(String cur : arr) {
            if(cur.length() == 0) {
                continue;
            }
            try {
                int step = Integer.parseInt(cur.substring(1));
                switch(cur.charAt(0)) {
                    case 'W':
                        pos[1] += step;
                        break;
                    case 'S':
                        pos[1] -= step;
                        break;
                    case 'A':
                        pos[0] -= step;
                        break;
                    case 'D':
                        pos[0] += step;
                        break;
                }
            } catch(Exception e){
            }
        }
        System.out.println(pos[0] + "," + pos[1]);
    }
}
    