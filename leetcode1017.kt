import java.util.*

class Solution {
    fun baseNeg2(n: Int): String {
        var ans = ""
        val bStr = n.toString(2)
        var add = 0
        var i = bStr.length - 1
        while(i >= 0 || add > 0) {
            var temp = add
            if(i >= 0) {
                temp += Integer.parseInt("" + bStr[i])
            }
            if(temp == 2) {
                temp = 0
                add = 1
            } else {
                add = 0
            }
            if((bStr.length - 1 - i)%2 == 1 && temp == 1) {
                add = 1
            }
            ans =  temp.toString() + ans
            i-- 
        }
       

        return ans
    }
}

fun main(args:Array<String>) {

    val nums = intArrayOf(4,6,5,9,3,7)
    val sol = Solution()
    val ret = sol.baseNeg2(4)
    println("${ret}")


}