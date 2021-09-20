"""
Given an array of ints, return True if 6 appears as either the first or last element in the array. The array will be length 1 or more. 
first_last6([1, 2, 6]) → True
first_last6([6, 1, 2, 3]) → True
first_last6([3, 2, 1]) → False

Diberikan sebuah array (himpunan), kembalikan true jika angka 6 muncul sebagai elemen pertama atau elemen terkhir pada array tersebut
first_last6([1, 2, 6]) → True
first_last6([6, 1, 2, 3]) → True
first_last6([3, 2, 1]) → False

"""

def first_last6(nums):
    #'in' digunakan untuk memeriksa apakah sebuah nilai berada di dalam array
    # nums[0] merujuk ke elemen array nums yang pertama
    # nums[1] merujuk ke elemen array nums yang terakhir
    return 6 in (nums[0], nums[-1])