def find_first_non_repeating_char(string):
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else: