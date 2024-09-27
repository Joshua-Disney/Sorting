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

print([12, 5, 3, 4, 2, 6, 7, 8])
# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    # loop through array
    # Figure out how to make this into a while.
    has_looped = True
    while has_looped:
        # Loop through rest of array
        has_looped = False
        print("Has looped: False 31")
        for i in range(0, len(arr) - 1):
            # Compare i to next in line through array
            print(f"{arr[i]}: {arr[i+1]}")
            if arr[i+1] < arr[i]:
                # if larger, switch places
                print(f"Moving {arr[i]} to the right of {arr[i+1]}")
                arr[i], arr[i+1] = arr[i+1], arr[i]
                has_looped = True
                print(f"{arr}, Has looped: True")
    # return array
    print(arr)
    return arr


bubble_sort([12, 5, 3, 4, 2, 6, 7, 8])

# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr
