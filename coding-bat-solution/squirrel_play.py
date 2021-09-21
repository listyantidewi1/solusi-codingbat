"""
The squirrels in Palo Alto spend most of the day playing. In particular, they play if the temperature is between 60 and 90 (inclusive). Unless it is summer, then the upper limit is 100 instead of 90. Given an int temperature and a boolean is_summer, return True if the squirrels play and False otherwise.
squirrel_play(70, False) → True
squirrel_play(95, False) → False
squirrel_play(95, True) → True

Tupai2 di Palo ALto menghabiskan sebagian besar harinya dengan bermain. Mereka bermain jika suhu/temperature udara antara 90 dan 90. Kecuali pada musim panas, maka batas atas suhu dimana mereka bermain adalah 100. Diberikan sebuah nilai int dan sebuah boolean "is_summer", kembalikan True jika tupai2 bermain, dan false jika tupai2 tidak bermain

squirrel_play(suhu, is_summer)

squirrel_play(70, False) → True
squirrel_play(95, False) → False
squirrel_play(95, True) → True
"""


def squirrel_play(temp, is_summer):
    return 60 <= temp <= (100 if is_summer else 90)
