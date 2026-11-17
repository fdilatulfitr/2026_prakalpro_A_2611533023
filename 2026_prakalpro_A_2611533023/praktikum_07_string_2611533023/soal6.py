# Nama: Fadilatul fitri
# Nim: 2611533023
# Question 6
first_name = " muhammad"
last_name = "rafi "
full_name = first_name.strip() + " " + last_name.strip()
print(full_name)
print(full_name.title())



full_name = "Fadilatul Fitri"
nim = "2611533023"

clean = full_name.strip()
space = clean.find(" ")

if space == -1:
    first = clean.lower()
else:
    first = clean[:space].lower()

username = first + nim[-3:]
print(username)
# Build the username: first name in lowercase + last 3 digits of the NIM.
# Do not use split().
