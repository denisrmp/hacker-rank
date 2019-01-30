package arraysandstrings

/*
Question 1.6 String Compression
 */

fun compress(str: String): String {

    val sb = StringBuilder()
    var counter = 0
    var lastChar: Char? = null
    for (c in str) {

        if (c == lastChar) {

            counter++
        } else {

            if (lastChar != null) {

                sb.append(lastChar).append(counter)
                if (sb.length >= str.length) return str
            }

            lastChar = c
            counter = 1
        }
    }

    sb.append(lastChar).append(counter)
    return if (sb.length >= str.length) str else sb.toString()
}

fun main() {

    println("compress ${ compress("aabcccccaaa") }")
    println("compress ${ compress("abddjws") }")
    println("compress ${ compress("abcdfghjuytt") }")
    println("compress ${ compress("abcdfghjuyt") }")
}