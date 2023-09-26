def int_or_str(l1):
    int_str = lambda x: type(x) in (int, str)
    for item in l1:
        if not int_str(item):
            return False
    return True


my_list = [1, 'Ram', 2, 'Shalini', 3, 'Orange', 4]
result = int_or_str(my_list)
print(result)
