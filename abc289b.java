import java.util.*;

// 注意类名必须为 Main, 不要有任何 package xxx 信息
public class abc289b {
    static boolean find = false;
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        // solve(5, 0, new int[]{1,3,4});
        // solve(10, 6, new int[]{1,2,3,7,8,9});
        // 注意 hasNext 和 hasNextLine 的区别
        int n = in.nextInt();
        int m = in.nextInt();
        String s = "";
        try {
            in.nextLine();
            s = in.nextLine();
        } catch(Exception e) {

        }
        String [] arr = s.split(" ");
        int [] nums = new int[arr.length];
        for(int i = 0; i < m; i++) {
            nums[i] = Integer.parseInt(arr[i]);
        }
        solve(n, m, nums);
        in.close();
    }

    public static void solve(int n, int m, int [] nums) {
        // System.out.println("" + n +  m +  nums);
        boolean [] vis = new boolean[n + 1];
        List<Integer> ans = new ArrayList<Integer>();
        int [] next = new int[n + 1];
        for(int i = 0; i < m; i++) {
            next[nums[i]] = nums[i] + 1;
        }
        for(int i = 1; i <= n; i++) {
            if(vis[i] == false) {
               
                List<Integer> temp = new ArrayList<Integer>();
                int curr = i;
                vis[i] = true;
                temp.add(i);
                while(next[curr] != 0) {
                    vis[next[curr]] = true;
                    temp.add(next[curr]);
                    curr = next[curr];
                }
                temp.sort(new Comparator<Integer>() {

                    @Override
                    public int compare(Integer a, Integer b) {
                        // TODO Auto-generated method stub
                        return b - a;
                    }
                    
                });
                ans.addAll(temp);
                
            }
        }
        StringBuilder sb = new StringBuilder();
        for(Integer i: ans){
            sb.append(i + " ");
        }
        System.out.println(sb.toString());
        
    }
}
    