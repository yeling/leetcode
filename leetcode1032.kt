import java.util.*

class StreamChecker(words: Array<String>) {

    class Node(char: Char) {
        var value = char
        var child = mutableSetOf<Node>()
        var end = false
    }

    private var root:Node
    var cache = mutableListOf<Node>()

    init {
        root = Node('-')
        // root.child.add(Node('c'))
        for(v in words) {
            var temp = root
            for(le in v) {
                var next:Node ?= null
                for(ch in temp.child) {
                    if(ch.value == le) {
                        next = ch
                        break
                    }
                }
                if(next == null) {
                    next = Node(le)
                    temp.child.add(next)
                }
                temp = next
                //println("$le $ret")
            }
            temp.end = true
        }

    }

    fun query(letter: Char): Boolean {
        // println("query ${cache.size} ${letter} ")
        // for(v in cache) {
        //     print("begin ${v.value} ")
        // }
        // println()
        var find = false
        for(curr in cache.size - 1 downTo 0) {
            // println(curr)
            for(ch in cache[curr].child) {
                if(ch.value == letter) {
                    cache.add(ch)
                    if(ch.end) {
                        find = true
                    }
                    break;
                }
            }
            cache.remove(cache[curr])
        }
        for(ch in root.child) {
            if(ch.value == letter) {
                cache.add(ch)
                if(ch.end) {
                    find = true
                }
                break;
            }
        }
        for(v in cache) {
            // print("end ${v} ${v.end} ${v.value} ")
        }
        return find
    }

}

fun main(args:Array<String>) {

    val words = arrayOf("ab","ba","aaab","abab","baa")
    // val ret = words.all{
    //     println(it)
    //     it == "cd"
    // }
    // println("$ret")
    val sol = StreamChecker(words)
    var ret = sol.query('a')
    println("${Arrays.toString(words)} ${ret}")
    ret = sol.query('b')
    println("${Arrays.toString(words)} ${ret}")
    ret = sol.query('a')
    println("${Arrays.toString(words)} ${ret}")


}