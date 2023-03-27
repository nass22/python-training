import random
import sys

def guessANumber():
    secret_number = random.randint(0, 1000000)
    chance = 10
    win = False
    print(secret_number)

    if chance != 0 and win == False:
        while chance != 0:
            print(f"Choississez un nombre en 0 & 1000000! Il vous reste {chance} chance(s)")
            try:
                user_input = int(input("Votre choix: "))
            except ValueError:
                print("ERROR: It's not a number!")
                sys.exit()
            chance -= 1

            if user_input > secret_number:
                print("C'est moins!")
                
            elif user_input < secret_number:
                print("C'est plus!")
            else:
                win = True
                print("Bravo, vous avez gagné!")
                break

    if chance == 0:
        print("Dommage, vous avez perdu!")

guessANumber()