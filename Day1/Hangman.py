import random
from Words import list_words

def get_word():
    word = random.choice(list_words)
    return word.upper()

def play(word):
    word_completion = "_ " * len(word)  
    guessed = False
    guessed_letters = []
    guessed_words = [] 
    tries = 6 
    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print()
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha(): #It's a character
            if guess in guessed_letters: #You already tried guessing
                print(f"You already guessed the letter, {guess}")
            elif guess not in word: #It's not in the word
                print(f"{guess} is not in the word.")
                tries = tries - 1
                guessed_letters.append(guess)
            else: #It's in the word
                print(f"Nice job, {guess}, is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion) #Make the blanks a list
                for index in range(len(word)):
                    if word[index] == guess:
                        word_as_list[index*2] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha(): #guessing a word
            if guess in guessed_words:
                print(f"You already guessed the word, {guess}")
            elif guess != word:
                print(f"{guess} is not the word.")
                tries = tries - 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else: #not a valid guess
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print(f"Sorry, you ran out of tries. The word was {word}. Maybe next time!")

    
def display_hangman(tries): 
    stages = [ """
                ---------
                |       |
                |       o
                |      \|/
                |       |
                |      / \\
                |
    
              """,
              """
                ---------
                |       |
                |       o
                |      \|/
                |       |
                |      / 
                |
    
              """,
              """
                ---------
                |       |
                |       o
                |      \|/
                |       |
                |      
                |
    
              """,
              """
                ---------
                |       |
                |       o
                |      \|
                |       |
                |      
                |
    
              """,
              """
                ---------
                |       |
                |       o
                |       |
                |       |
                |      
                |
    
              """,
              """
                ---------
                |       |
                |       o
                |      
                |       
                |      
                |
    
              """,
              """
                ---------
                |       |
                |       
                |      
                |     
                |     
                |
    
              """
    ]
    return stages[tries]

def main():
    word = get_word()
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)

main()
