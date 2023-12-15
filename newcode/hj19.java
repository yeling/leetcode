// package newcode;
package leetcode.newcode;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Map;
import java.util.Scanner;

// 注意类名必须为 Main, 不要有任何 package xxx 信息
public class hj19 {
    static boolean find = false;
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        // 注意 hasNext 和 hasNextLine 的区别
        LinkedList<String> stack = new LinkedList<String>();
        Map<String,Integer> cnt = new HashMap<String,Integer>();
        int max = 8;
        while (in.hasNextLine()) { // 注意 while 处理多个 case
            String cur = in.nextLine();
            String [] arr = cur.split(" ");
            String [] fileNames = arr[0].split("\\\\");
            
            String lastName = fileNames[fileNames.length - 1];

            String key = "";
            if(lastName.length() <= 16) {
                key += lastName;
            } else {
                key += lastName.substring(lastName.length() - 16);
            }
            key += " " + arr[1];
            // System.out.println(key);
            if(cnt.get(key) == null) {
                if(stack.size() == max) {
                    stack.removeFirst();
                }
                stack.addLast(key);
            }
            cnt.put(key, cnt.getOrDefault(key, 0) + 1);
        }
        for(String key : stack) {
            System.out.println(key + " " + cnt.get(key));
        }
        in.close();

    }
}
    