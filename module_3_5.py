def get_muitiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:
        return first*get_muitiplied_digits(int(str_number[1:]))
    elif len(str_number) <= 1:
        return first
result = get_muitiplied_digits(4506)
print(result)