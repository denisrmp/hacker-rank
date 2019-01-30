// https://www.hackerrank.com/challenges/two-strings/problem

fun main() {

    val pairs = readLine().orEmpty().trim().toInt()
    (0 until pairs).forEach {
        val a = readLine().orEmpty().trim().toCharArray().toSet()
        val b = readLine().orEmpty().trim().toCharArray().toSet()
        println(if (a.intersect(b).isEmpty()) "NO" else "YES")
    }
}