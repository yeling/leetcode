import java.util.*;

// 注意类名必须为 Main, 不要有任何 package xxx 信息
public class Solution {

    // Definition for a binary tree node.
    class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

        TreeNode() {
        }

        TreeNode(int val) {
            this.val = val;
        }

        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }

    public boolean dfs(TreeNode cur) {
        if(cur.left == null && cur.right == null) {
            return cur.val == 1;
        } else {
            if(cur.val == 2) {
                return dfs(cur.left) || dfs(cur.right); 
            } else if (cur.val == 3) {
                return dfs(cur.left) && dfs(cur.right); 
            }
        }
        return false;
    }

    public boolean evaluateTree(TreeNode root) {
        return dfs(root);
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

    }
}
