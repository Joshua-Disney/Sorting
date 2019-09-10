# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(cur_index+1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # TO-DO: swap
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr


selection_sort([1, 5, 3, 2, 4, 2, 6, 8, 7])

print([12, 5, 3, 2, 4, 2, 6, 8, 7])
# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    # loop through array
    for i in range(0, len(arr) - 1):
        # assign i to current index
        cur_index = i
        # Loop through rest of array
        for j in range(0, len(arr) - 1):
                # Compare i to next in line through array
            print(f"{arr[j]}: {arr[j+1]}")
            if arr[j+1] < arr[j]:
                # if larger, switch places
                print(f"Moving {arr[j]} to the right of {arr[j+1]}")
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print(arr)
    # return array
    print(arr)
    return arr


bubble_sort([12, 5, 3, 2, 4, 2, 6, 8, 7])

# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr
