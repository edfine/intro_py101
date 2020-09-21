def roman(rnum):
    roman_dict = {"M": 1000, 'C': 100, "L": 50, "X": 10, "I": 1}
    prev = max(roman_dict.values())
    total = 0
    for char in rnum:
        if prev < roman_dict[char]:
            total += roman_dict[char] - 2 * prev
        else:
            total += roman_dict[char]
        prev = roman_dict[char]
    return total


rstr = "I"
print(roman(rstr))

rstr = "C"
print(roman(rstr))

rstr = "XI"
print(roman(rstr))

rstr = "XX"
print(roman(rstr))

rstr = "IL"
print(roman(rstr))

rstr = "IX"
print(roman(rstr))
