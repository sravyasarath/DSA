"""
This script takes a sorted array of integers (which may include negative numbers) and returns
a new array with the squares of each number, also sorted in non-decreasing order.

How it works:
- Uses a two-pointer technique: one pointer at the start, one at the end of the array.
- Compares the absolute values at both ends, places the larger square at the end of the result array.
- Efficiently builds the sorted squared array in O(n) time.

Example:
Input: [-11, 2, 3, 4]
Output: [4, 9, 16, 121]
"""


def sorted_squared_array(array):
    n=len(array)
    i=0
    j=n-1
    result_array=[0]*n
    print(result_array)
    for k in reversed(range(n)):
        if array[i]**2>array[j]**2:
            result_array[k]=array[i]**2
            i=i+1
        else:
            result_array[k]=array[j]**2
            j=j-1
    print(result_array)       


sorted_squared_array([-11,2,3,4])

