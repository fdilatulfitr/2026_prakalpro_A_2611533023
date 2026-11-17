# Nama: Fadilatul fitri
# Nim: 2611533023
# Question 5
username = input("Username: ")
 
# Check the rules in a safe order and print the first rule that fails.
if len(username) < 5:
    print ("Invalid: at least 5 characters")
elif not username.isalnum():
    print ("Invalid: letters and digits only")
elif not username[0].isalpha():
    print ("Invalid: must start with a letter")
else:
    print("Valid")



nim = input("Nim: ")
if len(nim) == 10 and nim.isdigit():
    print (f"Valid, intake year 20{nim[:2]}")
else:
    print ("Invalid NIM")