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


def randomstuffgo():
    print("this is a silly wittle tewxt advwentuwe gawme")
    print("i cant believe i typed that fahh")
    tungsahurcomes = input("tung sahur comes into your room and starts hitting stuff with his bat. what u do? 1 = tell him stop, 2 = ask him why bro is here")
    if tungsahurcomes == "1": # done
        print("'grrrrrr im tripple t', you hear triple t say")
        tungsahurgrowlreaction = input("he starts walking towards you, what you doing now? 1 = hide under yo bed, 2 = try to dab bro up, 3 = tell him he mispelled triple")
        if tungsahurgrowlreaction == "1": # done
            print("due to triple t's history as a brainrot he has gained the negative attention span and forgot about you under the bed")
            undertungbed = input("what you do under there? 1 = start watching yt shorts, 2 = start watching the ticky tocky, 3 = start watching instagram reels")
            if undertungbed == "1":
                print("triple t hears you and lowkey goes under there to watch shorts w/ you YOU WIN restart the code")
            elif undertungbed == "2":
                print("triple t hears you watching the tick tock and highkey throws a grenade under the bed and you DIE grr")
            elif undertungbed == "3":
                print("triple t hears the rascist videos on that godforsaken platform and runs away through your wall, which causes your apartment building to collapse. he may or may not be back")
                apartmentGONE = input("what you do? 1 = lowkey rob a store for fun, 2 = check for wounds")
                if apartmentGONE == "1":
                    print("you have a giant scar on ur leg and you bleed out on the way, u die, restart the code twin")
                elif apartmentGONE == "2":
                    print("you have some minor bruises but thats about it")
                    print("nvm i lied u got a big ahh scar and you DIE grr restart the code twin")
                else:
                    print("twin that aint an option restart the code")
            else:
                print("twin that aint an option restart the code")
        elif tungsahurgrowlreaction == "2":
            print("he hits u with his bat and you DIE in a FIRE grrrrrr you DIE restart the code twin")
        elif tungsahurgrowlreaction == "3":
            print("triple t realizes his mistake and promptly dies you LOSE because WE ALL LOVE TRIPLE T restart the code twin")
        else:
            print("twin that aint an option restart the code")
    elif tungsahurcomes == "2":
        print("wip")




gameselector = input("what would you like to play? 1 = rock paper scissors, 2 = random stuff go") # game selector
if gameselector == "1":
    rpsdif = input("what difficulty? 1 through 5")
    rockpaperscissors(rpsdif)
elif gameselector == "2":
    randomstuffgo()
else:
    print("twin that aint an option restart the code")
