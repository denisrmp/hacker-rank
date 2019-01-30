package arraysandstrings

import java.lang.Math.abs

/*
pg. 91 Question 1.5 One Away
 */

fun oneAway(a: CharArray, b: CharArray): Boolean {

    val sizeDiff = a.size - b.size
    if (abs(sizeDiff) > 1) return false

    // by storing the bigger string in x we can treat the "remove" case as an insertion on x
    val (x, y) = if (sizeDiff >= 0) Pair(a, b) else Pair(b, a)

    var xIdx = 0
    var yIdx = 0
    var diff = 0
    while (diff <= 1 && yIdx < y.size) {

        if (x[xIdx] != y[yIdx]) {

            // the case when the bigger string has one insertion
            if (xIdx + 1 < x.size && x[xIdx + 1] == y[yIdx]) xIdx++
            diff++
        }

        xIdx++
        yIdx++
    }

    return diff <= 1
}


fun main() {

    println("Is oneAway? true == ${ oneAway("pale".toCharArray(), "ale".toCharArray()) }")
    println("Is oneAway? true == ${ oneAway("pales".toCharArray(), "pale".toCharArray()) }")
    println("Is oneAway? true == ${ oneAway("pales".toCharArray(), "bale".toCharArray()) }")
    println("Is oneAway? false == ${ oneAway("pales".toCharArray(), "bake".toCharArray()) }")
    println("Is oneAway? true == ${ oneAway("apple".toCharArray(), "aple".toCharArray()) }")
}
