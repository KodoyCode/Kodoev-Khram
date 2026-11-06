fun main() {
    val fruits = listOf("Apple", "Banana", "Apple")
    println(fruits[0])  
    println(fruits.size)


    val numbers = mutableListOf(1, 2, 3)
    numbers.add(4)
    numbers.removeAt(0)
    println(numbers)    
}