def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    a = len(str_number)
    if a <= 1:
        return first
    elif a > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
result = get_multiplied_digits(40203)
print(result)
