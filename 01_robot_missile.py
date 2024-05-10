import random
import string

print("""
ROBOT MISSILE

TYPE THE CORRECT CODE
LETTER (A-Z) TO
DEFUSE THE MISSILE.
YOU HAVE 4 CHANCES

""")

rnd_letter = random.choice(string.ascii_uppercase)
max_guess = 4
cur_guess = 1

while True:
    guess = input("ENTER YOUR GUESS: ").upper()

    assert guess in string.ascii_letters and len(guess) == 1, "ONLY ONE LETTER!"

    if guess == rnd_letter:
        print("TICK...FZZZZ...CLICK...")
        print("YOU DID IT!")
        break

    elif cur_guess == max_guess:
        print("BOOOOOOMMMM...")
        print("YOU BLEW IT!")
        print(f"THE CORRECT CODE WAS {rnd_letter}")

    else:
        if ord(guess) < ord(rnd_letter):
            print("LATER")
            cur_guess += 1
        else:
            print("EARLIER")
            cur_guess += 1

