package leetcode.newcode;
// package newcode;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

// 注意类名必须为 Main, 不要有任何 package xxx 信息
public class hj26 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        // 注意 hasNext 和 hasNextLine 的区别
        String str = in.nextLine();
        List<Character> c1[] = new List[26];
        Character ans [] = new Character[str.length()];
        for(int i = 0; i < 26; i++) {
            c1[i] = new ArrayList<Character>();
        }
        for(int i = 0; i < str.length(); i++) {
            if(str.charAt(i) <= 'Z' && str.charAt(i) >= 'A') {
                c1[str.charAt(i) - 'A'].add(str.charAt(i));
                
            } else if(str.charAt(i) <= 'z' && str.charAt(i) >= 'a') {
                c1[str.charAt(i) - 'a'].add(str.charAt(i));
            } else {
                ans[i] = str.charAt(i);
            }
        }
        int j = 0,k = 0;
        for(int i = 0; i < ans.length; i++) {
            while(j < c1.length && k == c1[j].size()) {
                k = 0;
                j += 1;
            }
            
            if(ans[i] == null) {
                System.out.print(c1[j].get(k));
                k += 1;
            } else {
                System.out.print(ans[i]);
            }   
        }
        in.close();
        System.out.println('a' - 'z');
    }


    
}