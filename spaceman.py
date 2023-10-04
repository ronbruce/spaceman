import random 

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.

    Returns: 
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    
    words_list = words_list[0].split(' ') #comment this line out if you use a words.txt file with each word on a new line
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.

    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns: 
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    #Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
    for letter in secret_word:
        if letter not in letters_guessed:
    #  secret_word != "spider":
            return False
    else:
        return True
    
# secret_word = "Kairi"
# letters_guessed = ["n", "r", "a", "u", "t", "o"]

def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.

    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    # Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet

    guessed_word = ["n", "r", "a", "u", "t", "o"]
    for letter in secret_word:
        if letter in letters_guessed == True:
            guessed_word += letter
    
        else:
            guessed_word += "_"
    return guessed_word

# secret_word = "kingdom hearts"
# letters_guessed = ["k", "i", "n", "g", "d", "o"]
# result = get_guessed_word(secret_word, letters_guessed)
# print(result)

def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word

    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word

    Returns:
        bool: True if the guess is in the secret_word, False otherwise

    '''
    #check if the letter guess is in the secret word
    if guess in secret_word:
        return True
    else:
        return False

# guess = "E"
# secret_word = "Sora"
# result = is_guess_in_word(guess, secret_word)
# print(result)

def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.

    Args:
      secret_word (string): the secret word to guess.

    '''


    #TODO: show the player information about the game according to the project spec

    #TODO: Ask the player to guess one letter per round and check that it is only one letter

    #TODO: Check if the guessed letter is in the secret or not and give the player feedback

    #TODO: show the guessed word so far

    #TODO: check if the game has been won or lost

# Imported words using random
print("Hey there! Welcome to the spaceman game. you have 6 correct guesses to complete the word.")

with open("words.txt", "r") as file:
    word_list = file.read().splitlines()

random_index = random.randint(0, len(word_list) - 1)

random_word = word_list[random_index]

# Initialize game state
guessed_word = ['_'] * len(random_word)
max_attempts_guessed = 6
incorrect_attempts = 0

while True:
    # Display state of guessed word
    print(" ".join(guessed_word))

    letter_guess = input("Hey, guess one letter: ")
    #check if the guessed letter is in the secret word
    if len(letter_guess) != 1 or not letter_guess.isalpha():
        print("Please enter a single letter.")
        continue
        
        #Update the guessed word with correctly guessed letters
    if letter_guess in random_word:
        print("You guessed correctly!")

    # Update guessed word
        for i in range(len(random_word)):
            if random_word[i] == letter_guess and guessed_word[i] == '_':
                guessed_word[i] = letter_guess
    else: 
        print("Bummer! Incorrect guess!")
        incorrect_attempts += 1
    # check if the game has been won
    if "_".join(guessed_word) == random_word:
        print(f"congrats! you guessed the word: '{random_word}'")
        break
    elif incorrect_attempts >= max_attempts_guessed:
        print(f"sorry, you lost. The word was '{random_word}")

    play_again = input("Would you like to give it another shot? (yes/no): ")
    if play_again.lower() != 'yes':
        break

