"""
Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their middle elements. 
middle_way([1, 2, 3], [4, 5, 6]) → [2, 5]
middle_way([7, 7, 7], [3, 8, 0]) → [7, 8]
middle_way([5, 2, 9], [1, 4, 5]) → [2, 4]

Diberikan 2 buah array bilangan bulat, a dan b. Masing-masing array memiliki panjang = 3. Kembalikan sebuah array baru yang berisi masing-masing elemen tengah dari array a dan b.
middle_way([1, 2, 3], [4, 5, 6]) → [2, 5]
middle_way([7, 7, 7], [3, 8, 0]) → [7, 8]
middle_way([5, 2, 9], [1, 4, 5]) → [2, 4]

"""


def middle_way(a, b):
    # elemen tengah dari sebuah array n dengan panjang = 3 adalah n[1]
    # elemen tengah array a jika panjang array = 3 adalah a[1]
    # elemen tengah array b jika panjang array = 3 adalah a[1]
    # return [] artinya mengembalikan sebuah array baru
    # return [a[1], b[1]] artinya mengembalikan sebuah array baru berisi elemen tengah array a dan b
    return [a[1], b[1]]
