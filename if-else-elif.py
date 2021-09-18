name = input("Please enter your username ")
if len(name) <= 5:
   print("Your name is too short.")
elif len(name) == 8:
#    print("Your name is 8 characters.")
    pass
elif len(name) >= 8:
   print("Your name is 8 or more characters.")
else:
   print("Your name is short.")