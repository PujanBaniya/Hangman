import random
import Man
import words
lives=6
chosen_word= random.choice(words.word)
# print(chosen_word)
display=[]
for letter in chosen_word:
    display += '_'


print(display)
game_over=False
while not game_over:
    guessed_letter=input("Guess Letter: ").lower()
    for position in range(len(chosen_word)):
        letter=chosen_word[position]
        if letter== guessed_letter:
            display[position]=guessed_letter
        
    print(display)
    if guessed_letter not in chosen_word:
        lives-=1
        if lives==0:
            game_over=True
            print("You loose")
            print(f"The word is {chosen_word} " )
    if '_' not in display:
        game_over=True
        print("You win")
    print(Man.ManCondition[lives])