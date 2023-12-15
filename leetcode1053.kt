import java.util.*

class Solution {
    // 42 / 54
    fun prevPermOpt12(arr: IntArray): IntArray {
        val ans = arr.slice(0..arr.size-1).toMutableList()
        for(i in arr.size-1 downTo 1) {
            if(ans[i] < ans[i - 1]) {
                for(j in arr.size-1 downTo i) {
                    if(ans[i - 1] != ans[j]) {
                        val temp = ans[i - 1]
                        ans[i - 1] = ans[j]
                        ans[j] = temp
                        break
                    }
                }
                break
            } 
        } 
        return ans.toIntArray()
    }

    fun prevPermOpt1(arr: IntArray): IntArray {
        val ans = arr.slice(0..arr.size-1).toMutableList()
        for(i in arr.size-1 downTo 1) {
            if(ans[i] < ans[i - 1]) {
                var j = arr.size - 1
                while(arr[j] >= arr[i - 1] || arr[j] == arr[j - 1]) {
                    j -- 
                    // println(j)
                }
                val temp = ans[i - 1]
                ans[i - 1] = ans[j]
                ans[j] = temp
                break
            } 
        } 
        return ans.toIntArray()
    }
}

fun main(args:Array<String>) {

    val nums = intArrayOf(3,1,1,3)
    val sol = Solution()
    val ret = sol.prevPermOpt1(nums)
    println("${Arrays.toString(ret)}")


}