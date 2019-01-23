import java.math.BigDecimal

fun main(args: Array<String>) {

    val (_, ratio) = readLine().orEmpty()
        .trim()
        .split(' ')
        .map(String::toInt)

    val singlets = mutableMapOf<Int, BigDecimal>()
    val doublets = mutableMapOf<Int, BigDecimal>()
    var qtyTriplets = BigDecimal.ZERO
    readLine().orEmpty()
        .trim()
        .split(' ')
        .map(String::toInt)
        .forEach {

            if (it % ratio == 0 && doublets.containsKey(it / ratio)) {
                qtyTriplets += doublets[it / ratio]!!
            }

            if (it % ratio == 0 && singlets.containsKey(it / ratio))  {
                doublets[it] = doublets.getOrDefault(it, BigDecimal.ZERO) + singlets[it / ratio]!!
            }

            singlets[it] = singlets.getOrDefault(it, BigDecimal.ZERO) + BigDecimal.ONE
        }

    println(qtyTriplets)
}
