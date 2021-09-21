"""
Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".
first_half('WooHoo') → 'Woo'
first_half('HelloThere') → 'Hello'
first_half('abcdef') → 'abc'

Diberikan sebuah string dengan panjang genap. Return sebagian awal dari string tersebut
first_half('WooHoo') → 'Woo'
first_half('HelloThere') → 'Hello'
first_half('abcdef') → 'abc'
"""


def first_half(str):
    # fungsi str[] digunakan untuk mengambil beberapa huruf dari sebuah string str
    return str[:len(str) / 2]
    # untuk mengembalikan sebagian karakter pertama, maka diambil karakter pertama sebanyak panjang string / 2
