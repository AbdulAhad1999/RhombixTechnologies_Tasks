import random

def choose_word():
    words = ['python', 'hangman', 'challenge', 'programming', 'code']
    return random.choice(words)

def display_hangman(tries):
    stages = [
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   /
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |   
           |
        """,
        """
           ------
           |    |
           |    O
           |    
           |   
           |
        """,
        """
           ------
           |    |
           |    
           |    
           |   
           |
        """,
        """
           ------
           |    
           |    
           |    
           |   
           |
        """,
        """
           ------
           |    
           |    
           |    
           |   
           |
        """,
    ]
    return stages[tries]

def play():
    word = choose_word()
    guessed = ''
    tries = 6
    print("Welcome to Hangman!")
    
    while tries > 0:
        print(display_hangman(tries))
        print("Word: ", end=' ')
        
        for letter in word:
            if letter in guessed:
                print(letter, end=' ')
            else:
                print('_', end=' ')
        
        print()
        
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed:
            print("You've already guessed that letter.")
            continue
        
        guessed += guess
        
        if guess not in word:
            tries -= 1
            print(f"Wrong guess! You have {tries} tries left.")
        
        if all(letter in guessed for letter in word):
            print(f"Congratulations! You've guessed the word: {word}")
            break
    else:
        print(display_hangman(tries))
        print(f"Sorry, you've run out of tries. The word was: {word}")

if __name__ == "__main__":
    play()
