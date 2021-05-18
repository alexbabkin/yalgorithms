
def group_str(start, end, last):
    result = f"{start}" if start == end else f"{start}-{end}"
    if not last:
        result += ", "
    return result


def colapse1(lst):
    result = ""
    max_number = max(lst)
    group_start, group_end = None, None
    for i in range(max_number+1):
        if i in lst:
            if group_start is None:
                group_start = i
        else:
            if group_start is not None:
                group_end = i - 1
                result += group_str(group_start, group_end, False)
                group_start = None
    if group_start:
        result += group_str(group_start, max_number, True)
    return result


def colapse2(lst):
    result = ""
    sorted_lst = sorted(lst)
    group_start, group_end, prev_elem = None, None, None
    for elem in sorted_lst:
        if group_start is None:
            group_start = elem
        if prev_elem is not None:
            if elem != prev_elem + 1:
                group_end = prev_elem
                result += group_str(group_start, group_end, False)
                group_start = elem
        prev_elem = elem
    result += group_str(group_start, prev_elem, True)
    return result


lst = [1, 4, 5, 2, 3, 9, 8, 11, 0]
print(f"1: {lst} -> {colapse1(lst)}")

lst = [1, 4, 5, 2, 3, 9, 11, 0]
print(f"1: {lst} -> {colapse1(lst)}")

lst = [1, 4, 3, 2]
print(f"1: {lst} -> {colapse1(lst)}")

lst = [1, 4]
print(f"1: {lst} -> {colapse1(lst)}")

lst = [1, 4, 5, 2, 3, 9, 8, 11, 0]
print(f"2: {lst} -> {colapse2(lst)}")

lst = [1, 4, 5, 2, 3, 9, 11, 0]
print(f"2: {lst} -> {colapse2(lst)}")

lst = [1, 4, 3, 2]
print(f"2: {lst} -> {colapse2(lst)}")

lst = [1, 4]
print(f"2: {lst} -> {colapse2(lst)}")
