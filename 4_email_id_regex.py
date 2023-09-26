import re

def is_valid_email(id):

    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9._]+\.[a-zA-Z]{2,}$'

    if re.match(pattern, id):
        return True
    else:
        return False

id = "example1234@gmail.com"
if is_valid_email(id):
    print(f"{id} is a valid email address")
else:
    print(f"{id} is not a valid email address")