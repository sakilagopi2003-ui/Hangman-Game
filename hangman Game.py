import random

words = {
    "Fruits": ["apple", "banana", "mango"],
    "Animals": ["tiger", "elephant", "zebra"]
}

def play_game():
    category = random.choice(list(words.keys()))
    word = random.choice(words[category])
    guessed = []
    attempts = 6

    print(f"\nCategory: {category}")

    while attempts > 0:
        display = [letter if letter in guessed else "_" for letter in word]
        print("Word:", " ".join(display))
        print("Attempts left:", attempts)

        if "_" not in display:
            print("🎉 You Won!")
            return

        guess = input("Enter letter: ").lower()

        if guess in guessed:
            print("Already guessed!")
            continue

        guessed.append(guess)

        if guess not in word:
            attempts -= 1
            print("Wrong guess!")

        # Hint
        if attempts == 3:
            print("💡 Hint: First letter is", word[0])

    print("💀 Game Over! Word was:", word)


while True:
    play_game()
    if input("Play again? (y/n): ").lower() != 'y':
        break