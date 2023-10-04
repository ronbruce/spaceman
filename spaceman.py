import random
# Note: my game is in an infinite loop. i tried so many different solutions and was not able to solve this challenge.
def choose_random_word():
    with open("words.txt", "r") as file:
        word_list = file.read().splitlines()
    return random.choice(word_list)

def spaceman():
    secret_word = choose_random_word()
    letters_guessed = []
    max_attempts = 6

    print("Hey, Welcome to Spaceman!")
    print("You will have 6 tries at guessing the right word")
    print("_____________________________")

    display_word = "_" * len(secret_word)  # Initialize display_word

    while max_attempts > 0 and secret_word != display_word:
        print("Word: " + display_word)
        print("Incorrect guesses left: " + str(max_attempts))

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in letters_guessed:
            print("You already guessed that letter.")
            continue

        letters_guessed.append(guess)

        if guess not in secret_word:
            print("Nope. Incorrect guess!")
            max_attempts -= 1
        else:
            # Update display_word with correctly guessed letters
            display_word = "".join([letter if letter in letters_guessed else "_" for letter in secret_word])

    if display_word == secret_word:
        print("Congratulations! You guessed the word: " + secret_word)
    else:
        print("Sorry, you ran out of guesses. The word was: " + secret_word)

    play_again = input("Would you like to give it another shot? (yes/no): ").lower()
    if play_again == 'yes':
        spaceman()
    else:
        print("Thanks for playing Spaceman!")

spaceman()


            


    
