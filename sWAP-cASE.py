def swap_case(s):
    swapped_s = ""
    for char in s:
        if char.islower():
            char = char.upper()
        elif char.isupper():
            char = char.lower()
        swapped_s += char
    return swapped_s