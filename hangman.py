import random
def hungman():
    word = random.choice(["pokemon","doraemon","shinchan","bheem","hattori","mickey","kiteretsu","tom","jerry"])
    alpha ="abcdefghijklmnopqrstuvwxyz"
    count = 10
    guess = ''
    if len(word)<=4 and len(word)>=2:
        print("The first latter is :")
        print(word[0])
    else:
        print("first and last latter is given the gsause full :")
        print(word[0],word[-1])

    while len(word)!=0 :
        choice = ""
        for letter in word:
            if letter in guess:
                choice = choice + letter
            else:
                choice = choice + "_" + " "

        if choice == word:
            print(word)
            print(" Hurry! You Won ")
            break


        print("guess your word : ",choice)

        guesses = input().lower()
        if guesses in alpha:
            guess=guess+guesses
        else:
            print("you enter wrong word enter a alphabate ")
            guesses= input().lower()

        if guesses not in word:
            count = count -1
            if count == 9:
                print("9 turn left ")
                print("---------")
            elif count == 8:
                print('8 turm left')
                print("---------")
                print("    O    ")
            elif count == 7:
                print('7 turm left')
                print("---------")
                print("    O    ")
                print("    |    ")

            elif count == 6:
                print('6 turm left')
                print("---------")
                print("    O    ")
                print("    |    ")
                print("   /     ")

            elif count == 5:
                print('5 turm left')
                print("---------")
                print("    O    ")
                print("    |    ")
                print("   / \   ")
            elif count == 4:
                print('4 turm left')
                print("---------")
                print("  \ O    ")
                print("    |    ")
                print("   / \   ")
            elif count == 3:
                print('3 turm left')
                print("---------")
                print("  \ O /   ")
                print("    |    ")
                print("   / \   ")
            elif count == 2:
                print('2 turm left')
                print("---------")
                print("  \ O /|  ")
                print("    |    ")
                print("   / \   ")
            elif count == 1:
                print('1 turm left')
                print('last chance to save your man, common!')
                print("---------")
                print("  \ O_|/ ")
                print("    |    ")
                print("   / \   ")
            elif count == 0:
                print('you loose')
                print('your man dies')
                print("------|--")
                print("    O_|  ")
                print("   /|\   ")
                print("   / \   ")
                break












name = input("Enter your Name : ").title()
print("Welcome",name)
print("Rules:")
print("you have to guess the word in 10 try otherwise you loss the game ")
hungman()
print()




