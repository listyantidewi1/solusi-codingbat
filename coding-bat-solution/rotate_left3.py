"""
Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}. 
rotate_left3([1, 2, 3]) → [2, 3, 1]
rotate_left3([5, 11, 9]) → [11, 9, 5]
rotate_left3([7, 0, 0]) → [0, 0, 7]

diberikan sebuah array integer dengan panjang = 3, kembalikan sebuah array baru dengan elemen "diputar ke kiri". Contoh: {1,2,3} menjadi {2,3,1}
"""


def rotate_left3(nums):
    # 1 2 3, diputar ke kiri menjadi 2 3 1
    # indeks 0, 1 , 2 diputar ke kiri menjadi 1, 2 , 0
    # indeks ke 1 bergeser ke kiri menempati posisi indeks ke 0. indeks ke 2 bergeser ke kiri menempati posisi indeks ke 1, indeks ke 0 berputar masuk ke posisi indeks terakhir
    return [nums[1], nums[2], nums[0]]
