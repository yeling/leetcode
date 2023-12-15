// package newcode;
package leetcode.newcode;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.HashSet;
import java.util.List;
import java.util.Scanner;
import java.util.Set;

// 注意类名必须为 Main, 不要有任何 package xxx 信息
public class hc2 {
    static boolean find = false;
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        // 注意 hasNext 和 hasNextLine 的区别
        int m = in.nextInt();
        in.nextLine();
        if(m > 10 || m < 1) {
            System.out.println("[[]]");
            return;
        } 
        List<List<Integer>> grid = new ArrayList<>();
        for(int i = 0; i < m; i++) {
            String str = in.nextLine();
            // System.out.println(str);
            String [] ans = str.split("\\,");
            if(ans.length == 0 || ans.length > 100) {
                System.out.println("[[]]");
                return;
            }
            // System.out.println(ans.length);
            List<Integer> cur = new ArrayList<>();
            for(String s:ans) {
                cur.add(Integer.parseInt(s));
            }
            grid.add(cur);
            // System.out.println(grid[i].size());
        }
        join(grid);
        System.out.print("[");
        for(int j = 0; j < grid.size(); j++) {
            List<Integer> nums = grid.get(j);
            nums.sort(new Comparator<Integer>() {

                @Override
                public int compare(Integer t0, Integer t1) {
                    return t0 - t1;
                }
            });
            if(j > 0) {
                System.out.print(",");
            }
            System.out.print("[");
            for(int i = 0; i < nums.size(); i++) {
                if(i == 0 || nums.get(i) != nums.get(i - 1)) {
                    if(i > 0) {
                        System.out.print(",");
                    }
                    System.out.print(nums.get(i));
                }
            }
            System.out.print("]");
        }
        System.out.print("]");
        
        in.close();

    }

    public static void join(List<List<Integer>> grid) {
        for(int i = 0; i < grid.size(); i++) {
            for(int j = i + 1; j < grid.size(); j++) {
                if(canJoin(grid, i, j)) {
                    grid.get(i).addAll(grid.get(j));
                    grid.remove(j);
                    join(grid);
                    return;
                }
            }
        }
    }

    public static boolean canJoin(List<List<Integer>> grid, int i, int j) {
        int same = 0;
        boolean vis [] = new boolean[grid.get(j).size()];
        for(int pi = 0; pi < grid.get(i).size(); pi++) {
            for(int qj = 0; qj < grid.get(j).size(); qj++) {
                if(grid.get(i).get(pi) == grid.get(j).get(qj) && vis[qj] == false) {
                    vis[qj] = true;
                    same++;
                    break;
                }
                if(same >= 2) {
                    return true;
                }
            }
            if(same >= 2) {
                return true;
            }
        }
        return false;
    }
}
    