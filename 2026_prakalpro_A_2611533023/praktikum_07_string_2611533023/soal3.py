# Nama: Fadilatul fitri
# Nim: 2611533023
# Question 3
text = "Informatika"
print (text[10])
print (text.upper())
print (text[0:20])


text = "Fadilatul Fitri"
count = 0
for char in text.lower():
    if char in "aiueo":
        count = count +1
print("Vowels:", count)
