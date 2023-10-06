import random 

def choose_random_word():
    with open("words.txt", "r") as file:
        word_list = file.readlines()[0].split(' ')
    return random.choice(word_list)

# Imported words using random
print("Hey there! Welcome to the spaceman game. you have 6 correct guesses to complete the word.")

random_word = choose_random_word()

# Initialize game state
guessed_word = ['_'] * len(random_word)
max_attempts_guessed = 6
incorrect_attempts = 0

while True:
    # Display state of guessed word
    # print(" ".join(guessed_word))

    print("Word: " + " ".join(guessed_word))

    letter_guess = input("Hey, guess one letter: ")
    
    if len(letter_guess) != 1 or not letter_guess.isalpha():
        print("Please enter a single letter.")
        continue

    # Check if the guessed letter is in the secret word
    if letter_guess in random_word:
        print("You guessed correctly!")

        # Update the guessed word with correctly guessed letters
        for i in range(len(random_word)):
            if random_word[i] == letter_guess:
                guessed_word[i] = letter_guess
    else:
        print("Bummer! Incorrect guess!")
        incorrect_attempts += 1

    # Check if the game has been won
    if "".join(guessed_word) == random_word:
        print(f"Congratulations! You guessed the word: {random_word}")
        break
    elif incorrect_attempts >= max_attempts_guessed:
        print(f"Sorry, you lost. The word was '{random_word}'")
        break

