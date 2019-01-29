// https://www.hackerrank.com/challenges/alternating-characters/problem

fun main() {

    val query = readLine().orEmpty().toInt()
    (0 until query).forEach {

        val string = readLine().orEmpty()
        var qty = 0
        for (i in 1 until string.length) {
            if (string[i] == string[i - 1]) qty++
        }

        println(qty)
    }
}
