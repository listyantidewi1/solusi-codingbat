"""
Given an array of ints, return the sum of the first 2 elements in the array. If the array length is less than 2, just sum up the elements that exist, returning 0 if the array is length 0. 
sum2([1, 2, 3]) → 3
sum2([1, 1]) → 2
sum2([1, 1, 1, 1]) → 2

Diberikan sebuah array integer, kembalikan jummlah dari dua elemen pertama dari array tersebut. Jika panjang array kurang dari 2, maka jumlahkan elemen seadanya. Return 0 jika array memiliki panjang = 0 / tidak ada isinya
sum2([1, 2, 3]) → 3
sum2([1, 1]) → 2
sum2([1, 1, 1, 1]) → 2
"""


def sum2(nums):
    # return jumlah nums[0] + nums[1] jika len(nums) > 1, selain itu return sum(nums) jumlah seluruh elemen array nums
    return nums[0] + nums[1] if len(nums) > 1 else sum(nums)
