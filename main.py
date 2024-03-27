import random

def choose_word():
    words = ["apple", "banana", "orange", "grape", "pineapple", "strawberry", "watermelon"]
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

def main():
    print("Welcome to Hangman!")
    word = choose_word()
    guessed_letters = []
    attempts = 6
    
    while attempts > 0:
        print("\n" + display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        
        guessed_letters.append(guess)
        
        if guess not in word:
            attempts -= 1
            print(f"Incorrect guess! {attempts} attempts left.")
            if attempts == 0:
                print("Sorry, you're out of attempts. The word was:", word)
                break
        else:
            if '_' not in display_word(word, guessed_letters):
                print("Congratulations! You guessed the word:", word)
                break
    
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        main()
    else:
        print("Thanks for playing!")

if __name__ == "__main__":
    main()
