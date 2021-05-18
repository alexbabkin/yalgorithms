
def get_one_length(lst):
    one_length = 0
    lengths = []
    for elem in lst + [0]:
        if elem == 1:
            one_length += 1
        else:
            lengths.append(one_length)
            one_length = 0
    return lengths


def calc_max_one_length(lst):
    one_lengths = get_one_length(lst)
    if len(one_lengths) == 1:
        return one_lengths[0] - 1
    else:
        i = 0
        max_length = 0
        while i < len(one_lengths) - 1:
            if one_lengths[i] + one_lengths[i+1] > max_length:
                max_length = one_lengths[i] + one_lengths[i+1]
            i += 1
        return max_length


lst = [0, 1, 0]
print(str(lst) + " -> " + str(calc_max_one_length(lst)))

lst = [1, 1, 1]
print(str(lst) + " -> " + str(calc_max_one_length(lst)))

lst = [1, 1, 0, 1, 1]
print(str(lst) + " -> " + str(calc_max_one_length(lst)))

lst = [1, 1, 0]
print(str(lst) + " -> " + str(calc_max_one_length(lst)))

lst = [1, 1, 1, 0, 0, 0, 1, 1, 1]
print(str(lst) + " -> " + str(calc_max_one_length(lst)))

lst = [0, 0, 1, 1, 0, 1, 1, 0]
print(str(lst) + " -> " + str(calc_max_one_length(lst)))

lst = [1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
print(str(lst) + " -> " + str(calc_max_one_length(lst)))

lst = [1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
print(str(lst) + " -> " + str(calc_max_one_length(lst)))

lst = [0, 0, 0]
print(str(lst) + " -> " + str(calc_max_one_length(lst)))
