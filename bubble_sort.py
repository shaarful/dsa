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


def bubble_dict_sort(elements, key=None):
    size = len(elements)
    for i in range(size - 1):
        swapped = False
        for j in range(size - 1 - i):
            if elements[j][key] > elements[j + 1][key]:
                tmp = elements[j]
                elements[j] = elements[j + 1]
                elements[j + 1] = tmp
                swapped = True
        if not swapped:
            break


if __name__ == '__main__':
    nums = [32, 1, 53, 52, 12, 43, 64, 34, 33]
    bubble_sort(nums)
    # print(nums)

    elmts = [
        {'name': 'mona', 'transaction_amount': 1000, 'device': 'iphone-10'},
        {'name': 'dhaval', 'transaction_amount': 400, 'device': 'google pixel'},
        {'name': 'kathy', 'transaction_amount': 200, 'device': 'vivo'},
        {'name': 'aamir', 'transaction_amount': 800, 'device': 'iphone-8'},
    ]

    bubble_dict_sort(elmts, 'transaction_amount')
    print(elmts)

