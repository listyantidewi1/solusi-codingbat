"""
You and your date are trying to get a table at a restaurant. The parameter "you" is the stylishness of your clothes, in the range 0..10, and "date" is the stylishness of your date's clothes. The result getting the table is encoded as an int value with 0=no, 1=maybe, 2=yes. If either of you is very stylish, 8 or more, then the result is 2 (yes). With the exception that if either of you has style of 2 or less, then the result is 0 (no). Otherwise the result is 1 (maybe).
date_fashion(5, 10) → 2
date_fashion(5, 2) → 0
date_fashion(5, 5) → 1

Anda dan pacar anda ingin memesan meja di restaurant. Parameter "you" adalah tingkat ke-stylish-an pakaian anda, dalam jangkauan 0..10, dan "date" adalah tingkat ke-stylish-an pakaian pacar Anda. Hasil kesuksesan pemesanan meja dinyatakan dalam bilangan bulat, yaitu 0 = gagal, 1 = mungkin, 2 = berhasil. Jika anda atau pacar anda sangat stylish, dibuktikan dengan tingkat stylish >= 8, maka hasil pemesanan meja adalah 2. Jika salah satu dari anda atau pacar anda tingkat stylish-nya adalah <= 2, maka anda gagal memesan meja (0). Selain itu, pemesanan meja mungkin berhasil (1)
date_fashion(5, 10) → 2
date_fashion(5, 2) → 0
date_fashion(5, 5) → 1

"""


def date_fashion(you, date):
    if you <= 2 or date <= 2:
        return 0

    if you >= 8 or date >= 8:
        return 2

    return 1