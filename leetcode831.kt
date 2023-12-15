import java.util.*

class Solution {
    fun maskPII(s: String): String {
        var ans:String = ""
        val index = s.indexOf('@')
        if(index != -1) {
            var name = s.substring(0,index)
            if(name.length >= 2) {
                ans += "${name.first().toLowerCase()}*****${name.last().toLowerCase()}"
            } else {
                ans += "${name.toLowerCase()}"
            }
            ans += "${s.substring(index).toLowerCase()}" 
        } else {
            var number = ""
            for(c in s) {
                if(c.isDigit()) {
                    // println("$c ${c.toInt()}")
                    number += Character.digit(c, 10)
                }
            }
            val nation = number.substring(0, number.length - 10)
            println("$number nation $nation")
            when(nation.length) {
                0-> ans = "***-***-${number.takeLast(4)}"
                1-> ans = "+*-***-***-${number.takeLast(4)}"
                2-> ans = "+**-***-***-${number.takeLast(4)}"
                3-> ans = "+***-***-***-${number.takeLast(4)}"
            }
        }
        // println("$ans")
        return ans
    }
}

fun main(args:Array<String>) {

    // val s = "LeetCode@LeetCode.com"
    val s = "LeetCode@LeetCode.com"
    // var s = "1(234)567-890"
    // s = "86-(10)12345678"
    val sol = Solution()
    val ret = sol.maskPII(s)
    println("${ret}")


}