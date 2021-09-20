"""
Given an array of ints, return a new array length 2 containing the first and last elements from the original array. The original array will be length 1 or more. 
make_ends([1, 2, 3]) → [1, 3]
make_ends([1, 2, 3, 4]) → [1, 4]
make_ends([7, 4, 6, 2]) → [7, 2]

Diberikan sebuah array integer, kembalikan sebuah array baru yang berisi elemen pertama dan elemen terakhir dari array asli.
make_ends([1, 2, 3]) → [1, 3]
make_ends([1, 2, 3, 4]) → [1, 4]
make_ends([7, 4, 6, 2]) → [7, 2]

"""

def make_ends(nums):
    # [nums[0], nums[1]] -> mengambil nilai pertama dan nilai terakhir dari array nums dan memasukkannya ke dalam sebuah array baru
    return [nums[0], nums[-1]]