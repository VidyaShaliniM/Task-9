import re

def is_USA_num(num):

    pattern = r'^(?:\+1\s?)?(\d{3})[-.\s]?(\d{3})[-.\s]?(\d{4})$'

    if re.match(pattern, num):
        return True
    else:
        return False

number = "+1 153-456-6799"
if is_USA_num(number):
    print(f"{number} is a valid USA Telephone number")
else:
    print(f"{number} is not a valid USA Telephone number")