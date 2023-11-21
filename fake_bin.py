'''
Given a string of digits, you should replace any digit below 5 with '0' and
any digit 5 and above with '1'. Return the resulting string.
Note: input will never be an empty string
'''

def convert_binary(digits_str):
    result = ""
    for digit in digits_str:
        if int(digit) < 5:
            result += "0"
        else:
            result += "1"
    return result


def fake_bin(x):
    return ''.join('0' if c < '5' else '1' for c in x)
