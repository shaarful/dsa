def merge_sort(elements):
    if len(elements) <= 1:
        return elements
    mid = len(elements) // 2
    left = merge_sort(elements[:mid])
    right = merge_sort(elements[mid:])
    return merge_two_list(left, right)


def merge_two_list(left, right):
    sorted_list = []
    left_len = len(left)
    right_len = len(right)
    i = j = 0
    while i < left_len and j < right_len:
        if left[i] <= right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    while i < left_len:
        sorted_list.append(left[i])
        i += 1
    while j < right_len:
        sorted_list.append(right[j])
        j += 1

    return sorted_list


if __name__ == '__main__':
    numbers = [21, 12, 32, 24, 23, 22, 57, 16]
    print(numbers)
    print(merge_sort(numbers))
