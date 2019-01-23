
fun main(args: Array<String>) {

    val queries = readLine().orEmpty().trim().toInt()
    (0 until queries).forEach {

        val a = readLine().orEmpty().trim()
        println(countAnagrams(a))
    }
}

fun countAnagrams(chars: String): Int {

    val map = HashMap<String, Int>()
    for (setSize in 1 until chars.length) {
        for (i in 0..chars.length - setSize) {

            val key = String(chars.substring(i, i + setSize).toCharArray().sortedArray())
            map[key] = map.getOrDefault(key, 0) + 1
        }
    }

    return map.values.map { (it * (it - 1))/2 }.sum()
}
