# Basic theory of conditional statement
fakta = True
if (fakta):
    print("Fakta merupakan kejadian asli")
else:
    print("Fakta tidak nyata: HOAX")
    
    
# You can use conditional statement with comparison operators and logic operators
# example of comparison opertors such as: <, <=, >, >=, ==, ===
myNumber = 8
if (myNumber > 10):
    print("The number is more than 10!")
elif (myNumber == 9):
    print("It's Equal!")
elif (myNumber < 9):
    print("It's less than 9")
else:
    print("The number is less than 8!")
    

# example of logic operators: or, and
myNumber = 11
print("AND logic. Semua pengecekan logic hasilnya harus true")
if (myNumber >= 0 and myNumber <= 10):
    print("The number is between 0 - 10")
else:
    print("Unknown range")
    

print("OR logic. At least ada satu hasil true dalam kondisi, maka dianggap true")
myNumberTwo = 11
if (myNumberTwo >= 0 or myNumberTwo <= 10):
    print("The number is between 0 - 10")
else:
    print("Unknown range")
    
