

class Solution {
    fun commonFactors(a: Int, b: Int): Int {
        val cnt = Math.min(a,b)
        var ans = 0
        for(i in 1..cnt) {
            if(a%i == 0 && b%i == 0) {
                ans += 1
            }
        }
        return ans
    }
}

fun main(args:Array<String>) {

    val nums = intArrayOf(4,6,5,9,3,7)
    val sol = Solution()
    val ret = sol.commonFactors(2,6)
    println("${ret}")


}