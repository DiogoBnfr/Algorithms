def insertion_sort(list: list) -> list:
        for i in range(1, len(list)):
                while (i > 0):
                        if (list[i] < list[i - 1]):
                                list[i], list[i - 1] = list[i - 1], list[i]
                                swap_count += 1
                                i -= 1
                        else:
                                break
        return list

list = [7, 3, 1, 6, 4, 2]
print(*insertion_sort(list), sep=', ')