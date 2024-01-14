from util import time_it


@time_it
def linear_search(numbers: list, val):
    for idx, element in enumerate(numbers):
        if element == val:
            return idx
    return -1


@time_it
def binary_search(numbers: list, val):
    left_index = 0
    right_index = len(numbers) - 1
    mid_index = 0

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = numbers[mid_index]

        if mid_number == val:
            return mid_index

        if mid_number < val:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1

    return -1


def binary_search_recursive(numbers: list, val, left_index, right_index):
    if left_index > right_index or left_index < 0 or right_index >= len(numbers):
        return -1
    mid_index = (left_index + right_index) // 2
    mid_number = numbers[mid_index]

    if mid_number == val:
        return mid_index
    if mid_number < val:
        left_index = mid_index + 1
    else:
        right_index = mid_index - 1

    return binary_search_recursive(numbers, val, left_index, right_index)


if __name__ == '__main__':
    nums = [21, 43, 64, 86, 97]
    print(binary_search(range(100001), 100000))
    print(linear_search(range(100001), 100000))

    print(binary_search_recursive(nums, 8326, 0, len(nums)))
