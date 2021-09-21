"""
Given an array of ints length 3, return a new array with the elements in reverse order, so {1, 2, 3} becomes {3, 2, 1}. 

reverse3([1, 2, 3]) → [3, 2, 1]
reverse3([5, 11, 9]) → [9, 11, 5]
reverse3([7, 0, 0]) → [0, 0, 7]

Diberikan sebuah array (nums) bilangan bulat dengan panjang = 3 (jumlah elemen array = 3 buah), return sebuah array baru dengan elemen nums dalam urutan yang terbalik. Misal nums = {1,2,3}, menjadi nums = {3.2,1}

reverse3([1, 2, 3]) → [3, 2, 1]
reverse3([5, 11, 9]) → [9, 11, 5]
reverse3([7, 0, 0]) → [0, 0, 7]
"""


def reverse3(nums):
    # nums[::-1] digunakan untuk membalik urutan elemen array nums
    return nums[::-1]
