import java.util.*

class Solution {
    fun maxWidthOfVerticalArea(points: Array<IntArray>): Int {
        // points.sortBy({it[0]})
        points.sortWith(object:Comparator<IntArray> {
            override
            fun compare(a: IntArray, b: IntArray): Int {
                return a[0] - b[0]
            }
        })
        var ans = 0
        for((index, item) in points.withIndex()) {
            if(index > 0) {
                ans = Math.max(ans, item[0] - points[index - 1][0])
            }
        }
        return ans
    }
}

fun main(args:Array<String>) {

    val points = arrayOf(intArrayOf(3,1),intArrayOf(9,0))
    val sol = Solution()
    val ret = sol.maxWidthOfVerticalArea(points)
    println("${ret}")


}