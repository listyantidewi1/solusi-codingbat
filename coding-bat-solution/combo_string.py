"""
Given 2 strings, a and b,
return a string of the form short+long+short,
with the shorter string on the outside and the longer string on the inside.
The strings will not be the same length, but they may be empty (length 0).
combo_string('Hello', 'hi') → 'hiHellohi'
combo_string('hi', 'Hello') → 'hiHellohi'
combo_string('aaa', 'b') → 'baaab'

Diberikan dua buah string a dan b
Kembalikan sebuah string dalam bentuk pendek+panjang+pendek, dengan string pendek berada di luar string panjang. String a dan b bisa jadi berbeda panjangnya, tapi bisa jadi juga kosong

combo_string('Hello', 'hi') → 'hiHellohi'
combo_string('hi', 'Hello') → 'hiHellohi'
combo_string('aaa', 'b') → 'baaab'
"""


def combo_string(a, b):
    # kembalikan b + a + b jika panjang a lebih dari panjang b
    # kembalikan a + b + a jika panjang b lebih dari panjang a
    panjang_a = len(a)
    panjang_b = len(b)
    if panjang_a > panjang_b:
        return b + a + b
    else:
        return a + b + a

    return b + a + b if len(a) > len(b) else a + b + a
