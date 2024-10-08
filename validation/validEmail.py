import re

def validate_email(email):
    x = re.search(r"^[\w\-\.]+@([\w-]+\.)+[\w-]{2,}$", email)
    return x.group() == email

print(validate_email("johnmicrosoft@gmail.com"))