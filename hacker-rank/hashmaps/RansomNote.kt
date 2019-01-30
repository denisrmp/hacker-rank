// https://www.hackerrank.com/challenges/ctci-ransom-note/problem

fun main(args: Array<String>) {

    val (_, _) = readLine().orEmpty()
        .trim()
        .split(' ')
        .map { i -> i.toInt() }

    val map = mutableMapOf<String, Int>()
    // read magazine
    readLine().orEmpty()
        .trim()
        .split(' ')
        .forEach { word ->
            map[word] = map[word]?.plus(1) ?: 1
        }

    // write ransom note
    readLine().orEmpty()
        .trim()
        .split(' ')
        .forEach { word ->

            if (map[word] == null || map[word] == 0) {

                println("No")
                return
            } else map[word] = map[word]!! - 1
        }

    println("Yes")
}