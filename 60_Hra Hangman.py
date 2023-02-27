# Hangman
import random
from test2 import stages

# generovani nahodneho slova
words = ["harry","ronald","albus","hermiona"]
random_words = words[random.randint(0, 3)]


# generovani podtrzitek
hidden_word = []
for one_letter in random_words:
    hidden_word.append("_")

# zivoty
lives = 6
print(stages[lives])

# vypsani slova s podtrzitky v normalni podobe
printedWord = ""
for one_letter in hidden_word:
    printedWord += one_letter
print(printedWord)

while "_" in hidden_word:
    guess = input("Zadejte hadane pismeno\n").lower()
    for index in range(0, len(random_words)):
        if guess == random_words[index]:
            hidden_word[index] = guess
    
    # kontrola životů
    if guess not in random_words:
        lives -= 1
        print(stages[lives])
    print(f"Pocet vasich zivotu je {lives}")
    if lives == 0:
        print("Prohrali jste!")
        break

    # vypsani slova s podtrzitky v normalni podobe
    printedWord = ""
    for one_letter in hidden_word:
        printedWord += one_letter
    print(printedWord)


# kontrola vitezstvi
    if "_" not in hidden_word:
        print("Vyhráli jste!!")



