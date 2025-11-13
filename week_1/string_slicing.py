User_name = input("Enter your name: ")
initials = '.'.join([word[0].upper() for word in User_name.split()])
# first_initial = initials[0][0]
# last_initial = initials[-1][0]
# print(f"Your initials are: {first_initial}{last_initial}")
print(f"Your initials are{initials}")