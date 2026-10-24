import random

global level
global rocupgrades
global stillplaying

level = 0
rocupgrades = 0
stillplaying = True

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


def randomstuffgo(): # triple t text adventure
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
        print("triple t doesnt respond, but he does lowkey start hitting the griddy")
        triplegriddy = input("do you? 1 = griddy w/ him, 2 = make fun of him")
        if triplegriddy == "1":
            print("yall become griddy buddies and live happily ever after YOU WIN now restart the code twin")
        elif triplegriddy == "2":
            print("triple t blows you up and you LOSE restart the code twin")
        else:
            print("twin that aint an option restart the code")
    else:
        print("twin that aint an option restart the code")


def mindreadergame(): # mind reader
    mindreadingislowkeyeasy = random.randint(1,10)
    mindreadingisez = str(mindreadingislowkeyeasy)
    mindreadmaybe = input("read my mind twin, 1 to 10.")
    if mindreadmaybe == "1" or mindreadmaybe == "2" or mindreadmaybe == "3" or mindreadmaybe == "4" or mindreadmaybe == "5" or mindreadmaybe == "6" or mindreadmaybe == "7" or mindreadmaybe == "8" or mindreadmaybe == "9" or mindreadmaybe == "10":
        print("thats a number")
        if mindreadingisez == mindreadmaybe:
            print("wow u got my number YOU WIN restart the code twin")
        else:
            print("YOU LOSE its okay tho restart the code twin")
    else:
        print("twin that aint an option restart the code")


def tripletartwork(): # self explanitory
    print("  |    _________      ")
    print("  |    |       |      ")
    print("  |    |  0 0  |      ")
    print("  |----| |___| |----  ")
    print("  |    |       |      ")
    print("       |_______|      ")
    print("         |   |       ")
    print("         |   |       ")
    print("         |   |       ")
    print("        _|   |_      ")




def rocdif4():
    randomroc = random.randint(1,6)
    rocplayed = input("what would you like to play? 1 = rock, 2 = paper, 3 = scissors")
    if randomroc == 1:
        if rocplayed == "1" or rocplayed == "2" or rocplayed == "3":
            print("tie")
            level + 1
        else:
            print("twin that aint an option restart the code")
    if randomroc == 2:
        if rocplayed == "1":
            print("i had scissors, you win")
            level + 2
        elif rocplayed == "2":
            print("i had rock, you win")
            level + 2
        elif rocplayed == "3":
            print("i had paper, you win")
            level + 2
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







def levelsim(): # a game
    stillplaying = True
    inputforlevelsim = "blah"
    print("LEVEL:")
    print(level)
    print("__")
    print("||"    )
    print("||" )
    print("||   __    __")
    print("||___||____||_____")
    print("| This is level sim, a game where you... level up!")
    print("| Input '1' for rock paper scissors, '2' for mind reader!")
    print("| Input 's' to go to shop")
    inputforlevelsim = input("")
    if inputforlevelsim == "1":
        while stillplaying == True:
            if rocupgrades == 0:
                rocdif4()
                print("keep going? 1 = yes, 2 = no")
                keepgoingmaybe = input()
                if keepgoingmaybe == "2":
                    stillplaying = False

gameselector = input("what would you like to play? 1 = rock paper scissors, 2 = random stuff go, 3 = mind reader game, 4 = triple t artwork, 5 = level sim") # game selector
if gameselector == "1":
    rpsdif = input("what difficulty? 1 through 5")
    rockpaperscissors(rpsdif)
elif gameselector == "2":
    randomstuffgo()
elif gameselector == "3":
    mindreadergame()
elif gameselector == "4":
    tripletartwork()
elif gameselector == "5":
    print("time to play some straight idiocracy")
    levelsim()
else:
    print("twin that aint an option restart the code")

#while True:
    if stillplaying == False:
        levelsim()
