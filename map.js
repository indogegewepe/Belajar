/**
 * TODO:
 * 1. Buatlah variabel currency yang merupakan Map dengan kriteria:
 *   - key "USD", value 14000
 *   - key "JPY", value 131
 *   - key "SGD", value 11000
 *   - key "MYR", value 3500
 * 2. Buatlah variabel priceInIDR yang bernilai dari hasil perkalian:
 *     - priceInJPY dengan nilai currency JPY
 */

const priceInJPY = 5000;

// Tulis kode di bawah ini

const currency = new Map([
    ["USD", 14000],
    ["JPY", 131],
    ["SGD", 11000],
    ["MYR", 3500]
    ]);

    const priceInIDR = priceInJPY * currency.get("JPY");

    console.log(currency);
    console.log(priceInIDR);

    /* output
    Map(3) { '1' => 'a String key', 1 => 'a number key', true => true }
    */