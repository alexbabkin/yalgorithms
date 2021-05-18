def group_words(words):
    result = []
    words_dict = {}
    for word in words:
        sorted_word = "".join(sorted(word))
        if not sorted_word in words_dict.keys():
            words_dict[sorted_word] = []
        words_dict[sorted_word].append(word)
    for key, value in words_dict.items():
        result.append(value)
    return result


input = ["eat", "tea", "tan", "ate", "nat", "bat"]
output = group_words(input)
print(f"input: {input}")
print(f"output: {output}")
