"""
Given 2 arrays of ints, a and b, return True if they have the same first element or they have the same last element. Both arrays will be length 1 or more. 
common_end([1, 2, 3], [7, 3]) → True
common_end([1, 2, 3], [7, 3, 2]) → False
common_end([1, 2, 3], [1, 3]) → True

Diberikan 2 array (himpunan) int (bilangan bulat), kembalikan nilai True jika elemen pertama atau elemen terakhir kedua array tersebut sama. Kedua array memiliki banyak elemen satu atau lebih
common_end([1, 2, 3], [7, 3]) → True
common_end([1, 2, 3], [7, 3, 2]) → False
common_end([1, 2, 3], [1, 3]) → True


"""

def common_end(a, b):
    # jika elemen pertama array a sama dengan elemen pertama array b -> a[0] == b[0]
    # jika elemen terakhir array a sama dengan elemen terakhir array b -> a[-1] == b[-1]
    # jika elemen pertama array a sama dengan elemen pertama array b ATAU jika elemen terakhir array a sama dengan elemen terakhir array b
    return a[0] == b[0] or a[-1] == b[-1]