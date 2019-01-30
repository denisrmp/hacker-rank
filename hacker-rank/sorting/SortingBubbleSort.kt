
fun main(args: Array<String>) {

    readLine() // Ignore first line (size of array)
    val array = readLine().orEmpty().trim().split(" ").map { num -> num.toInt() }.toMutableList()

    var qtySwaps = 0
    for (i in 0 until array.size) {
        var itSwaps = 0
        for (j in 0 until array.size - 1) {
            if (array[j] > array[j + 1]) {
                val aux = array[j]
                array[j] = array[j + 1]
                array[j + 1] = aux

                itSwaps++
            }
        }

        if (itSwaps == 0) break
        else qtySwaps += itSwaps
    }

    println("Array is sorted in $qtySwaps swaps.")
    println("First Element: ${array[0]}")
    println("Last Element: ${array.last()}")
}