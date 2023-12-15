// package newcode;
package leetcode.newcode;
import java.util.Set;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.HashSet;
import java.util.List;
import java.util.Scanner;

// 注意类名必须为 Main, 不要有任何 package xxx 信息
public class hj3 {
    static boolean find = false;
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        
        int n = in.nextInt();
        Set<Integer> cache = new HashSet<Integer>();
        for(int i = 0; i < n; i++) {
            int temp = in.nextInt();
            cache.add(temp);
        }
        List<Integer> allNum = new ArrayList<Integer>();
        for(Integer i : cache) {
            allNum.add(i);
        }
        allNum.sort(new Comparator<Integer>() {
            @Override
            public int compare(Integer a, Integer b) {
                return a - b;
            }
        });
        for(int i = 0; i < allNum.size(); i++) {
            System.out.println(allNum.get(i) + " ");
        }
        
        in.close();

    }
}
    