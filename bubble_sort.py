def bubble_sort(elements):
    size = len(elements)
    for i in range(size - 1):
        swapped = False
        for j in range(size - 1 - i):
            if elements[j] > elements[j + 1]:
                tmp = elements[j]
                elements[j] = elements[j + 1]
                elements[j + 1] = tmp
                swapped = True
        if not swapped:
            break


if __name__ == '__main__':
    nums = [32, 1, 53, 52, 12, 43, 64, 34, 33]
    bubble_sort(nums)
    print(nums)
