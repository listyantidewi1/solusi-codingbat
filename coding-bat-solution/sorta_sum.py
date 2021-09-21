"""
Given 2 ints, a and b, return their sum. However, sums in the range 10..19 inclusive, are forbidden, so in that case just return 20.
sorta_sum(3, 4) → 7
sorta_sum(9, 4) → 20
sorta_sum(10, 11) → 21

Diberikan 2 bilangan bulat (int) a dan b. Kembalikan nilai a+b, kecuali jika jumlah  a+b antara 10 .. 19, maka return 20

"""


def sorta_sum(a, b):
    total = a + b  # hitung a + b, simpan hasilnya ke variabel total
    # kembalikan 20 jika hasil a + b lebih dari sama dengan 10 dan kurang dari saa dengan 19
    return 20 if 10 <= total <= 19 else total
