import java.util.*

class Solution {
    fun checkArithmeticSubarrays(nums: IntArray, l: IntArray, r: IntArray): List<Boolean> {
        // println(Arrays.toString(nums))
        var ret = mutableListOf<Boolean>()
        val m = l.size
        for(i in 0..m-1) {
            var temp = nums.slice(l[i]..r[i])
            // var tempM:MutableList<Int> = temp
            temp = temp.sortedBy({it})
            if(temp.size == 1) {
                ret.add(true)
            } else {
                val diff = temp[1] - temp[0]
                // println("${temp} ${diff}")
                var find = true
                for(j in temp.indices) {
                    if(j > 0 && temp[j] - temp[j - 1] != diff) {
                        find = false
                        break
                    }
                    // println(i)
                }
                ret.add(find)
            }
            // println("${temp}")
        }

        return ret
    }

}

fun main(args:Array<String>) {
    println("Hello Kotlin")
    
    val nums = intArrayOf(4,6,5,9,3,7)
    val l = intArrayOf(0,0,2)
    val r = intArrayOf(2,3,5)
    val sol = Solution()
    val ret = sol.checkArithmeticSubarrays(nums, l, r)
    println("${ret}")


}