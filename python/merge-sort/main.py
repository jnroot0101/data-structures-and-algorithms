def merge_sort(nums):
    if len(nums) < 2:
        return nums

    # Split the input array into two halves down the middle
    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])

    return merge(left, right)


def merge(left, right):
    final = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            final.append(left[i])
            i += 1
        else:
            final.append(right[j])
            j += 1

    # After comparing all the items, there may be some items left over in either left or right.
    while i < len(left):
        final.append(left[i])
        i += 1

    while j < len(right):
        final.append(right[j])
        j += 1

    return final
