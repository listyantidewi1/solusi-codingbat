"""
Given an array of ints length 3, figure out which is larger between the first and last elements in the array, and set all the other elements to be that value. Return the changed array. 
max_end3([1, 2, 3]) → [3, 3, 3]
max_end3([11, 5, 9]) → [11, 11, 11]
max_end3([2, 11, 3]) → [3, 3, 3]


Diberikan sebuah array berisi bilangan bulat dengan panjang array = 3. Tentukan mana yang lebih besar antara elemen pertama dan elemen terakhir array, lalu ubah nilai elemen array yang lain dengan nilai tersebut

max_end3([1, 2, 3]) → [3, 3, 3]
max_end3([11, 5, 9]) → [11, 11, 11]
max_end3([2, 11, 3]) → [3, 3, 3]

"""


def max_end3(nums):
    # duplikasi nilai nums[0] (nilai pertama array) sebanyak 3 kali jika nums[0] lebih dari atau sama denan nums[-1] (nilai terakhir array). Jika nilai nums[0] tidak lebih dari atau sama dengan nums[-1] maka duplikasi nums[-1] sebanyak 3 kali
    return [nums[0]] * 3 if nums[0] >= nums[-1] else [nums[-1]] * 3
