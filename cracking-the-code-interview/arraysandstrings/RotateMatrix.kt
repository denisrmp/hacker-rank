package arraysandstrings

/*
Question 1.7 Rotate Matrix
 */

fun rotate(matrix: Array<Array<Int>>): Array<Array<Int>> {

    // can rotate the matrix by layers
    // I don't care about the "remainder" layer in the case of an odd matrix
    // because it will be size 1 anyway and can't change by rotation
    val layers = matrix.size / 2
    for (layer in 0 until layers) rotateLayer(layer, matrix)
    return matrix
}

fun rotateLayer(layer: Int, matrix: Array<Array<Int>>) {

    val len = matrix.size - 1
    for (i in (0 + layer)..(len - layer - 1)) {

        val aux = matrix[layer][i]
        matrix[layer][i] = matrix[len - i][layer]
        matrix[len - i][layer] = matrix[len - layer][len - i]
        matrix[len - layer][len - i] = matrix[i][len - layer]
        matrix[i][len - layer] = aux
    }
}

fun main() {

    val test1 = arrayOf(arrayOf(1, 2, 3), arrayOf(4, 5, 6), arrayOf(7, 8, 9))
    println("original")
    printMatrix(test1)
    println("rotated")
    printMatrix(rotate(test1))
}

fun printMatrix(matrix: Array<Array<Int>>) {
    for (row in matrix) {
        for (column in row) {
            print(column)
        }
        println()
    }
}