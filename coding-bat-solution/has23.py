"""
Given an int array length 2, return True if it contains a 2 or a 3. 
has23([2, 5]) → True
has23([4, 3]) → True
has23([4, 5]) → False

diberikan sebuah array dengan panjang = 2 (jumlah elemen array-nya 2). Kembalikan nilai true jika array tersebut mengandung angka 2 atau angka 3
has23([2, 5]) → True
has23([4, 3]) → True
has23([4, 5]) → False
"""

def has23(nums):
    # 2 in nums -> jika ada angka 2 dalam array nums
    # 3 in nums -> jika ada angka 3 dalam array nums
    # 2 in nums or 3 in nums -> jika ada angka 2 di dalam array nums ATAU jika ada angka 3 di dalam array nums
    return 2 in nums or 3 in nums