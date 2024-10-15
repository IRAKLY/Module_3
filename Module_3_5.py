# def get_multiplied_digits(number):
#     if number == 0:
#         return 1
#     else:
#         return number * get_multiplied_digits(number - 1)

def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    elif first == 0:
        return 1
    else:
        return first


n = int(input("Введите целое число: "))

result = get_multiplied_digits(n)
print(f'Произведение чисел: {result}')
