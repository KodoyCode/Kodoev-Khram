

//Null - "qiymat yoq"

//Bosh quti: ozgaruvchi quti. Null - qutining ichida hech narsa yoq. 0 ham emas, bo'sh matn "" ham emas - umuman yoq.


//Anketa 

//"Uy telefoni: ___" - ko'pchilikda uy telefoni yo'q. Bu maydon to'ldirilmagan - u null.


//Siz allaqachon ko‘rgansiz

//ballar["Bobur"] --> null

//sonlar.find { it > 100} --> null


//Nega xavfli? Bo'sh qutidan narsa olmoqchi bo'lsak, dastur NullPointerException xatosi bilan yopiladi. Java va boshqa tillarda bu ilovalar "qulashi"ning wng ko'p uchraydigan sabablaridan biri.




//Savol belgisi hamma narsani hal qiladi


//var ism: String  = "Aziz"

//ism = null        // HATO!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


//var telefon: Stirng? = "998901234567"

//telefon = null // MUMKIN!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


//String

//hech qacho null bolmaydi. kotlin bunga kafolat beradi - xotirjam ishlatish mumkin.


//String?

//null bo'lishi mumkin. Ishlatishdan oldin Kotlin sizni tekshirishga majbur qiladi.


//Har qanday turga "?" qo'shsa bo'ladi: Int?, Double?, Boolean?, Oquvchi?. Birinchi qatordagi xato: Null can not be a value of a non-null type String.




//"String?" ni to‘g‘ridan-to‘g‘ri ishlatib bo‘lmaydi.


//val telefon: String? = Null

//println(telefon.length)       // KOMPILYATOR RUXSAT BERMAYDI!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


//Android Studio xabari:

//Only safe (?.) or non-null asserted (!!.) calls are allwed on a nullable receiver of type String?


//Kotlin aytyapti: "Bu quti bosh bo'lishi mumkin!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Avval tekshir." Buning uchun to'rtta usul bor: if, ?., ?: va !! - ularni birma-bir ko'ramis.




//if bilan tekshirish


//val telefon: String? = null

//if (telefon != null) {

//    println("Uzunligi: ${telefon.length")

//} else {

//    println("Telefon raqami yo'q.")

//}


//Natija: telefon raqami yo'q


//Kotlin aqlli

//<strong>if</strong> ichida Kotlin biladiki, telefon null emas - shuning uchun u yerda telefon.length xatosiz ishlaydi.




