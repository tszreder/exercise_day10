# napisać funkcję która z tablicy wybierze wszystkie liczby calkowite, które:
# nie są zerem, nie zawierają zera z przodu, etc.

tab = ['0 12', '12 0', '12.', '12','2a', '15', '12.45']


def get_numbers(numbers_list):
    invalid_numbers = []
    valid_numbers = []
    for item in numbers_list:
        try:
            valid_numbers.append(int(item))
        except ValueError:
            invalid_numbers.append(item)
    return valid_numbers, invalid_numbers

print(get_numbers(tab), end='\n')
