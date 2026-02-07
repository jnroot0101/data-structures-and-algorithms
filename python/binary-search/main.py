def binary_search(arr, target):
    """
    This function takes in a sorted array and a target value. It returns the index of the
    target value if it is present in the array.
    Otherwise, it returns None.
    :param arr:
    :param target:
    :return:
    """

    # low and high keep track of which part of the list you'll search in
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2 # median
        guess = arr[mid]

        if guess == target:
            return mid
        elif guess > target:
            high = mid - 1
        else:
            low = mid + 1

    return None



print(binary_search([1, 2, 3, 4, 5, 6], 3))

