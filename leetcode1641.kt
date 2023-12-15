import java.util.*

class Solution {
    fun countVowelStrings(n: Int): Int {
        val tab = arrayOf("a","e","i","o","u")
        var pre:MutableMap<String, Int> = mutableMapOf<String, Int>().withDefault({0})
        for(v in tab) {
            pre[v] = 1
        }
        if(n == 1) {
            return 5
        }
        for(i in 1..n-1) {
            var next: MutableMap<String, Int>  = mutableMapOf<String, Int>().withDefault({0})
            next["a"] = pre.getOrElse("a",{0})
            next["e"] = pre.getOrElse("a",{0}) + pre.getOrElse("e", {0})
            next["i"] = pre.getOrElse("a",{0})  + pre.getOrElse("e", {0}) +
                       pre.getOrElse("i", {0})
            // println("${next["i"]} ${pre["a"]} ${pre["e"]} ${pre["i"]}")
            next["o"] = pre.getOrElse("a",{0})  + pre.getOrElse("e", {0}) +
                       pre.getOrElse("i", {0}) + pre.getOrElse("o", {0})
            next["u"] = pre.getOrElse("a",{0})  + pre.getOrElse("e", {0}) +
                       pre.getOrElse("i", {0})  + pre.getOrElse("o", {0})  +  pre.getOrElse("u", {0})
            pre = next
        }
        // println(pre)
        var ans = 0
        for(v in tab) {
            ans += pre[v]?:0
        }
        return ans
    }
}

fun main(args:Array<String>) {
    val sol = Solution()
    val ret = sol.countVowelStrings(33)
    println("${ret}")
}