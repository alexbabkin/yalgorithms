def max_num_guests(guests):
    guest_days = []
    for guest in guests:
        days = range(guest[0], guest[1])
        guest_days.extend(days)
    guest_num = {}
    for d in guest_days:
        if not d in guest_num:
            guest_num[d] = 0
        guest_num[d] += 1
    return max(guest_num.values())


input = [(1, 2), (1, 3), (2, 4), (2, 3), (1, 4)]
output = max_num_guests(input)
print(f"input: {input}")
print(f"output: {output}")
