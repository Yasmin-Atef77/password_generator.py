import random
import string

password = int(input("How many characters would you like in your password: "))
symbols = int(input("How many symbols would you like in your password: "))
numbers = int(input("How many numbers would you like in your password: "))
letters = int(input("How many letters would you like in your password: "))

if symbols + numbers + letters != password:
    print("That doesn't equal the number of characters you entered.")
else:
    csymbols = random.choices(string.punctuation, k=symbols)

    cnumbers = random.choices(string.digits, k=numbers)

    cletters = random.choices(string.ascii_letters, k=letters)

    all = csymbols + cnumbers + cletters

    random.shuffle(all)

    yourpassword = "".join(all)

    print(yourpassword)
