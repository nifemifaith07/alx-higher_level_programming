#!/usr/bin/python3
def roman_to_int(roman_string):
    ri = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    i = 0
    n = len(roman_string)
    sum = 0
    if isinstance(roman_string, str):
        while i < n:
            if (i != n - 1 && ri[roman_string[i]] < ri[roman_string[i + 1]]):
                sum -= ri[roman_string[i]]
            else:
                sum += ri[roman_string[i]]
            i += 1
         return sum
    else:
        return 0
