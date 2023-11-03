# CodeAlpha_Hangman
The hangman game programmed here starts by randomly selecting a word from a file called "words.txt". It then uses this selected word as the argument for the hangman function. The hangman function first displays the current word state with hyphens for letters not yet guessed. It also shows the letters already guessed and the number of incorrect guesses made so far.

The game then allows the user to input a letter. If the letter is in the word, it replaces the corresponding hyphen in the word state with the guessed letter. If the letter is not in the word, it adds the letter to the list of incorrect guesses. This process continues until the word is completely guessed or the user runs out of guesses.

At the end of the game, a message is displayed to inform the user of their success or failure. The game also counts the number of incorrect guesses made throughout the game, with six being the maximum allowed before the user loses.

To ensure a new word is chosen each time the program is run, the word is randomly selected within the hangman function. This ensures the hangman game always starts with a different word from the "words.txt" file.
