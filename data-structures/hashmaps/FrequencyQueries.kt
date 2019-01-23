import java.lang.StringBuilder

fun main(args: Array<String>) {

    val queries = readLine().orEmpty().trim().toInt()
    val map = HashMap<Int, Int>()
    val frequencies = HashMap<Int, Int>()
    val inputs = Array(queries) {
        val (operation, value) = readLine().orEmpty()
            .split(" ")
            .map { n -> n.toInt() }
        intArrayOf(operation, value)
    }

    val sb = StringBuilder()
    inputs.forEach {
        val value = it[1]
        when (it[0]) {
            1 -> {
                frequencies.merge(map[value] ?: 0, 0) { oldValue, _ -> Math.max(oldValue - 1, 0) }
                map.merge(value, 1) { oldValue, _ -> oldValue + 1 }
                frequencies.merge(map[value] ?: 0, 1) { oldValue, _ -> Math.max(oldValue + 1, 0) }
            }
            2 -> {
                frequencies.merge(map[value] ?: 0, 0) { oldValue, _ -> Math.max(oldValue - 1, 0) }
                map.merge(value, 0) { oldValue, _ -> Math.max(oldValue - 1, 0) }
                frequencies.merge(map[value] ?: 0, 1) { oldValue, _ -> Math.max(oldValue + 1, 0) }
            }
            3 -> if (frequencies.getOrDefault(value, 0) > 0) sb.append("1\n") else sb.append("0\n")
        }
    }

    print(sb)
}