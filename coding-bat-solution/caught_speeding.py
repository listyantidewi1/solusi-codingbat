"""
You are driving a little too fast, and a police officer stops you. Write code to compute the result, encoded as an int value: 0=no ticket, 1=small ticket, 2=big ticket. If speed is 60 or less, the result is 0. If speed is between 61 and 80 inclusive, the result is 1. If speed is 81 or more, the result is 2. Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.
caught_speeding(60, False) → 0
caught_speeding(65, False) → 1
caught_speeding(65, True) → 0

Anda menyetir terlalu cepat, dan seorang polisi menghentikan anda. tulis kode program komputer untuk menghitung hasilnya dalam bilangan bulat. 0=tidak ditilang, 1 = tilang kecil, 2 = tilang besar. Jika kecepatan lebih kecil atau sama dengan 60, maka hasilnya adalah 0 (tidak ditilang). Jika kecepatan mengemudi adalah di antara 61 dan 80, maka hasilnya 1. Jika kecepatan lebih dari 80 maka hasilnya 2. Kecuali jika hari ini adalah hari ulang tahun anda, batas tilang Anda adalah 5 satuan lebih cepat dari biasanya.
"""


def caught_speeding(speed, is_birthday):

    if is_birthday:
        speed -= 5

    if speed <= 60:
        return 0

    return 1 if 61 <= speed <= 80 else 2