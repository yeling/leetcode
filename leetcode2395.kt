import java.util.*

class Solution {
    fun findSubarrays(nums: IntArray): Boolean {
        var cache = mutableSetOf<Int>()
        for(i in 1..nums.size - 1) {
            val temp = nums[i] + nums[i - 1]
            if(temp in cache) {
                return true
            } else {
                cache.add(temp)
            }
        }
        return false

    }
}

fun main(args:Array<String>) {
    val nums = intArrayOf(4,2,5)
    val sol = Solution()
    val ret = sol.findSubarrays(nums)
    println("${ret}")

}