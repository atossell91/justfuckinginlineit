import math
import sys

subtwenties = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen"
}

tens_words = {
    2: "twenty",
    3: "thirty",
    4: "fourty",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "ninety",
}

steps = [
    {"step_digits": 2, "step_word": ""},
    {"step_digits": 1, "step_word": "hundred"},
    {"step_digits": 3, "step_word": "thousand"},
    {"step_digits": 3, "step_word": "million"},
]

def extract_num(target, digits):
    divisor = 10**digits
    trimmed = target % divisor

    remainder = int(target/divisor)
    return remainder, trimmed

def speak_num(number):
    remainder, trim = extract_num(number, 2)
    tens = trim

    remainder, trim = extract_num(remainder, 1)
    hundreds = trim

    remainder, trim = extract_num(remainder, 3)
    thousands = trim

    print(f'{thousands} thousand {hundreds} hundred and {tens}')

def tens_helper(number):
    if number < 20:
        return subtwenties[number]
    elif number < 100:
        tens, digit = extract_num(number, 1)
        return tens_words[tens] + " " + tortchfairy(digit, 0)

def tortchfairy(number, step_index):
    step_info = steps[step_index]
    if number < 100:
        return tens_helper(number) + " " + step_info["step_word"]
    
    num, trim = extract_num(number, step_info["step_digits"])

    print(f'{trim}: {step_info}')
    stri = tortchfairy(num, step_index+1) + " " + tortchfairy(trim, step_index+1)
    print(stri)
    return stri


def main():
    tortchfairy(931, 0)

if __name__ == '__main__':
    main()