
fun main() {

    readLine() // ignore first input
    val str = readLine().orEmpty()

    var count = 0L
    val freqTable = buildFreqTable(str)

    // all singles
    for (freq in freqTable) count += triangleNumber(freq.second)

    // all "middle" cases
    for (i in 0 until freqTable.size - 2) {

        if (freqTable[i + 1].second == 1 && freqTable[i].first == freqTable[i + 2].first) {

            count += Math.min(freqTable[i].second, freqTable[i + 2].second)
        }
    }

    println(count)
}

private fun buildFreqTable(str: String): List<Pair<Char, Int>> {

    if (str.length == 1) return listOf(Pair(str[0], 1))

    val table = mutableListOf<Pair<Char, Int>>()
    var lastChar = str[0]
    var count = 1
    for (i in 1 until str.length) {

        if (str[i] == lastChar) count++
        else {
            table.add(Pair(lastChar, count))
            lastChar = str[i]
            count = 1
        }
    }

    table.add(Pair(lastChar, count))
    return table
}

private fun triangleNumber(n: Int) = (n * (n + 1L)) / 2L
