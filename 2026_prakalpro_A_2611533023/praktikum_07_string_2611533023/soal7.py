# Nama: Fadilatul fitri
# Nim: 2611533023
# Question 7

name = "Fadilatul Fitri"
nim = "2611533023"

clean = name.strip()
space = clean.find(" ")
if space == -1: 
    first = clean.lower()
else:
    first = clean[:space].lower()

username = first +nim[-3:]
intake = "20" + nim[:2]

print("=" * 30)
print(f"{'STUDENT CARD':^30}")
print("=" * 30)
print(f"{'Name':<10}: {name.title()}")
print(f"{'NIM':<10}: {nim}")
print(f"{'Username':<10}: {username}")
print(f"{'Intake':<10}: {intake}")
print("=" * 30)
