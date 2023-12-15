import java.util.*

class Solution {
    // 105 / 118 
    fun findLengthOfShortestSubarray(arr: IntArray): Int {
        var left = 0
        var right = arr.size - 1
        
        //find max left
        while(left + 1 < arr.size) {
            if(arr[left + 1] >= arr[left]) {
                left++
            } else {
                break
            }
        }
        // println("$left ${arr.size}")
        var ans = arr.size - 1 - left

        while(left < right && left >= 0) {
            if(arr[left] > arr[right]) {
                left--
            } else {
                var temp = right
                while(left <= temp && arr[left] <= arr[temp - 1] && arr[temp] >= arr[temp - 1]) {
                    temp -= 1
                }
                ans = Math.min(ans, temp - left - 1)
                right = temp
                left--
            }
        }
        if(left == -1) {
            while(right - 1 >= 0 && arr[right] >= arr[right - 1]) {
                right--
            }
            ans = Math.min(ans, right)
        }
        return ans
    }

}

fun main(args:Array<String>) {
    var nums = intArrayOf(1,2,3,10,2,2,3,5)
    nums = intArrayOf(16,10,0,3,22,1,14,7,1,12,15)
    val sol = Solution()
    val ret = sol.findLengthOfShortestSubarray(nums)
    println("${ret}")
}