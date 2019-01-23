// https://www.hackerrank.com/challenges/crush/problem

fun main(args: Array<String>) {

    val (_, qtyManipulations) = readLine().orEmpty()
        .trim()
        .split(' ')
        .map { i -> i.toInt() }


    val array = sortedMapOf<Int, Long>()
    for (i in 0 until qtyManipulations) {

        val (from, to, inc) = readLine().orEmpty()
            .trim()
            .split(' ')
            .map { n -> n.toLong() }
        array[from.toInt()] = array[from.toInt()]?.plus(inc) ?: inc
        array[to.toInt() + 1] = array[to.toInt() + 1]?.minus(inc) ?: -inc
    }

    var max = 0L
    var current = 0L

    array.forEach { k, value ->

        current += value
        if (current > max) max = current
    }

    println(max)
}
