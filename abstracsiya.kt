// open class bilan nima noto‘g‘ri?

open class Shakl(val nomi: String) {
    open fun yuza(): Double = 0.0 // ???
}

class Kvadrat(val a: Double) : Shakl("Kvadrat")

// Override yozish esdan chiqdi!

println(Shakl("Nimadir").yuza())
println(Kvadrat(4.0).yuza())

// Natija:
    // 0.0
    // 0.0 

// 1-muammo
    // «Shunchaki shakl» obyektini yaratish mumkin — lekin

// 2-muammo
    // override unutilsa, kompilyator jim turadi — kvadrat yuzasi 0 bo‘lib qoladi.




// abstrakt class - umumiy shablon

abstrakt class Shakl(val nomi: String) {
    abstrakt fun yuza(): Double // tanasi yoq!
    fun malumot() = println("$nomi: yuzasi ${yuza()}")

}

class Kvadrat(val a: Double) : Shakl("Kvadrat") {
    override fun yuza() = a * a
}

class Doira(val r: Double) : Shakl("Doira") {
    override fun yuza() = 3.14 * r * r
}
Kvadrat(4.0).malumot()
Doira(2.0).malumot()

// Natija:
    // Kvadrat: yuzasi 16.0
    // Doira: yuzasi 12.56

// abstract fun
    // Faqat nomi va turi — tanasi yo‘q. «Har bir bola sinf o‘zi 

// fun malumot()
    // Oddiy funksiyalar ham bo‘lishi mumkin — ula




// interface — «nima qila oladi?»

interface Uchuvchi {
    fun Uch() //faqat va'da
}

class Qush : Uchuvchi {
    override fun uch() {
        println("Qanot qoqip uchyapman")
    }
}

class Samolyot : Uchuvchi {
    override fun uch() {
        println("Dvigatel bilan uchyapman")
    }
}

// Haydovchilik guvohnomasi
    // Kim bo‘lishingdan qat’i nazar — guvohnoma bor bo‘lsa, haydashni biladi. Interfeys ham shunday «qobil

// Qush va samolyot
    // «Qarindosh» emas, lekin ikkalasi ham ucha

// class Qush : Uchuvchi
    // Interfeys nomidan keyin qavs yo‘q — interfeysning konstruktori bo‘lmaydi.




// Ota - bitta, qobiliyatlar - kop

interface Suzuvchi {
    fun Suz() {
        println("Suzayapman") // tayyor kod
    }
}

open class Hayvon(val ism: String)

class Ordak : Hayvon("O'rdak"), Uchuvchi, Suzuvchi {
    override fun uch() {
        println("$ism uchyapti")
    }
}

val o = Ordak()
o.uch()
o.suz()

// Natija:
    // O‘rdak uchyapti
    // Suzyapman

// Faqat 1 ta sinf
    // Meros faqat bitta sinfdan olinadi (qavs bilan).

// Istalgancha interfeys
    // Interfeyslar vergul bilan ko‘p bo‘lishi mumkin.




// Kim bo'lsang ham - uch!

val uchuvchilar: List<Uchuvchi> = listOf(
    Qush(), Samolyot(), Ordak()
)

for (u in uchuvchilar) {
    u.uch()
}

// Natija:
    // Qanot qoqib uchyapman
    // Dvigatel bilan uchyapman
    // O‘rdak uc

// Qush, samolyot va o‘rdakning umumiy otasi yo‘q, lekin ularni bitta List<Uchuvchi> ga yig‘a olamiz — chunki ularning hammasi «ucha oladi».




// abstract class yoki interface?
//                              | abstract class                | interface
// Savol                        | «U kim?» (It — bu Hayvon)     | «U nima qila oladi?» (Qush — ucha oladi)
// Meros                        | Faqat bitta sinfdan           | Istalgancha interfeys
// Konstruktor                  | Bor: Shakl(nomi)              | Yo‘q — qavssiz yoziladi
// Holat (qiymatli xususiyat)   | Saqlay oladi: val nomi        | Saqlay olmaydi
// Tayyor kodli funksiya        | Bo‘lishi mumkin               | Bo‘lishi mumkin
// Obyekt yaratish              | Mumkin emas                   | Mumkin emas
//              ||||||||||||
//              ||||||||||||
//              ||||||||||||
//              ||||||||||||
//              ||||||||||||
//              ||||||||||||
//              ||||||||||||
//              ||||||||||||
//              ||||||||||||
//              ||||||||||||
//              ||||||||||||
//              ||||||||||||
//              ||||||||||||
//              ||||||||||||
//              ||||||||||||
//              ||||||||||||
//              ||||||||||||
//              ||||||||||||
//              ||||||||||||
//              ||||||||||||