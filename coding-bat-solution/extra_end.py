"""
Given a string, return a new string made of 3 copies of the last 2 chars of the original string.
The string length will be at least 2.
extra_end('Hello') → 'lololo'
extra_end('ab') → 'ababab'
extra_end('Hi') → 'HiHiHi'

Diberikan sebuah string, kembalikan sebuah string baru yang terdiri dari 3 salinan dari 2 karakter terakhir string asli. Panjang string minimal 2
extra_end('Hello') → 'lololo'
extra_end('ab') → 'ababab'
extra_end('Hi') → 'HiHiHi'
"""


def extra_end(str):
    # str[-2:] digunakan untuk mengambil dua karakter terakhir dari string str
    # *3 digunakan untuk menduplikasi string sebanyak 3 kali
    return str[-2:] * 3
