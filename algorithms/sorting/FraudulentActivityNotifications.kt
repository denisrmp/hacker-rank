
fun main() {

    val (_, days) = readLine().orEmpty().trim().split(" ").map(String::toInt)
    val expenditures = readLine().orEmpty().trim().split(" ").map(String::toInt).toTypedArray()
    fraudulentActivityNotifications(days, expenditures)
}

fun fraudulentActivityNotifications(days: Int, expenditures: Array<Int>) {

    val countArray = IntArray(200)
    var qty = 0

    // initialize
    for (i in 0 until days) {
        countArray[expenditures[i]]++
    }

    for (i in days until expenditures.size) {

        if (expenditures[i] >= median(days, countArray)) qty++
        countArray[expenditures[i - days]]--
        countArray[expenditures[i]]++
    }

    println(qty)
}

fun median(days: Int, countArray: IntArray): Int {

    var count = 0
    val even = days % 2 == 0
    val medianIdx = days / 2
    var foundFirst = false
    var median = 0
    for (countIdx in 0 until countArray.size) {

        count += countArray[countIdx]
        if (!even) {
            if (count > medianIdx) {

                median = countIdx * 2
                break
            }
        } else {

            if (countArray[countIdx] > 0 && count == medianIdx) {

                median = countIdx
                foundFirst = true
            } else if (countArray[countIdx] > 0 && count > medianIdx) {

                if (foundFirst) median += countIdx
                else median = countIdx * 2
                break
            }
        }
    }

    return median
}

