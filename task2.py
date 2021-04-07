
# input_str = input('Enter the string: ')

def convert_string(input_str):

    prev_symbol = None
    len_of_series = 0
    result = ""

    for symb in input_str:
        if prev_symbol and symb != prev_symbol:
            result = result + f"{prev_symbol}{len_of_series}"
            len_of_series = 1
        else:
            len_of_series += 1

        prev_symbol = symb

    return result + f"{prev_symbol}{len_of_series}" if prev_symbol else ""

input_str = ""
print(input_str + " -> " + convert_string(input_str))

input_str = "AAABBBCCCXYZA"
print(input_str + " -> " + convert_string(input_str))

input_str = "AAAAAAAAAA"
print(input_str + " -> " + convert_string(input_str))
