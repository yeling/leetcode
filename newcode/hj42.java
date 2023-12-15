// package newcode;
package leetcode.newcode;
import java.util.Scanner;

// 注意类名必须为 Main, 不要有任何 package xxx 信息
public class hj42 {
    static boolean find = false;
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        // 注意 hasNext 和 hasNextLine 的区别
        int num = in.nextInt();
        String res = "";
        //and,billion,million,thousand,hundred
        // 22: twenty two
        // 100:  one hundred 
        // 145:  one hundred and forty five
        // 1,234:  one thousand two hundred and thirty four
        // 8,088:  eight thousand (and) eighty eight (注:这个and可加可不加，这个题目我们选择不加)
        // 486,669:  four hundred and eighty six thousand six hundred and sixty nine
        // 1,652,510:  one million six hundred and fifty two thousand five hundred and ten
        //2,000,000 
        //百位数和十位数之间要加and



        in.close();
    }

    public static String solve(int n) {
        String [] single  = new String[]{"one","two","three","four","five","six","eight","nine","ten"};
        String res = "";
        
    }
}
    