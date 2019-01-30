package arraysandstrings

/*
pg. 90
1.2 Check Permutation: Given two strings, write a method to decide if one is a permutation of the other
 */

fun checkPermutation(s1: String, s2: String): Boolean {

    if (s1.length == s2.length) return false

    val charMap = mutableMapOf<Char, Int>()
    for (i in 0 until s1.length) {

        val charCount = charMap.getOrPut(s1[i]) { 0 }
        charMap.replace(s1[i], charCount + 1)

        val charCountS2 = charMap.getOrPut(s2[i]) { 0 }
        charMap.replace(s2[i], charCountS2 - 1)
    }

    return charMap.values.all { i -> i == 0 }
}
