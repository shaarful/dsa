def swap(s: str, first_index: int, second_index: int):
    if first_index == second_index:
        return s
    if first_index < second_index:
        return s[:first_index] + s[second_index] + s[first_index + 1:second_index] + s[first_index] + s[
                                                                                                      second_index + 1:]
    return s[:second_index] + s[first_index] + s[second_index + 1:first_index] + s[second_index] + s[first_index + 1:]


def permute(s: str, left: int, right: int):
    if left == right:
        print(s)
        return
    for i, a in enumerate(s):
        s = swap(s, left, i)
        permute(s, left + 1, right)


txt = 'abc'
permute(txt, 0, len(txt) - 1)

# print(swap('abc', 1, 2))
