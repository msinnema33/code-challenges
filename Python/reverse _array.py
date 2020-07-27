# Given an array

# Print in reverse order each on a new line

arr = [10, 9, 8, -7, 6, 5, 4, 3, 2, 1, 0]

# make my function
# arr is a list of integers
def reverse(arr):
    # rev_arr = list.reversed(arr)  if array/list is alredy sorted doean't matter asc/desc
    rev_arr = arr[::-1] # us if not sorted or order is unknown.
    # arr.sort(reverse = True) #same as  the line above
    for i in rev_arr: # for i in arr
        print (i)

reverse(arr)