package arraysandstrings

/*
1.8 Write and algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.

input
1 2 3
4 5 6
7 8 9

expected
1 2 3
4 5 6
7 8 9

---

input
1 2 0
0 5 6
7 8 9

expected
0 0 0
0 0 0
0 8 0
 */

fun main() {
    // TODO write more tests
    test1()
    test2()
}

fun test1() {

    val matrix = arrayOf(intArrayOf(1, 2, 3), intArrayOf(4, 5, 6), intArrayOf(7, 8, 9))
    val expected = arrayOf(intArrayOf(1, 2, 3), intArrayOf(4, 5, 6), intArrayOf(7, 8, 9))
    zeroMatrix(matrix)
    if (!matrix.contentDeepEquals(expected)) throw AssertionError("Test 1 failed")
    println("test1 OK")
}

fun test2() {

    val matrix = arrayOf(intArrayOf(1, 2, 0), intArrayOf(0, 5, 6), intArrayOf(7, 8, 9))
    val expected = arrayOf(intArrayOf(0, 0, 0), intArrayOf(0, 0, 0), intArrayOf(0, 8, 0))
    zeroMatrix(matrix)
    if (!matrix.contentDeepEquals(expected)) throw AssertionError("Test 2 failed")
    println("test2 OK")
}

fun zeroMatrix(matrix: Array<IntArray>) {

    val zeroRows = mutableSetOf<Int>()
    val zeroCols = mutableSetOf<Int>()
    matrix.forEachIndexed { rowIndex, row ->
        row.forEachIndexed { colIndex, cell ->
            if (cell == 0) {
                zeroRows.add(rowIndex)
                zeroCols.add(colIndex)
            }
        }
    }

    matrix.forEachIndexed { rowIndex, row ->
        row.forEachIndexed { colIndex, _ ->
            if (zeroRows.contains(rowIndex) || zeroCols.contains(colIndex)) {
                matrix[rowIndex][colIndex] = 0
            }
        }
    }
}