MAX_ATTEMPTS = 3
attempts = 1
correct_pin = "1234"
pin = input("enter PIN: ")
while pin != correct_pin and attempts < MAX_ATTEMPTS:
    print("Incorrect PIN. Please try again.")
    pin = input("enter PIN: ")
    attempts += 1

if pin == correct_pin:
    print("Access granted.")
else:
    print("Too many incorrect attempts. Access denied.")