// https://www.hackerrank.com/challenges/ctci-making-anagrams/problem

fun main() {

    val a = readLine().orEmpty()
    val b = readLine().orEmpty()
    val charCount = mutableMapOf<Char, Int>()
    for (char in a) charCount[char] = charCount.getOrDefault(char, 0) + 1
    for (char in b) charCount[char] = charCount.getOrDefault(char, 0) - 1
    val deleteCount = charCount.map { (_, value) -> Math.abs(value) }.sum()
    println(deleteCount)
}