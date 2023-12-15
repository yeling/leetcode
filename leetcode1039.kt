import java.util.*

class Solution {
    //贪心+dfs 每次选择最小的两个不相邻的边相连
    fun minScoreTriangulation(values: IntArray): Int {
        fun dfs(curr:IntArray):Int {
            cache = mutableIntArrayOf<>()
            for 
        }
        return 10
    }
}

fun main(args:Array<String>) {
    val nums = intArrayOf(3,7,4,5)
    val sol = Solution()
    val ret = sol.minScoreTriangulation(nums)
    println("${ret}")


}