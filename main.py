import random

def rockpaperscissors(dif): # rock paper scissors
    if dif == "1": # done
        rocplayed = input("what would you like to play? 1 = rock, 2 = paper, 3 = scissors")
        if rocplayed == "1":
            print("i had scissors, you win")
        elif rocplayed == "2":
            print("i had rock, you win")
        elif rocplayed == "3":
            print("i had paper, you win")
        else:
            print("twin that aint an option restart the code")
    elif dif == "2": # done
        randomroc = random.randint(1,6)
        rocplayed = input("what would you like to play? 1 = rock, 2 = paper, 3 = scissors")
        if randomroc == 1:
            if rocplayed == "1" or rocplayed == "2" or rocplayed == "3":
                print("tie")
            else:
                print("twin that aint an option restart the code")
        elif randomroc == 2:
            if rocplayed == "1":
                print("i had paper, i win")
            elif rocplayed == "2":
                print("i had scissors, i win")
            elif rocplayed == "3":
                print("i had rock, i win")
            else:
                print("twin that aint an option restart the code")
        elif randomroc == 3 or randomroc == 4 or randomroc == 5 or randomroc == 6:
            if rocplayed == "1":
                print("i had scissors, you win")
            elif rocplayed == "2":
                print("i had rock, you win")
            elif rocplayed == "3":
                print("i had paper, you win")
            else:
                print("twin that aint an option restart the code")
    elif dif == "3": # done
        randomroc = random.randint(1,3)
        rocplayed = input("what would you like to play? 1 = rock, 2 = paper, 3 = scissors")
        if rocplayed == "1":
            if randomroc == 1:
                print("i had paper, i win")
            elif randomroc == 2:
                print("tie")
            elif randomroc == 3:
                print("i had scissors, you win")
        elif rocplayed == "2":
            if randomroc == 1:
                print("i had scissors, i win")
            elif randomroc == 2:
                print("tie")
            elif randomroc == 3:
                print("i had rock, you win")
        elif rocplayed == "3":
            if randomroc == 1:
                print("i had rock, i win")
            elif randomroc == 2:
                print("tie")
            elif randomroc == 3:
                print("i had paper, you win")
        else:
            print("twin that aint an option restart the code")
    elif dif == "4": # done
        randomroc = random.randint(1,6)
        rocplayed = input("what would you like to play? 1 = rock, 2 = paper, 3 = scissors")
        if randomroc == 1:
            if rocplayed == "1" or rocplayed == "2" or rocplayed == "3":
                print("tie")
            else:
                print("twin that aint an option restart the code")
        if randomroc == 2:
            if rocplayed == "1":
                print("i had scissors, you win")
            elif rocplayed == "2":
                print("i had rock, you win")
            elif rocplayed == "3":
                print("i had paper, you win")
            else:
                print("twin that aint an option restart the code")
        if randomroc >= 3:
            if rocplayed == "1":
                print("i had paper, i win")
            elif rocplayed == "2":
                print("i had scissors, i win")
            elif rocplayed == "3":
                print("i had rock, i win")
            else:
                print("twin that aint an option restart the code")
    elif dif == "5": # done
        rocplayed = input("what would you like to play? 1 = rock, 2 = paper, 3 = scissors")
        if rocplayed == "1":
            print("i had paper, i win")
        elif rocplayed == "2":
                print("i had scissors, i win")
        elif rocplayed == "3":
                print("i had rock, i win")
        else:
                print("twin that aint an option restart the code")
    else: # done
        print("twin that aint an option restart the code")

gameselector = input("what would you like to play? 1 = rock paper scissors") # game selector
if gameselector == "1":
    rpsdif = input("what difficulty? 1 through 5")
    rockpaperscissors(rpsdif)
else:
    print("twin that aint an option restart the code")
