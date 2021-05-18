
def get_intersections(a, b):
    my_b = list(b)
    result = []

    for elem in a:
        if elem in my_b:
            result.append(elem)
            my_b.remove(elem)

    return result


a = [1, 2, 3, 2, 0]
b = [5, 1, 2, 7, 3, 2]

print(get_intersections(a, b))
