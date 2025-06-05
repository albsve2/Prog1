a = [1, 2, 6, 4, 5, 0, 1, 2]


def smooth_a(a, n):  # lista a, heltal n
    lst = []  # ny lista
    for i in range(len(a)):
        start = max(0, i - n)  # inne i listan till vänster
        end = min(len(a), i + n + 1)  # inne i listan till höger

        left = [a[0]] * max(0, n - i)  # utanför till vänster
        right = [a[-1]] * max(0, n - (len(a) - 1 - i))  # utanför till höger

        x = left + a[start:end] + right  # tillfällig lista x
        lst.append(sum(x) / len(x))

    return lst


def smooth_b(a, n):
    list = []
    for i in range(len(a)):
        start = max(0, i - n)
        end = min(len(a), i + n + 1)
        x = a[start:end]  # del av listan a
        list.append(sum(x) / len(x))

    return list


def round_list(list, ndigits):
    return [round(a, ndigits) for a in list]


# print(smooth_a(a, 1))
# print(smooth_a(a, 2))
# print(smooth_b(a, 1))
# print(smooth_b(a, 2))
# print(round_list(smooth_a(a, 1), 2))
# # print(round_list(smooth_b(a, 1), 2))
