// https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem

fun main() {

    val string = readLine().orEmpty()
    println(if (isValid(string)) "YES" else "NO")
}

fun isValid(string: String): Boolean {

    if (string.length <= 3) return true

    val charFreq = IntArray('z' - 'a' + 1)
    for (char in string) charFreq[char - 'a']++

    val metaFreq = mutableMapOf<Int, Int>()
    for (frequency in charFreq) {
        if (frequency != 0) metaFreq[frequency] = metaFreq.getOrDefault(frequency, 0) + 1
    }

    return when (metaFreq.keys.size) {
        1 -> true
        2 -> {
            val (first, second) = metaFreq.keys.toList()
            if ((first == 1 && metaFreq[first] == 1) || (second == 1 && metaFreq[second] == 1)) true
            else Math.abs(first - second) == 1 && (metaFreq[first] == 1 || metaFreq[second] == 1)
        }
        else -> false
    }
}
