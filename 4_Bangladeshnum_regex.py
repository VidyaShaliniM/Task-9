import re

def is_Bangladesh_num(num):

    pattern = r'^01[3-9][0-9]{8}$'

    if re.match(pattern, num):
        return True
    else:
        return False

number = "01611223344"
if is_Bangladesh_num(number):
    print(f"{number} is a valid Bangladesh mobile number")
else:
    print(f"{number} is not a valid Bangladesh mobile number")