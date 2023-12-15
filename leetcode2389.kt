import java.util.*

class Solution {
    fun answerQueries(nums: IntArray, queries: IntArray): IntArray {
        val n = nums.size
        val m = queries.size
        nums.sort()
        var ans:IntArray = IntArray(m)
        var pre:IntArray = IntArray(n+1)
        for(i in nums.indices) {
            pre[i + 1] = nums[i] + pre[i]
        }
        // println("$n $m ${Arrays.toString(pre)}")
        for(i in queries.indices) {
            for(j in nums.indices) {
                if(pre[j + 1] > queries[i]) {
                    break
                } else {
                    ans[i] = j + 1
                }
            }
            // println("$i + ${queries.get(i)}  ${ans[i]}" )
        }
        // println("$n $m ${Arrays.toString(ans)}")
        return ans
    }
}

fun main(args:Array<String>) {
    println("Hello Kotlin")
    val nums = intArrayOf(4,5,2,1)
    val queries = intArrayOf(3,10,21)
    val sol = Solution()
    val ret:IntArray = sol.answerQueries(nums, queries)
    println("${Arrays.toString(ret)}")

    val chars = ('a'..'z' step 2).toList()
    println(chars)
    println(chars.take(3))
    println(chars.takeLast(3))
    val ind:IntRange = chars.indices
    println("$ind ${ind.average()}")

    val all = (1..20 step 2).toList()
    val all2 = (30 downTo 2 step 2).toList()
    println("$all \n$all2")
    all2.filter{it > 5}
        .sortedBy{it}
        .forEach{println(it)}
    all2[5]?.let {
        println("all2[5] = $it")
    }

    var state:Boolean = false 
    println(state)
    state = all2[10] == 6
    state.let {
        println("state = $it")
    }

    val testList = mutableListOf(1,2,3)
    val testList1:List<Int> = testList
    testList.add(4)

    println("$testList $testList1")

    val fruitsBag = listOf("apple","orange","banana","grapes")  // 1
    val clothesBag = listOf("shirts","pants","jeans")
    val cart = listOf(fruitsBag, clothesBag)
    val flatMapBag = cart.flatMap { it }
    flatMapBag.let {
        println(it)
    }

    val A = listOf("a", "b", "c")                  // 1
    val B = listOf(1, 2, 3, 4)                     // 1

    val resultPairs = A zip B   
    println(resultPairs)                   // 2
    val resultReduce = A.zip(B) { a, b -> "$a$b" } // 3
    resultReduce.forEach{
        println(it)
    }
    //[apple, orange, banana, grapes, shirts, pants, jeans]

}