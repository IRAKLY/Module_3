def print_params(a=1, b='строка', c=True):
    print(f" a = {a}\n b = {b}\n c = {c}\n")


values_list = [True, 'String', [1, 2, 3]]
values_list_2 = [12.7, 'Число']

values_dict = {'a': False, 'b': 'Number', 'c': 67}

print_params()
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)
