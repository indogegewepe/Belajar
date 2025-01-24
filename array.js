// * TODO:
// * Buatlah sebuah variabel dengan nama evenNumber yang merupakan sebuah array dengan ketentuan:
// *   - Array tersebut menampung bilangan genap dari 1 hingga 100
// *
// * Catatan:
// *   - Agar lebih mudah, gunakanlah for loop dan logika if untuk mengisi bilangan genap pada array.
// */

// Tulis kode di bawah ini

let evenNumber = [];

let j = 0;

for (var i = 1; i <= 100; i++) {
    if (i % 2 == 0) {
      evenNumber[j] = i;
    	j++;
    }
}

for (var i = 0; i < 50; i++) {
    console.log(evenNumber[i]);
}