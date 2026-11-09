fun main() {
    val fruits = listOf("Apple", "Banana", "Apple")
    println(fruits[0])  
    println(fruits.size)


    val numbers = mutableListOf(1, 2, 3)
    numbers.add(4)
    numbers.removeAt(0)
    println(numbers)    

    
    val kvadrat = {x: Int -> x * x}
    println(kvadrat(5)) //25

    val ikkilash: (Int) -> Int = { it * 2 }
    println(ikkilash(7)) //14

    val salom = { ism: String -> "Salom, %ism!" }
    println(salom("Ali")) // Salom, ali!


    //forEach and filter
    val sonlar = listOf(1, 2, 3, 4, 5, 6)
    sonlar.forEach { println(it) }

    val juft = sonlar.filter { it % 2 == 0 }
    println(juft) // [2, 4, 6]
    println(sonlar.count { it > 3 }) // 3
    println(sonlar.any { it > 5 }) // true

    val narxlar = mapOf("Laptop" to 1200.00, "Phone" to 800.00, "Watch" to 250.00)
    println(narxlar.filter { it.value > 500 }) // {Laptop=1200.00, Phone=800.00}


    // Map
    val nomlar = listOf("ali", "vali", "gulnora")
    println(nomlar.map { it.uppercase()})  // [ALI, VALI, GULNORA]

    val sonlar = listOf(1, 2, 3, 4, 5, 6)
    println(sonlar.map { it * it }) // [1, 4, 9, 16, 25, 36]

    val jami = sonlar.filter { it > 2 }.map { it * 10 }.sum()
    println(jami) // 180
}