"""
Given a number n, return True if n is in the range 1..10, inclusive. Unless "outsideMode" is True, in which case return True if the number is less or equal to 1, or greater or equal to 10.
in1to10(5, False) → True
in1to10(11, False) → False
in1to10(11, True) → True

Diberikan sebuah bilangan n. Kembalikan true jika n memiliki nilai 1 sampai 10 (1..10), kecuali jika "outSideMode" bernilai True. Jika "outSideMode" bernilai true, maka kembalikan True jika nilai lebih kecil atau sama dengan 1, atau lebih besar atau ssama dengan 10.

in1to10(5, False) → True
in1to10(11, False) → False
in1to10(11, True) → True
"""


def in1to10(n, outside_mode):
    if outside_mode:  # jika outside_mode
        return n <= 1 or n >= 10  # kembalikan true jika n <=1 atau n >= 10
    return 1 <= n <= 10  # jika bukan outside_mode kembalikan true jika n di antara 1 sampai 10
