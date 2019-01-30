package arraysandstrings

/*
pg. 90
1.3 URLify: Write a method to replace all spaces in a string with '20%'
 */

fun urlify(str: CharArray, len: Int): CharArray {

    var rawIdx = len - 1
    var urlIdx = str.size - 1
    while (rawIdx != urlIdx) {

        if (str[rawIdx] == ' ') {
            str[urlIdx--] = '0'
            str[urlIdx--] = '2'
            str[urlIdx--] = '%'
            rawIdx--
        } else {
            str[urlIdx--] = str[rawIdx--]
        }
    }

    return str
}

fun main() {

    val (test1Str, test1Size) = Pair("URLify Me!  ".toCharArray(), 10)
    val (test2Str, test2Size) = Pair("URLifyMeToo!".toCharArray(), 12)
    println("URLify str='${String(test1Str)}' into '${ String(urlify(test1Str, test1Size)) }'")
    println("URLify str='${String(test2Str)}' into '${ String(urlify(test2Str, test2Size)) }'")
}