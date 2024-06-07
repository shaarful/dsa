def merge_sort(elements):
    for i in range(1, len(elements)):
        anchor = elements[i]
        j = i - 1
        while j >= 0 and anchor < elements[j]:
            elements[j + 1] = elements[j]
            j -= 1
        elements[j + 1] = anchor


if __name__ == '__main__':
    numbers = [21, 12, 32, 24, 23, 22, 57, 16]
    merge_sort(numbers)
    print(numbers)
