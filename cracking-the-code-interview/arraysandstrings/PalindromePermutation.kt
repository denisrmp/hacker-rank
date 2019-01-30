package arraysandstrings

/*
pg 91
Question 1.4 Palindrome Permutation
 */

fun isPalindromable(str: String): Boolean {

    val aIndex = 'a'.toInt()
    val oddMap = BooleanArray(26) { false }
    str.forEach { c ->
        val charIndex = c.toInt() - aIndex
        if (charIndex in 0 until 26) oddMap[charIndex] = !oddMap[charIndex]
    }

    return oddMap.count { b -> b } <= 1
}

fun main() {

    val t1 = "not a palindrome"
    val t2 = "ar ar a!"
    println("'$t1' isPalindrome=${isPalindromable(t1.toLowerCase())}")
    println("'$t2' isPalindrome=${isPalindromable(t2.toLowerCase())}")
}