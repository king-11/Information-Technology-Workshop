# fun10 takes argument of string and returns string
# stating number of lower and uppercase alphabets


def fun10(s: str):
    x = y = 0
    for i in s:
        if i.isupper():
            x += 1
        elif i.islower():
            y += 1
    return "No. of Upper case characters : {x}\nNo. of Lower case characters : {y}"
