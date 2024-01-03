expense = [2200, 2350, 2600, 2130, 2190]


def expense_till_month(month_no):
    total_exp = 0
    for month in range(month_no):
        total_exp += expense[month]
    return total_exp


odd_list = []

if __name__ == '__main__':
    print(f"Feb extra expense: ", expense[1] - expense[0])
    print(f"first quarter Total expense: ", expense_till_month(3))

    max_num = input("Enter Max Number: ")

    for i in range(1, int(max_num)):
        if i % 2: odd_list.append(i)

    print(odd_list)
