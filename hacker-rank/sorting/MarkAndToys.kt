// https://www.hackerrank.com/challenges/mark-and-toys/problem

fun main(args: Array<String>) {

    val (_, budget) = readLine().orEmpty().trim().split(" ").map { num -> num.toInt() }
    val toys = readLine().orEmpty().trim().split(" ").map { num -> num.toInt() }.sorted()

    var sum = 0
    var qty = 0
    for (price in toys) {

        if (sum + price > budget) break
        else {
            qty++
            sum += price
        }
    }

    println(qty)
}