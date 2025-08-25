# === Import library yang dibutuhkan ===
import random

# === Cetak aturan permainan ===
print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

# === Generate angka acak antara 1 dan 10 ===
number = 5

# === Variabel untuk melacak tebakan benar/salah ===
isGuessRight = False

# === Loop permainan ===
while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))
