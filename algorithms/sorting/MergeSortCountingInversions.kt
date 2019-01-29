import java.lang.StringBuilder

private fun IntArray.toNiceString(): String {

    val sb = StringBuilder().append("[")
    this.forEach { sb.append(it).append(",") }
    if (sb.length > 1) sb.deleteCharAt(sb.lastIndex).append("]")
    return sb.toString()
}

private val IntRange.size: Int
    get() = this.last - this.first

private val IntRange.half: Int
    get() = this.first + (this.size / 2)

fun main() {

    val queries = readLine().orEmpty().trim().toInt()
    val arrays =  Array(queries) {
        readLine() // ignore first line
        readLine().orEmpty().trim().split(" ").map { l -> l.toInt() }.toIntArray()
    }

    arrays.forEach {
        println(countSwaps(it))
    }
}

fun countSwaps(array: IntArray): Long {

    return sort(array, 0 .. array.size, IntArray(array.size))
}

fun sort(array: IntArray, range: IntRange, temp: IntArray): Long {

    if (range.size <= 1) return 0
    val leftHalf = range.first .. range.half
    val rightHalf = range.half .. range.last
    return sort(array, leftHalf, temp) + sort(array, rightHalf, temp) + merge(array, leftHalf, rightHalf, temp)
}

fun merge(array: IntArray, leftHalf: IntRange, rightHalf: IntRange, temp: IntArray): Long {

    var left = leftHalf.first
    var right = rightHalf.first
    var index = left
    var swaps = 0L
    while (left < leftHalf.last && right < rightHalf.last) {

        if (array[left] <= array[right]) temp[index] = array[left++]
        else {
            swaps += right - index
            temp[index] = array[right++]
        }
        index++
    }

    while (left < leftHalf.last) temp[index++] = array[left++]
    while (right < rightHalf.last) temp[index++] = array[right++]
    for (i in leftHalf.first until rightHalf.last) array[i] = temp[i]
    return swaps
}
