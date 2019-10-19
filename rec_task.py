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

print(get_numbers(tab))

def is_int(number):
    try:
        int(number)
        return True
    except ValueError:
        return False


list_comp = [number for number in tab]
print(list_comp)

integers = get_numbers(tab)
# print([item if item < 13 else None for item in integers])
# print([item for item in integers if item < 13])


print([x if is_int(x) == True else None for x in tab])

[print(x) if is_int(x) == True else None for x in tab]

print([int(x) for x in tab if is_int(x) and int(x) < 13])


# napisac funkcję zwracajacą liczby całkowite w list comprehension
