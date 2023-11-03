import random

def get_word():
    with open("words.txt", "r") as f:
        words = f.read().splitlines()
    return random.choice(words).upper()

def hangman(word):
    word_guessed = ['-'] * len(word)
    word_list = list(word)
    incorrect_guesses = 0
    letter_guessed = []

    print("\nWelcome to Hangman! Let's begin...")

    while incorrect_guesses < 6 and '-' in word_guessed:
        print("\nWord: ", ' '.join(word_guessed))
        print("Incorrect guesses: ", ', '.join(letter_guessed))
        guess = input("\nGuess a letter: ").upper()

        if guess in word_list:
            index = word_list.index(guess)
            word_guessed[index] = guess
            word_list[index] = '_'
        elif guess not in letter_guessed:
            letter_guessed.append(guess)
            incorrect_guesses += 1
            print("\nOops! That letter is not in the word. You've now guessed", incorrect_guesses, "letters.")
        else:
            print("\nYou've already guessed that letter. Try again!")

    if incorrect_guesses < 6:
        print("\nCongratulations! You've guessed the word:", ' '.join(word_guessed))
    else:
        print("\nSorry, you've run out of guesses! The word was", word)

def main():
    word = get_word()
    hangman(word)

if __name__ == "__main__":
    main()