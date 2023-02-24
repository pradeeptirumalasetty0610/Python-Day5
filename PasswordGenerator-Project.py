import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

letters_symbols_symbols=[]
letters_symbols_symbols.extend(letters)
letters_symbols_symbols.extend(symbols)
letters_symbols_symbols.extend(numbers)

letter_counter=nr_letters
symbol_counter=nr_symbols
number_counter=nr_numbers
passwordgen=''

while len(passwordgen) < nr_letters+nr_symbols+nr_numbers:
    data = random.choice(letters_symbols_symbols)
    if data in letters and letter_counter!=0:
        passwordgen += data
        letter_counter -= 1
    elif data in symbols and symbol_counter!=0:
        passwordgen += data
        symbol_counter -= 1
    elif data in numbers and number_counter!=0:
        passwordgen += data
        number_counter -= 1


print(passwordgen)