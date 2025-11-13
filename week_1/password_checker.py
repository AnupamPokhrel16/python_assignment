import getpass
#getpass helps to hide the password input
password = getpass.getpass("Enter a password")

special_chars = "@#$%&"

has_letter = any(ch.isalpha() for ch in password)
has_digit = any(ch.isdigit() for ch in password)
has_special = any(ch in special_chars for ch in password)

if len(password) >= 8 and has_letter and has_digit and has_special:
    print("Password strength:Strong")
elif len(password) >= 6 and has_letter and has_digit:
    print("Password strength:Moderate")
else:
    print("Password strength:Weak")
