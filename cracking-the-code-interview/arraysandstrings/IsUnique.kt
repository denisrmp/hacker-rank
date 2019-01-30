package arraysandstrings

/*
pg. 90
1.1 Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?
*/

fun isAllUnique(string: String): Boolean {

    val chars = mutableSetOf<Char>()
    string.forEach { c ->
        if (chars.contains(c)) return false
        else chars.add(c)
    }

    return true
}

fun isAllUniqueNoDS(string: String): Boolean {

    for (i in 0 until string.length - 1) {
        for (j in i + 1 until string.length) {
            if (string[i] == string[j]) return false
        }
    }

    return true
}

fun main() {

    println("assadas isAllUnique=${isAllUnique("assadas")}")
    println("qwerty isAllUnique=${isAllUnique("qwerty")}")

    println("assadas isAllUniqueNoDS=${isAllUniqueNoDS("assadas")}")
    println("qwerty isAllUniqueNoDS=${isAllUniqueNoDS("qwerty")}")
}
