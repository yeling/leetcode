// package newcode;
package leetcode.newcode;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

// 注意类名必须为 Main, 不要有任何 package xxx 信息
public class hc1 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        // 注意 hasNext 和 hasNextLine 的区别
        String all = in.nextLine();
        String [] arr = all.split(" ");
        Arrays.sort(arr, new Comparator<String>() {

            @Override
            public int compare(String a, String b) {
                // TODO Auto-generated method stub
                return b.length() - a.length();
            }
            
        });
        //
        // System.out.println(Arrays.toString(arr));
        List<String> dst = new ArrayList<String>();
        List<String> next = new ArrayList<String>();
        int dstLen = arr[0].length();
        int nextLen = dstLen - 1;
        for(int i = 0; i < arr.length; i++) {
            if(arr[i].length() == dstLen) {
                dst.add(arr[i]);
            } else if(arr[i].length() == nextLen) {
                next.add(arr[i]);
            } else {
                if(next.size() == 0) {
                    next.add(arr[i]);
                }
                Map<Integer,Integer> removePos = new HashMap<Integer,Integer>();
                for(int di = dst.size() - 1; di >= 0; di--) {
                    String dstStr = dst.get(di).substring(0,nextLen);
                    int nextPos = next.indexOf(dstStr);
                    if(nextPos == -1) {
                        dst.remove(di);
                    } else {
                        removePos.put(nextPos, 1);
                    }
                }
                for(int dj = 0; dj < next.size(); dj++) {
                    if(removePos.get(dj) == null) {
                        dst.add(next.get(dj));
                    }
                }
                next.clear();
                dstLen = nextLen;
                nextLen = nextLen - 1;
            }
        }
        if(next.size() > 0) {
            Map<Integer,Integer> removePos = new HashMap<Integer,Integer>();
            for(int di = dst.size() - 1; di >= 0; di--) {
                String dstStr = dst.get(di).substring(0,1);
                int nextPos = next.indexOf(dstStr);
                if(nextPos == -1) {
                    dst.remove(di);
                } else {
                    removePos.put(nextPos, 1);
                }
            } 
        }
        dst.sort(new Comparator<String>() {

            @Override
            public int compare(String a, String b) {
                // TODO Auto-generated method stub
                return b.compareTo(a);
            }
            
        });
        if(dst.size() > 0) {
            System.out.println(dst.get(0));
        } else {
            System.out.println(" ");
        }
        // for(int di = 0; di < dst.size(); di++) {
        //     System.out.println(dst.get(di));
        // }
        in.close();
    }

}
    