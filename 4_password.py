import re

def is_password(pwd):

    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&+=!])[A-Za-z\d@#$%^&+=!]{16}$'

    if re.match(pattern, pwd):
        return True
    else:
        return False

password = "Abc@123$rtS*Wf34"

if is_password(password):
    print(f"{password} is a valid password")
else:
    print(f"{password} is not a valid password")