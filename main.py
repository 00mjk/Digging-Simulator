# Good Luck Reading All This
# Wait A Minute, Why Are You Even Reading This In The First Place?
from os import system as sys
from os import environ as env
from time import sleep as wait
from random import choice, randint
from math import ceil as C
from colorama import Fore as fore
from replit import db
from threading import Thread as thread

def clear(): sys('clear')

dsta = True

digspeed = 1

inventory = []
pet = None
pav = 0
pl = 0

animm = False

print("""                  █                             |
                  █                             |
                  █                             |
                  █                             |
                  █                             |
                  █                             |
                  █                             |
                  █                             |
                  █                             |
              █████████                 ##      |
              █████████             ######      |
               ███████            ##########    |
                █████        ################## |
~~~~~~~~~~~                ~~~~~~~~~~~~~~~~~~~~~|
#########                    ###################|
####                           #################|
##                                 #############|
################################################|
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\n""")

def dig():
    global digspeed
    if digspeed < 0:
        digspeed = 0
    clear()
    print("    \                      ")
    print("     \                     ")
    print("      \                    ")
    print("       \_____              ")
    print("       |    |              ")
    print("       |____|              ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("###########################")
    print("###########################")
    print("###########################")

    wait(digspeed)
    clear()
    
    print("                           ")
    print("                     *     ")
    print("            /‾\         *  ")
    print("   ________/   \      *    ")
    print("           \   /           ")
    print("            \_/            ")
    print("~~~~      ~~~~~~~~~~~~~~~~~")
    print("####      #################")
    print("######   ##################")
    print("###########################")

    wait(digspeed)
    clear()

    print("    \                      ")
    print("     \                     ")
    print("      \                    ")
    print("       \_____              ")
    print("       |    |         ###  ")
    print("       |____|        ######")
    print("~~~~      ~~~~~~~~~~~~~~~~~")
    print("####      #################")
    print("######   ##################")
    print("###########################")

    wait(digspeed)
    clear()
    
    print("                       *   ")
    print("                        *  ")
    print("            /‾\      *     ")
    print("   ________/   \           ")
    print("           \   /      ###  ")
    print("            \_/      ######")
    print("~~~~        ~~~~~~~~~~~~~~~")
    print("####        ###############")
    print("###           #############")
    print("###########################")

    wait(digspeed)
    clear()

    print("    \                      ")
    print("     \                     ")
    print("      \                    ")
    print("       \_____          #   ")
    print("       |    |       #####  ")
    print("       |____|      ########")
    print("~~~~        ~~~~~~~~~~~~~~~")
    print("####        ###############")
    print("###           #############")
    print("###########################")

    wait(digspeed)
    clear()
    
    print("                        *  ")
    print("                   *  *    ")
    print("            /‾\          * ")
    print("   ________/   \       #   ")
    print("           \   /    #####  ")
    print("            \_/    ########")
    print("~~~~          ~~~~~~~~~~~~~")
    print("####           ############")
    print("###               #########")
    print("###########################")

    wait(digspeed)
    clear()
    
    print("    \                      ")
    print("     \                     ")
    print("      \                #   ")
    print("       \_____        ###   ")
    print("       |    |       ###### ")
    print("       |____|    ##########")
    print("~~~~          ~~~~~~~~~~~~~")
    print("####           ############")
    print("###               #########")
    print("###########################\n")

normalbox = ["Can", "500$", "Candy Wrapper", "Bottle Cap"]
goodbox = ["Car Tire", "1000$", "Nothing", "Diamond"]
megabox = ["Better Shovel", "2000$", "Great Shovel"]
ultimatebox = ["Mega Shovel", "4000$", "Super Shovel", "Dinosaur Bone"]
optimumbox = ["Superior Shovel", "8000$", "Prehistoric Spear", "5 T-Rex Bones"]
apexbox = ["Remarkable Shovel", "Extraordinary Shovel", "+20 Hp"]
epitomebox = ["Finist Shovel", "20000$", "2 Prehistoric Spears"]

petc1 = ["Frog", "Hamster", "Parrot"]
petc2 = ["Dog", "Gopher", "Mole"]
petc3 = ["Skunks", "Aarkvark", "Badger"]
petc4 = ["Platypus", "Tenrec"]

xp = 0
level = 0

trex = 0
trexfin = False
tricera = 0
tricerafin = False
steg = 0
stegfin = False
raptor = 0
raptorfin = False
spino = 0
spinofin = False
allo = 0
allofin = False
ptero = 0
pterofin = False

cd = dig
cdf = False

shoe = 0
shoefin = False
diamond = 0
diamondfin = False
dinosaurbone = 0
dinofin = False
can = 0
canfin = False
candywrapper = 0
candyfin = False
bottlecap = 0
bottlefin = False
cartire = 0
tirefin = False
car = 0
carfin = False
magicbean = 0
magicfin = False
trident = 0
tridentfin = False

hafin = False

rewards = ["Shoe", "Shoe", "Shoe", "Shoe", "Diamond", "Diamond", "Dinosaur Bone", "Can", "Can", "Can", "Candy Wrapper", "Candy Wrapper", "Candy Wrapper", "Bottle Cap", "Bottle Cap", "Bottle Cap", "Bottle Cap", "Car Tire", "Car Tire", "Car", "Car", "Magic Bean", "Magic Bean", "Magic Bean", "Trident", "Nothing", "Nothing", "Nothing", "Nothing", "Nothing", "Nothing", "Nothing"]

mo = ["Shoe", "Shoe", "Shoe", "Shoe", "Shoe", "Diamond", "Diamond", "Dinosaur Bone", "Can", "Can", "Can", "Can", "Candy Wrapper", "Candy Wrapper", "Candy Wrapper", "Candy Wrapper", "Candy Wrapper", "Bottle Cap", "Bottle Cap", "Bottle Cap", "Bottle Cap", "Bottle Cap", "Car Tire", "Car Tire", "Car Tire", "Car", "Car", "Magic Bean", "Magic Bean", "Magic Bean", "Trident"]

invs = 1

bal = 0

rank = "Unexperienced Digger"

variableidk = 0
wb = False
wb1 = False
wb2 = False

bbpf = False

print("Welcome To Digging Simulator!")
print("For The Best Experience, Please Slide The Console To The Very Left\n")
print("Dig Stuff Up And Then Sell Them To Make Profit!")
print("Open Mystery Boxes For Surprises!")
print("Buy Shovels For More Money!\n")
print("Have Fun!\n")

class defaultshovel():
    value = 0

class bettershovel():
    value = 10

class greatshovel():
    value = 20

class megashovel():
    value = 40

class ultrashovel():
    value = 70

class supershovel():
    value = 100

class superiorshovel():
    value = 120

class remarkableshovel():
    value = 150

class extraordinaryshovel():
    value = 170

class finistshovel():
    value = 200

class nobleshovel():
    value = 220

dinos = ["raptor", "trex", "triceratops", "stegasaurus", "spinosaurus", "allosaurus", "pterodactyl"]

print("People Who Have Finished The Game: None Yet\n")

username = env["REPL_OWNER"]
print("Greetings,",  str(username) + "!")
reader = input("\n(y or n) Are You A Fast Reader?: ")
cred = input("(y or n) Would You Like To See The Credits Before Starting?: ")

TIME = None

if reader == "y":
    TIME = 1

else:
    TIME = 2

if cred == "y":
    clear()
    credit = ["Main Developer: HyperAlternative", "Source Code: HyperScripter (My Main)", "Beta Tester: POWERMAN101", "Beta Tester: maz416", "Design Ideas: MrVoo", ""]

    def credits(credit):
    
        z = 0
        x = 20
        y = credit[z]
        
        while True:
            
            print("\n" * x)
            print("                               " + y)
            
            wait(0.2)
            
            x -= 1
    
            if z != len(credit) - 1:
                clear()
                if x < 0:
                    x = 20
                    z += 1
                    y = credit[z]
    
            else:
                print("The End")
                input("\nPress Enter To Continue ")
                break
      
    credits(credit)

inf = float('inf')

class privateshovel():
    value = inf

shovel = defaultshovel
ss = "Default Shovel"

GAMEDONE = False

ps = 0
psfin = False
psr = 201

clear()

ahp = 0

session = 0

w = [b'\xff\xfe\x00\x00h\x00\x00\x00y\x00\x00\x00p\x00\x00\x00e\x00\x00\x00r\x00\x00\x00h\x00\x00\x00a\x00\x00\x00c\x00\x00\x00k\x00\x00\x00'.decode("UTF-32"), b'\xff\xfe\x00\x00s\x00\x00\x00u\x00\x00\x00p\x00\x00\x00e\x00\x00\x00r\x00\x00\x00s\x00\x00\x00t\x00\x00\x00r\x00\x00\x00o\x00\x00\x00n\x00\x00\x00g\x00\x00\x00'.decode("UTF-32"), b'\xff\xfe\x00\x00s\x00\x00\x00t\x00\x00\x00o\x00\x00\x00p\x00\x00\x00d\x00\x00\x00e\x00\x00\x00c\x00\x00\x00o\x00\x00\x00d\x00\x00\x00i\x00\x00\x00n\x00\x00\x00g\x00\x00\x00'.decode("UTF-32"), b'\xff\xfe\x00\x00d\x00\x00\x00i\x00\x00\x00g\x00\x00\x00s\x00\x00\x00i\x00\x00\x00m\x00\x00\x001\x00\x00\x000\x00\x00\x000\x00\x00\x00'.decode("UTF-32")]

n = input("(l) Load Data Or (n) New Game: ")

if n == "l":
    try:
        print("\nLoading..")
        inventory = db["inventory"]
        invs = db["invs"]
        bal = db["bal"]
        xp = db["xp"]
        level = db["level"]
        trex = db["trex"]
        tricera = db["tricera"]
        steg = db["steg"]
        raptor = db["raptor"]
        spino = db["spino"]
        allo = db["allo"]
        ptero = db["ptero"]
        trexfin = db["trexfin"]
        tricerafin = db["tricerafin"]
        stegfin = db["stegfin"]
        raptorfin = db["raptorfin"]
        spinofin = db["spinofin"]
        allofin = db["allofin"]
        pterofin = db["pterofin"]
        shoe = db["shoe"]
        shoefin = db["shoefin"]
        diamond = db["diamond"]
        diamondfin = db["diamondfin"]
        dinosaurbone = db["dinosaurbone"]
        dinofin = db["dinofin"]
        can = db["can"]
        canfin = db["canfin"]
        candywrapper = db["candywrapper"]
        candyfin = db["candyfin"]
        bottlecap = db["bottlecap"]
        bottlefin = db["bottlefin"]
        cartire = db["cartire"]
        tirefin = db["tirefin"]
        car = db["car"]
        carfin = db["carfin"]
        magicbean = db["magicbean"]
        magicfin = db["magicfin"]
        trident = db["trident"]
        tridentfin = db["tridentfin"]
        rewards = db["rewards"]
        psr = db["psr"]
        ps = db["ps"]
        variableidk = db["variableidk"]
        wb = db["wb"]
        wb1 = db["wb1"]
        wb2 = db["wb2"]
        digspeed = db["digspeed"]
        hafin = db["hafin"]
        session = db["session"]
        pet = db["pet"]
        pav = db["pav"]
        pl = db["pl"]
        session += 1
        print("Loaded\n")

    except:
        print("You Don't Have Saved Data Or You Are Not Up To Date")
        wait(TIME)
        clear()
        x = 20

        while True:
            print("You Settle On The Journey To The Digging Planet, Earth..")
            print("\n" * x)
            print("""               /‾‾\ 
               |  |
               |  |
              /|  |\\
             / |  | \\
            /__|__|__\\
              /----\\
              ‾‾‾‾‾‾""")
            x -= 1
            wait(0.2)
            clear()
            if x == 0:
                break
    
        wait(TIME)
        print("You Have Arrived...")
        wait(TIME)

else:
    x = 20
    clear()
    while True:
        print("You Settle On The Journey To The Digging Planet, Earth..")
        print("\n" * x)
        print("""           /‾‾\ 
           |  |
           |  |
          /|  |\\
         / |  | \\
        /__|__|__\\
          /----\\
          ‾‾‾‾‾‾""")
        x -= 1
        wait(0.2)
        clear()
        if x == 0:
            break

    wait(TIME)
    print("You Have Arrived...")
    wait(TIME)

def save():
    global dsta
    if True:
        while dsta == True:
            db["inventory"] = inventory
            db["invs"] = invs
            db["bal"] = bal
            db["xp"] = xp
            db["level"] = level
            db["trex"] = trex
            db["tricera"] = tricera
            db["steg"] = steg
            db["raptor"] = raptor
            db["spino"] = spino
            db["allo"] = allo
            db["ptero"] = ptero
            db["trexfin"] = trexfin
            db["tricerafin"] = tricerafin
            db["stegfin"] = stegfin
            db["raptorfin"] = raptorfin
            db["spinofin"] = spinofin
            db["allofin"] = allofin
            db["pterofin"] = pterofin
            db["shoe"] = shoe
            db["shoefin"] = shoefin
            db["diamond"] = diamond
            db["diamondfin"] = diamondfin
            db["dinosaurbone"] = dinosaurbone
            db["dinofin"] = dinofin
            db["can"] = can
            db["canfin"] = canfin
            db["candywrapper"] = candywrapper
            db["candyfin"] = candyfin
            db["bottlecap"] = bottlecap
            db["bottlefin"] = bottlefin
            db["cartire"] = cartire
            db["tirefin"] = tirefin
            db["car"] = car
            db["carfin"] = carfin
            db["magicbean"] = magicbean
            db["magicfin"] = magicfin
            db["trident"] = trident
            db["tridentfin"] = tridentfin
            db["rewards"] = rewards
            db["psr"] = psr
            db["ps"] = ps
            db["variableidk"] = variableidk
            db["wb"] = wb
            db["wb1"] = wb1
            db["wb2"] = wb2
            db["digspeed"] = digspeed
            db["hafin"] = hafin
            db["pet"] = pet
            db["pav"] = pav
            db["pl"] = pl
            db["session"] = session

s = thread(target = save)
s.start()

################
######MAIN######
################

def main():

    global bal, shovel, ss, rank, normalbox, goodbox, megabox, ultimatebox, invs, tricera, trex, raptor, steg, tricerafin, trexfin, stegfin, raptorfin, dinos, cd, cdf, shoe, diamond, dinosaurbone, can, candywrapper, bottlecap, cartire, shoefin, diamondfin, dinofin, canfin, candyfin, bottlefin, tirefin, GAMEDONE, ps, psfin, hp, hp1, dmg, dmg1, wb, wb1, wb2, variableidk, psr, w, powerup, ahp, superiorshovel, remarkableshovel, extraordinaryshovel, finistshovel, car, magicbean, trident, carfin, magicfin, tridentfin, digspeed, bbpf, spino, spinofin, allo, allofin, ptero, pterofin, xp, level, session, animm, hafin, pet, pav, petc1, petc2, petc3, petc4, nobleshovel, pl, auto, dsta
    
    if bal < 0:
        bal = 0
    
    pro = f"""{username}'s Profile
-----------------------
Cans Found: {can}                   Candy Wrappers Found: {candywrapper}
Diamonds Found: {diamond}               Bottle Caps Found: {bottlecap}
Dinosaur Bones Found: {dinosaurbone}         Car Tires Found: {cartire}
Shoes Found: {shoe}                  Prehistoric Spears Found: {ps}
Cars Found: {car}                   Magic Beans Found: {magicbean}
Tridents Found: {trident}

Raptor Bones Found: {raptor}           T-Rex Bones Found: {trex}
Triceratops Bones Found: {tricera}      Stegasaurus Bones Found: {steg}
Spinosaurus Bones Found: {spino}      Allosaurus Bones Found: {allo}
Pterodactyl Bones Found: {ptero}

Shovel: {ss}
Rank: {rank}
Xp: {xp}
Level: {level}
Pet Level: {pl}
Session: {session}
    """

    print("""
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    | D I G G I N G - S I M U L A T O R ️|
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """)

    if invs == 13 and trexfin == True and raptorfin == True and stegfin == True and shoefin == True and diamondfin == True and dinofin == True and canfin == True and candyfin == True and bottlefin == True and tirefin == True and psfin == True and shovel == nobleshovel and cdf == True and wb1 == True and wb2 == True and carfin == True and magicfin == True and tridentfin == True and GAMEDONE == False and pet in petc4:
        GAMEDONE = True

    if GAMEDONE == True:
        print(fore.GREEN + "You Have Completed The Game!\n" + "\033[0;00m")

    if len(inventory) != 0:
        print("Inventory:", ", ".join(inventory))
    else:
        print("Inventory: Nothing")
    print("Inventory Space: {}".format(invs))
    print("Xp: {}".format(xp))
    print("Level: {}".format(level))
    print("Balance: {}".format(str(bal)) + "$")
    print("Shovel: {}".format(ss))
    print("Rank: {}".format(rank))
    print("Session: {}".format(session))
    if pet != None:
        print("Pet: Level {} {}".format(pl, pet))
    else:
        print("Pet: No Pet")

    """    
    print("\n1: Dig")
    print("2: Sell")
    print("3: Shop")
    print("4: Rarities")
    print("5: Mystery Box")
    print("6: Museum")
    print("7: Market")
    print("8: Market Values")
    print("9: Contracts")
    print("10: Levels Shop")
    print("11: Pet Shop")
    print("12: Profile\n")
    print("13: Save And Exit\n")
    """

    print(f"""
1: Dig               8: Market Values   
2: Sell              9: Contracts       
3: Shop              10: Levels Shop    
4: Rarities          11: Pet Shop       
5: Mystery Box       12: Nuke Shop        
6: Museum            13: View Profile
7: Market            14: Save And Exit\n""")

    q = input("Option: ")

    if q == "1":

        if len(inventory) != invs:

            xp += 1

            item = choice(rewards)

            chances = randint(0, psr)

            if chances == 1:
                item = "Prehistoric Spear"

            chances1 = randint(0, 100000)

            if chances1 == 1:
                print("You Found A Very Ancient Dragon Skeleton")
                wait(TIME)
                print("Nothing Is Greater Than This")
                wait(TIME)
                print(fore.GREEN + "You Win")
                quit()

            if item != "Nothing":

                cd()

                print("You Found A", item)

                c = randint(1, 5)

                tchance = randint(1, 10)

                if tchance == 1:
                    c = 2
                    wait(TIME)
                    print("Oh No! There Was A Trap With This Item")
                    wait(TIME)
                    print("You Lost 10% Of Your Money!")
                    bal -= C(bal * 0.1)

                if c == 1:
                    wait(TIME)
                    print("This Item Had Special Powers!")
                    wait(TIME)
                    print("\nPick A Powerup:\n\n1: +5 Hp\n2: Bigger Inventory\n3: 1000$")
                    
                    q = input("\nOption: ")

                    if q == "1":
                        ahp += 5

                        print("Good One")

                    if q == "2":
                        if invs != 9:
                            invs += 1
                            print("Awesome!")

                        else:
                            print("You Already Have Max Inventory!")

                    if q == "3":
                        bal += 1000

                        print("Nice")
                
                inventory.append(item)

                if item == "Shoe":
                    shoe = shoe + 1

                if item == "Diamond":
                    diamond = diamond + 1

                if item == "Can":
                    can = can + 1

                if item == "Candy Wrapper":
                    candywrapper = candywrapper + 1

                if item == "Bottle Cap":
                    bottlecap = bottlecap + 1

                if item == "Car Tire":
                    cartire = cartire + 1

                if item == "Car":
                    car = car + 1

                if item == "Magic Bean":
                    magicbean = magicbean + 1

                if item == "Trident":
                    trident = trident + 1

                if item == "Prehistoric Spear":
                    ps = ps + 1

                if item == "Dinosaur Bone":
                    dinosaurbone = dinosaurbone + 1
                    dino = choice(dinos)

                    if dino == "raptor":
                        raptor = raptor + 1

                    if dino == "trex":
                        trex = trex + 1

                    if dino == "triceratops":
                        tricera = tricera + 1

                    if dino == "stegasaurus":
                        steg = steg + 1

                    if dino == "spinosaurus":
                        spino = spino + 1

                    if dino == "allosaurus":
                        allo = allo + 1

                    if dino == "pterodactyl":
                        ptero = ptero + 1

                wait(TIME)

                clear()
                main()

            else:
                cd()
                print("You Found", item)
                wait(TIME)

                clear()
                main()

        else:
            print("You Have Max Inventory!")
            wait(TIME)
            clear()
            main()

    if q == "2":

        itm = input("Type 'all' To Sell All Items\nItem To Sell (Item Number In List): ")
        x = []
        for i in range(invs):
            x.append(str(i + 1))

        if itm != "all":

            if itm in x:
                itm = int(itm)
                try:
                    sell = inventory[itm - 1]
        
                    if sell == "Shoe":
                        inventory.remove(sell)
                        bal = bal + 50 + shovel.value + pav
                        print("You Sold Your", sell, "For", 50 + shovel.value + pav, "Dollars!")
                        wait(3)
                        clear()
                        main()
            
                    if sell == "Diamond":
                        inventory.remove(sell)
                        bal = bal + 500 + shovel.value + pav
                        print("You Sold Your", sell, "For", 500 + shovel.value + pav, "Dollars!")
                        wait(3)
                        clear()
                        main()
        
                    if sell == "Dinosaur Bone":
                        inventory.remove(sell)
                        bal = bal + 1000 + shovel.value + pav
                        print("You Sold Your", sell, "For", 1000 + shovel.value + pav, "Dollars!")
                        wait(3)
                        clear()
                        main()
        
                    if sell == "Can":
                        inventory.remove(sell)
                        bal = bal + 10 + shovel.value + pav
                        print("You Sold Your", sell, "For", 10 + shovel.value + pav, "Dollars!")
                        wait(3)
                        clear()
                        main()
        
                    if sell == "Candy Wrapper":
                        inventory.remove(sell)
                        bal = bal + 1 + shovel.value + pav
                        print("You Sold Your", sell, "For", 1 + shovel.value + pav, "Dollars!")
                        wait(3)
                        clear()
                        main()
        
                    if sell == "Bottle Cap":
                        inventory.remove(sell)
                        bal = bal + 5 + shovel.value + pav
                        print("You Sold Your", sell, "For", 5 + shovel.value + pav, "Dollars!")
                        wait(3)
                        clear()
                        main()
        
                    if sell == "Car Tire":
                        inventory.remove(sell)
                        bal = bal + 100 + shovel.value + pav
                        print("You Sold Your", sell, "For", 100 + shovel.value + pav, "Dollars!")
                        wait(3)
                        clear()
                        main()

                    if sell == "Car":
                        inventory.remove(sell)
                        bal = bal + 750 + shovel.value + pav
                        print("You Sold Your", sell, "For", 750 + shovel.value + pav, "Dollars!")
                        wait(3)
                        clear()
                        main()    

                    if sell == "Magic Bean":
                        inventory.remove(sell)
                        bal = bal + 150 + shovel.value + pav
                        print("You Sold Your", sell, "For", 150 + shovel.value + pav, "Dollars!")
                        wait(3)
                        clear()
                        main()

                    if sell == "Trident":
                        inventory.remove(sell)
                        bal = bal + 1500 + shovel.value + pav
                        print("You Sold Your", sell, "For", 1500 + shovel.value + pav, "Dollars!")
                        wait(3)
                        clear()
                        main()
        
                    if sell == "Prehistoric Spear":
                        inventory.remove(sell)
                        bal = bal + 10000 + shovel.value + pav
                        print("You Sold Your", sell, "For", 10000 + shovel.value + pav, "Dollars!")
                        wait(3)
                        clear()
                        main()
        
                    if sell == "Planetary Core":
                        print("Ha! Can't Sell That!")
                        wait(3)
                        clear()
                        main()
    
                except:
                    print("Index Out Of Range")
                    wait(TIME)
                    clear()
                    main()
    
            else:
                print("Invalid Input")
                wait(TIME)
                clear()
                main()

        else:
            x = 0
            y = 0
            for i in inventory:
                if i == "Shoe":                    
                    bal = bal + 50 + shovel.value + pav
                    x = x + 50 + shovel.value + pav
        
                if i == "Diamond":                  
                    bal = bal + 500 + shovel.value + pav
                    x = x + 500 + shovel.value + pav
    
                if i == "Dinosaur Bone":                   
                    bal = bal + 1000 + shovel.value + pav
                    x = x + 1000 + shovel.value + pav
    
                if i == "Can":                   
                    bal = bal + 10 + shovel.value + pav
                    x = x + 10 + shovel.value + pav
        
                if i == "Candy Wrapper":                   
                    bal = bal + 1 + shovel.value + pav
                    x = x + 1 + shovel.value + pav
        
                if i == "Bottle Cap":                   
                    bal = bal + 5 + shovel.value + pav
                    x = x + 5 + shovel.value + pav
        
                if i == "Car Tire":                   
                    bal = bal + 100 + shovel.value + pav
                    x = x + 100 + shovel.value + pav

                if i == "Car":                   
                    bal = bal + 750 + shovel.value + pav
                    x = x + 750 + shovel.value + pav

                if i == "Magic Bean":                   
                    bal = bal + 150 + shovel.value + pav
                    x = x + 150 + shovel.value + pav

                if i == "Trident":                   
                    bal = bal + 1500 + shovel.value + pav
                    x = x + 1500 + shovel.value + pav
        
                if i == "Prehistoric Spear":                   
                    bal = bal + 10000 + shovel.value + pav
                    x = x + 10000 + shovel.value + pav

                y += 1

            inventory.clear()
            print("{} Items Sold For {}$".format(y, x))
            wait(TIME)
            clear()
            main()

    if q == "3":
        clear()
        print("Balance: {}\n".format(bal))
        print("Every New Shovel Makes Digging 0.05 Less Time\n")
        print("1: Better Shovel - Increases Sell Values By 10 Dollars - Price: 200$")
        print("2: Great Shovel - Increases Sell Values By 20 Dollars - Price: 750$")
        print("3: Mega Shovel - Increases Sell Values By 40 Dollars - Price: 1500$")
        print("4: Ultra Shovel - Increases Sell Values By 70 Dollars - Price: 4000$")
        print("5: Super Shovel - Increases Sell Values By 100 Dollars - Price: 7000$")
        print("6: Superior Shovel - Increases Sell Values By 120 Dollars - Price: 10000$")
        print("7: Remarkable Shovel - Increases Sell Values By 150 Dollars - Price: 13000$")
        print("8: Extraordinary Shovel - Increases Sell Values By 170 Dollars - Price: 15000$")
        print("9: Finist Shovel - Increases Sell Values By 200 Dollars - Price: 18000$")
        print("10: Noble Shovel - Increases Sell Values By 220 Dollars - Price: 20000$")
        print("11: Rarity Changer - Changes Rarity Of An Item - Price: 20000$")
        print("12: Bigger Inventory - Increases The Max Inventory Space By 1 - Price: 200$")
        print("13: Speed Dig - Increases The Speed Of Digging - Price: 10000$")
        print("14: Less Chance Of Finding Nothing - Price: 5000$")
        print("15: Backpack - Lets You Store 4 More Than Max Inventory - Price: 10000$")
        print("16: Go Back\n")

        buy = input("Option: ")

        if buy == "1": 
            if bal >= 200 and shovel != bettershovel:
                shovel = bettershovel
                bal = bal - 200
                ss = "Better Shovel"
                rank = "Learning Digger"
                digspeed -= 0.05

                print("Congrats You Bought A Better Shovel!")

                wait(TIME)
                clear()
                main()

            elif bal < 200:
                print("That Shovel Is To Expensive!")
                wait(TIME)
                clear()
                main()

            elif shovel == bettershovel:
                print("You Already Have That Shovel!")
                wait(TIME)
                clear()
                main()

        if buy == "2": 
            if bal >= 750 and shovel != greatshovel:
                shovel = greatshovel
                bal = bal - 750
                ss = "Great Shovel"
                rank = "Experienced Digger"
                digspeed -= 0.05

                print("Congrats You Bought A Great Shovel!")

                wait(TIME)
                clear()
                main()

            elif bal < 750:
                print("That Shovel Is To Expensive!")
                wait(TIME)
                clear()
                main()

            elif shovel == bettershovel:
                print("You Already Have That Shovel!")
                wait(TIME)
                clear()
                main()

        if buy == "3":
            if bal >= 1500 and shovel != megashovel:
                shovel = megashovel
                bal = bal - 1500
                ss = "Mega Shovel"
                rank = "Smart Digger"
                digspeed -= 0.05

                print("Congrats You Bought A Mega Shovel!")

                wait(TIME)
                clear()
                main()

            elif bal < 1500:
                print("That Shovel Is To Expensive!")
                wait(TIME)
                clear()
                main()

            elif shovel == bettershovel:
                print("You Already Have That Shovel!")
                wait(TIME)
                clear()
                main()

        if buy == "4": 
            if bal >= 4000 and shovel != ultrashovel:
                shovel = ultrashovel
                bal = bal - 4000
                ss = "Ultra Shovel"
                rank = "Super Good Digger"
                digspeed -= 0.05

                print("Congrats You Bought An Ultra Shovel!")

                wait(TIME)
                clear()
                main()

            elif bal < 4000:
                print("That Shovel Is To Expensive!")
                wait(TIME)
                clear()
                main()

            elif shovel == bettershovel:
                print("You Already Have That Shovel!")
                wait(TIME)
                clear()
                main()

        if buy == "5": 
            if bal >= 7000 and shovel != supershovel:
                shovel = supershovel
                bal = bal - 7000
                ss = "Super Shovel"
                rank = "Supreme Digger"
                digspeed -= 0.05

                print("Congrats You Bought A Super Shovel!")

                wait(TIME)
                clear()
                main()

            elif bal < 7000:
                print("That Shovel Is To Expensive!")
                wait(TIME)
                clear()
                main()

            elif shovel == bettershovel:
                print("You Already Have That Shovel!")
                wait(TIME)
                clear()
                main()

        if buy == "6": 
            if bal >= 10000 and shovel != superiorshovel:
                shovel = superiorshovel
                bal = bal - 10000
                ss = "Superior Shovel"
                rank = "Senior Digger"
                digspeed -= 0.05

                print("Congrats You Bought A Superior Shovel!")

                wait(TIME)
                clear()
                main()

            elif bal < 10000:
                print("That Shovel Is To Expensive!")
                wait(TIME)
                clear()
                main()

            elif shovel == superiorshovel:
                print("You Already Have That Shovel!")
                wait(TIME)
                clear()
                main()

        if buy == "7": 
            if bal >= 13000 and shovel != remarkableshovel:
                shovel = remarkableshovel
                bal = bal - 13000
                ss = "Remarkable Shovel"
                rank = "Unforgettable Digger"
                digspeed -= 0.05

                print("Congrats You Bought A Remarkable Shovel!")

                wait(TIME)
                clear()
                main()

            elif bal < 13000:
                print("That Shovel Is To Expensive!")
                wait(TIME)
                clear()
                main()

            elif shovel == remarkableshovel:
                print("You Already Have That Shovel!")
                wait(TIME)
                clear()
                main()

        if buy == "8": 
            if bal >= 15000 and shovel != extraordinaryshovel:
                shovel = extraordinaryshovel
                bal = bal - 15000
                ss = "Extraordinary Shovel"
                rank = "Exceptional Digger"
                digspeed -= 0.05

                print("Congrats You Bought A Extraordinary Shovel!")

                wait(TIME)
                clear()
                main()

            elif bal < 15000:
                print("That Shovel Is To Expensive!")
                wait(TIME)
                clear()
                main()

            elif shovel == extraordinaryshovel:
                print("You Already Have That Shovel!")
                wait(TIME)
                clear()
                main()

        if buy == "9": 
            if bal >= 18000 and shovel != finistshovel:
                shovel = finistshovel
                bal = bal - 18000
                ss = "Finist Shovel"
                rank = "Exquisite Digger"
                digspeed -= 0.05

                print("Congrats You Bought The Finist Shovel!")

                wait(TIME)
                clear()
                main()

            elif bal < 18000:
                print("That Shovel Is To Expensive!")
                wait(TIME)
                clear()
                main()

            elif shovel == finistshovel:
                print("You Already Have That Shovel!")
                wait(TIME)
                clear()
                main()

        if buy == "10": 
            if bal >= 20000 and shovel != nobleshovel:
                shovel = nobleshovel
                bal = bal - 20000
                ss = "Noble Shovel"
                rank = "The Greatest Digger"
                digspeed -= 0.05

                print("Congrats You Bought The Noble Shovel!")

                wait(TIME)
                clear()
                main()

            elif bal < 20000:
                print("That Shovel Is To Expensive!")
                wait(TIME)
                clear()
                main()

            elif shovel == nobleshovel:
                print("You Already Have That Shovel!")
                wait(TIME)
                clear()
                main()

        if buy == "11":
            if bal >= 20000:
                bal = bal - 20000
                clear()
                print("Careful! If You Dont Type Any Of The Options Or Do Option 8, You Will Lose The Money Spent On This Rarity Changer!\n")
                print("1: Change Rarity Of Shoe")
                print("2: Change Rarity Of Bottle Cap")
                print("3: Change Rarity Of Can")
                print("4: Change Rarity Of Candy Wrapper")
                print("5: Change Rarity Of Car Tire")
                print("6: Change Rarity Of Diamond")
                print("7: Change Rarity Of Dinosaur Bone")
                print("8: Change Rarity Of Prehistoric Spear")
                print("9: Change Rarity Of Car")
                print("10: Change Rarity Of Magic Bean")
                print("11: Change Rarity Of Trident")
                print("\n12: Go Back\n")

                rare = input("Option: ")

                if rare == "1":
                    rewards.append("Shoe")
                    print("Congrats You Changed The Rarity Of Shoe!")
                    wait(TIME)
                    clear()
                    main()

                if rare == "2":
                    rewards.append("Bottle Cap")
                    print("Congrats You Changed The Rarity Of Bottle Cap!")
                    wait(TIME)
                    clear()
                    main()

                if rare == "3":
                    rewards.append("Can")
                    print("Congrats You Changed The Rarity Of Can!")
                    wait(TIME)
                    clear()
                    main()

                if rare == "4":
                    rewards.append("Candy Wrapper")
                    print("Congrats You Changed The Rarity Of Candy Wrapper!")
                    wait(TIME)
                    clear()
                    main()

                if rare == "5":
                    rewards.append("Car Tire")
                    print("Congrats You Changed The Rarity Of Car Tire!")
                    wait(TIME)
                    clear()
                    main()

                if rare == "6":
                    rewards.append("Diamond")
                    print("Congrats You Changed The Rarity Of Diamond!")
                    wait(TIME)
                    clear()
                    main()

                if rare == "7":
                    rewards.append("Dinosaur Bone")
                    print("Congrats You Changed The Rarity Of Dinosaur Bone!")
                    wait(TIME)
                    clear()
                    main()

                if rare == "8":
                    if psr != 1:
                        psr -= 20
                        print("Congrats You Changed The Rarity Of Prehistoric Spear!")
                        wait(TIME)
                        clear()
                        main()

                    else:
                        print("Prehistoric Spear Has A 100% Chance Of Being Found")
                        wait(TIME)
                        clear()
                        main()

                if rare == "9":
                    rewards.append("Car")
                    print("Congrats You Changed The Rarity Of Car!")
                    wait(TIME)
                    clear()
                    main()

                if rare == "10":
                    rewards.append("Magic Bean")
                    print("Congrats You Changed The Rarity Of Magic Bean!")
                    wait(TIME)
                    clear()
                    main()

                if rare == "11":
                    rewards.append("Trident")
                    print("Congrats You Changed The Rarity Of Trident!")
                    wait(TIME)
                    clear()
                    main()

                if rare == "12":
                    clear()
                    main()

                else:
                    print("Invalid Input!")
                    wait(TIME)
                    clear()
                    main()

            else:
                print("Not Enough!")
                wait(TIME)
                clear()
                main()

        if buy == "12":
            if bal >= 200 and invs != 9:
                bal = bal - 200

                invs = invs + 1
                print("Congrats You Bought A Bigger Inventory!")
                wait(TIME)
                clear()
                main()

            elif invs >= 9:
                print("Max Inventory Limit Reached!")
                wait(TIME)
                clear()
                main()

            else:
                print("Not Enough!")
                wait(TIME)
                clear()
                main()

        if buy == "13":
            if bal >= 10000 and cdf == False:
                cdf = True
                bal = bal - 10000
                digspeed -= 0.5

                print("Congrats! You Bought Speed Dig!")
                wait(TIME)
                clear()
                main()

            elif cdf == True:
                print("You Already Have Speed Dig")
                wait(TIME)
                clear()
                main()

            else:
                print("Too Expensive")
                wait(TIME)
                clear()
                main()

        if buy == "14":
            if bal >= 5000:
                x = 0
                for i in rewards:
                    if i == "Nothing":
                        rewards.pop(x)
                    x += 1
                bal -= 5000
                print("Done!")
                wait(TIME)
                clear()
                main()
            else:
                print("Not Enough")
                wait(TIME)
                clear()
                main()

        if buy == "15":
            if bbpf == False and bal >= 10000:
                bbpf = True
                invs += 4
                bal -= 10000
                print("You Bought A Backpack!")
                wait(TIME)
                clear()
                main()

            elif bbpf == True:
                print("You Already Bought That")
                wait(TIME)
                clear()
                main()

            elif bal < 10000:
                print("Not Enough")
                wait(TIME)
                clear()
                main()
        
        if buy == "16":
            clear()
            main()

        else:
            print("Invalid Input")
            wait(TIME)
            clear()
            main()

    if q == "4":
        clear()
        print("Nothing Rarity: {}% - Very Common".format(round((rewards.count("Nothing") / len(rewards)) * 100)))
        print("Shoe Rarity: {}% - {}Common{}".format(round((rewards.count("Shoe") / len(rewards)) * 100), fore.GREEN, fore.RESET))
        print("Bottle Cap Rarity: {}% - {}Common{}".format(round((rewards.count("Bottle Cap") / len(rewards)) * 100), fore.GREEN, fore.RESET))
        print("Can Rarity: {}% - {}Uncommon{}".format(round((rewards.count("Can") / len(rewards)) * 100), fore.BLUE, fore.RESET))
        print("Magic Bean Rarity: {}% - {}Uncommon{}".format(round((rewards.count("Magic Bean") / len(rewards)) * 100), fore.BLUE, fore.RESET))
        print("Candy Wrapper Rarity: {}% - {}Uncommon{}".format(round((rewards.count("Candy Wrapper") / len(rewards)) * 100), fore.BLUE, fore.RESET))
        print("Car Tire Rarity: {}% - {}Rare{}".format(round((rewards.count("Car Tire") / len(rewards)) * 100), fore.RED, fore.RESET))
        print("Diamond Rarity: {}% - {}Rare{}".format(round((rewards.count("Diamond") / len(rewards)) * 100), fore.RED, fore.RESET))
        print("Car Rarity: {}% - {}Rare{}".format(round((rewards.count("Car") / len(rewards)) * 100), fore.RED, fore.RESET))
        print("Dinosaur Bone Rarity: {}% - {}Epic{}".format(round((rewards.count("Dinosaur Bone") / len(rewards)) * 100), fore.MAGENTA, fore.RESET))
        print("Trident Rarity: {}% - {}Epic{}".format(round((rewards.count("Trident") / len(rewards)) * 100), fore.MAGENTA, fore.RESET))
        print("Prehistoric Spear Rarity: {}% - {}Legendary{}".format(round(1 / psr * 100), fore.YELLOW, fore.RESET))

        input("\n[ENTER]")
        clear()
        main()

    if q == "5":
        clear()
        print("Balance: {}\n".format(bal))
        print("1: Normal Mystery Box - Price: 100$")
        print("2: Good Mystery Box - Price: 250$")
        print("3: Mega Mystery Box - Price: 1000$")
        print("4: Ultimate Mystery Box - Price: 5000$")
        print("5: Optimum Mystery Box - Price: 10000$")
        print("6: Apex Mystery Box - Price: 13000$")
        print("7: Epitome Mystery Box - Price: 17000$")
        print("8: Go Back\n")

        box = input("Option: ")

        if box == "1":
            if bal >= 100:

                boxreward = choice(normalbox)
                bal = bal - 100

                if boxreward == "Can":
                    if invs == 9 or bbpf == True:
                        inventory.append("Can")
                        print("You Opened The Normal Mystery Box And Got A Can!")
                        wait(3)
                        clear()
                        main()

                    else:
                        print("Can But You Have Max Inventory!")
                        print("You Recieved A 100$ Refund")
                        bal += 100
                        wait(TIME)
                        clear()
                        main()

                if boxreward == "500$":
                    bal = bal + 500
                    print("You Opened The Normal Mystery Box And Got 500$!")
                    wait(3)
                    clear()
                    main()

                if boxreward == "Candy Wrapper":
                    if len(inventory) < invs:
                        inventory.append("Candy Wrapper")
                        print("You Opened The Normal Mystery Box And Got A Candy Wrapper!")
                        wait(3)
                        clear()
                        main()

                    else:
                        print("Candy Wrapper But You Have Max Inventory!")
                        print("You Recieved A 100$ Refund")
                        bal += 100
                        wait(TIME)
                        clear()
                        main()

                if boxreward == "Bottle Cap":
                    inventory.append("Bottle Cap")
                    print("You Opened The Normal Mystery Box And Got A Bottle Cap!")
                    wait(3)
                    clear()
                    main()

            else:
                print("You Dont Have Enough!")
                wait(TIME)
                clear()
                main()

        if box == "2":
            if bal >= 250:

                boxreward = choice(goodbox)
                bal = bal - 250

                if boxreward == "Car Tire":
                    if len(inventory) < invs:
                        inventory.append("Car Tire")
                        print("You Opened The Good Mystery Box And Got A Car Tire!")
                        wait(3)
                        clear()
                        main()

                    else:
                        print("Car Tire But You Have Max Inventory!")
                        print("You Recieved A 250$ Refund")
                        bal += 250
                        wait(TIME)
                        clear()
                        main()

                if boxreward == "1000$":
                    bal = bal + 1000
                    print("You Opened The Good Mystery Box And Got 1000$!")
                    wait(3)
                    clear()
                    main()

                if boxreward == "Nothing":
                    print("You Opened The Good Mystery Box And Got Nothing!")
                    wait(3)
                    clear()
                    main()

                if boxreward == "Diamond":
                    if len(inventory) < invs:
                        inventory.append("Diamond")
                        print("You Opened The Good Mystery Box And Got A Diamond!")
                        wait(3)
                        clear()
                        main()

                    else:
                        print("Diamond But You Have Max Inventory!")
                        print("You Recieved A 250$ Refund")
                        bal += 250
                        wait(TIME)
                        clear()
                        main()

            else:
                print("You Dont Have Enough!")
                wait(TIME)
                clear()
                main()

        if box == "3":
            if bal >= 1000:

                boxreward = choice(megabox)
                bal = bal - 1000

                if boxreward == "Better Shovel":
                    shovel = bettershovel
                    ss = "Better Shovel"
                    print("You Opened The Mega Mystery Box And Got A Better Shovel!")
                    wait(3)
                    clear()
                    main()

                if boxreward == "2000$":
                    bal = bal + 2000
                    print("You Opened The Mega Mystery Box And Got 2000$!")
                    wait(3)
                    clear()
                    main()

                if boxreward == "Great Shovel":
                    shovel = greatshovel
                    ss = "Great Shovel"
                    print("You Opened The Mega Mystery Box And Got A Great Shovel!")
                    wait(3)
                    clear()
                    main()

            else:
                print("You Dont Have Enough!")
                wait(TIME)
                clear()
                main()

        if box == "4":
            if bal >= 5000:

                boxreward = choice(ultimatebox)
                bal = bal - 5000

                if boxreward == "Mega Shovel":
                    shovel = megashovel
                    ss = "Mega Shovel"
                    print("You Opened The Ultimate Mystery Box And Got A Mega Shovel!")
                    wait(3)
                    clear()
                    main()

                if boxreward == "4000$":
                    bal = bal + 4000
                    print("You Opened The Ultimate Mystery Box And Got 4000$!")
                    wait(3)
                    clear()
                    main()

                if boxreward == "Super Shovel":
                    shovel = supershovel
                    ss = "Super Shovel"
                    print("You Opened The Ultimate Mystery Box And Got A Super Shovel!")
                    wait(3)
                    clear()
                    main()

                if boxreward == "Dinosaur Bone":
                    if len(inventory) < invs:
                        inventory.append("Dinosaur Bone")
                        print("You Opened The Ultimate Mystery Box And Got A Dinosaur Bone!")
                        wait(3)
                        clear()
                        main()

                    else:
                        print("Dinosaur Bone But You Have Max Inventory!")
                        print("You Recieved A 5000$ Refund")
                        bal += 5000
                        wait(TIME)
                        clear()
                        main()

            else:
                print("You Dont Have Enough!")
                wait(TIME)
                clear()
                main()

        if box == "5":
            if bal >= 10000:

                boxreward = choice(optimumbox)
                bal = bal - 10000

                if boxreward == "Superior Shovel":
                    shovel = superiorshovel
                    ss = "Superior Shovel"
                    print("You Opened The Optimum Mystery Box And Got A Superior Shovel!")
                    wait(3)
                    clear()
                    main()

                if boxreward == "8000$":
                    bal = bal + 8000
                    print("You Opened The Optimum Mystery Box And Got 8000$!")
                    wait(3)
                    clear()
                    main()

                if boxreward == "5 T-Rex Bones":
                    trex += 5
                    print("You Opened The Optimum Mystery Box And Got 5 T-Rex Bones!")
                    wait(3)
                    clear()
                    main()

                if boxreward == "Prehistoric Spear":
                    if len(inventory) < invs:
                        inventory.append("Prehistoric Spear")
                        print("You Opened The Ultimate Mystery Box And Got A Prehistoric Spear!")
                        wait(3)
                        clear()
                        main()

                    else:
                        print("Prehistoric Spear But You Have Max Inventory!")
                        print("You Recieved A 10000$ Refund")
                        bal += 10000
                        wait(TIME)
                        clear()
                        main()

            else:
                print("You Dont Have Enough!")
                wait(TIME)
                clear()
                main()

        if box == "6":
            if bal >= 13000:

                boxreward = choice(apexbox)
                bal = bal - 13000

                if boxreward == "Remarkable Shovel":
                    shovel = remarkableshovel
                    ss = "Remarkable Shovel"
                    print("You Opened The Apex Mystery Box And Got A Remarkable Shovel!")
                    wait(3)
                    clear()
                    main()

                if boxreward == "Extraordinary Shovel":
                    shovel = extraordinaryshovel
                    ss = "Extraordinary Shovel"
                    print("You Opened The Apex Mystery Box And Got A Extraordinary Shovel!")
                    wait(3)
                    clear()
                    main()

                if boxreward == "+20 Hp":
                    ahp += 20
                    print("You Opened The Apex Mystery Box And Got 20 More Hp!")
                    wait(3)
                    clear()
                    main()

            else:
                print("You Dont Have Enough!")
                wait(TIME)
                clear()
                main()

        if box == "7":
            if bal >= 17000:

                boxreward = choice(epitomebox)
                bal = bal - 17000

                if boxreward == "Finist Shovel":
                    shovel = finistshovel
                    ss = "Finist Shovel"
                    print("You Opened The Epitome Mystery Box And Got The Finist Shovel!")
                    wait(3)
                    clear()
                    main()

                if boxreward == "20000$":
                    bal = bal + 20000
                    print("You Opened The Epitome Mystery Box And Got 8000$!")
                    wait(3)
                    clear()
                    main()

                if boxreward == "2 Prehistoric Spears":
                    if len(inventory) <= (invs - 2):
                        for i in range(2):
                            inventory.append("Prehistoric Spear")
                        print("You Opened The Epitome Mystery Box And Got 2 Prehistoric Spears!")
                        wait(3)
                        clear()
                        main()

                    else:
                        print("2 Prehistoric Spears But You Have Max Inventory!")
                        print("You Recieved A 17000$ Refund")
                        bal += 17000
                        wait(TIME)
                        clear()
                        main()

            else:
                print("You Dont Have Enough!")
                wait(TIME)
                clear()
                main()

        if box == "8":
            clear()
            main()

        else:
            print("Invalid Input!")
            wait(TIME)
            clear()
            main()

    if q == "6":
        clear()
        print("1: Raptor: {}/10".format(raptor))
        print("2: Triceratops: {}/20".format(tricera))
        print("3: Stegosaurus: {}/25".format(steg))
        print("4: T-Rex: {}/30".format(trex))
        print("5: Spinosaurus: {}/35".format(spino))
        print("6: Allosaurus: {}/40".format(allo))
        print("7: Pterodactyl: {}/45".format(ptero))
        print("8: Go Back")

        mue = input("\nFinish Which One: ")

        if mue == "1":
            if raptor >= 10 and raptorfin == False:
                raptorfin = True
                bal = bal + 10000
                print("Raptor Skeleton Done!")
                print("You've Recieved 10000 Dollars!")
                wait(TIME)
                clear()
                main()

            elif raptorfin == True:
                print("You've Already Finished This Dinosaur!")
                wait(TIME)
                clear()
                main()

            elif raptor < 10:
                print("Not Enough Bones!")
                wait(TIME)
                clear()
                main()    

        if mue == "2":
            if tricera >= 20 and tricerafin == False:
                tricerafin = True
                bal = bal + 15000
                print("Triceratops Skeleton Done!")
                print("You've Recieved 15000 Dollars!")
                wait(TIME)
                clear()
                main()

            elif tricerafin == True:
                print("You've Already Finished This Dinosaur!")
                wait(TIME)
                clear()
                main()

            elif tricera < 20:
                print("Not Enough Bones!")
                wait(TIME)
                clear()
                main()

        if mue == "3":
            if steg >= 25 and stegfin == False:
                stegfin = True
                bal = bal + 20000
                print("Stegasaurus Skeleton Done!")
                print("You've Recieved 20000 Dollars!")
                wait(TIME)
                clear()
                main()

            elif tricerafin == True:
                print("You've Already Finished This Dinosaur!")
                wait(TIME)
                clear()
                main()

            elif tricera < 25:
                print("Not Enough Bones!")
                wait(TIME)
                clear()
                main()

        if mue == "4":
            if trex >= 30 and trexfin == False:
                trexfin = True
                bal = bal + 30000
                print("T-Rex Skeleton Done!")
                print("You've Recieved 30000 Dollars!")
                wait(TIME)
                clear()
                main()

            elif trexfin == True:
                print("You've Already Finished This Dinosaur!")
                wait(TIME)
                clear()
                main()

            elif trex < 30:
                print("Not Enough Bones!")
                wait(TIME)
                clear()
                main()

        if mue == "5":
            if spino >= 35 and spinofin == False:
                spinofin = True
                bal = bal + 35000
                print("Spinosaurus Skeleton Done!")
                print("You've Recieved 35000 Dollars!")
                wait(TIME)
                clear()
                main()

            elif spinofin == True:
                print("You've Already Finished This Dinosaur!")
                wait(TIME)
                clear()
                main()

            elif spino < 30:
                print("Not Enough Bones!")
                wait(TIME)
                clear()
                main()

        if mue == "6":
            if allo >= 40 and allofin == False:
                allofin = True
                bal = bal + 40000
                print("Allosaurus Skeleton Done!")
                print("You've Recieved 35000 Dollars!")
                wait(TIME)
                clear()
                main()

            elif allofin == True:
                print("You've Already Finished This Dinosaur!")
                wait(TIME)
                clear()
                main()

            elif allo < 30:
                print("Not Enough Bones!")
                wait(TIME)
                clear()
                main()

        if mue == "4":
            if ptero >= 45 and pterofin == False:
                trexfin = True
                bal = bal + 45000
                print("Pterodactyl Skeleton Done!")
                print("You've Recieved 40000 Dollars!")
                wait(TIME)
                clear()
                main()

            elif pterofin == True:
                print("You've Already Finished This Dinosaur!")
                wait(TIME)
                clear()
                main()

            elif ptero < 30:
                print("Not Enough Bones!")
                wait(TIME)
                clear()
                main()

        if mue == "8":
            clear()
            main()

        else:
            print("Invalid Input")
            wait(TIME)
            clear()
            main()

    if q == "7":
        clear()
        market = choice(mo)
        price = randint(200, 900)
        market1 = choice(mo)
        price1 = randint(200, 900)
        market2 = choice(mo)
        price2 = randint(200, 900)

        print("1: {}: {}$".format(market, price))
        print("2: {}: {}$".format(market1, price1))
        print("3: {}: {}$".format(market2, price2))
        print("4: Go Back\n")

        x = input("Option: ")

        if x == "1":
            if len(inventory) < invs:
                if bal >= price:
                    bal = bal - price
                    inventory.append(market)
                    print("You Bought The {} For {}$".format(market, price))
    
                    if market == "Dinosaur Bone":
                        dino = choice(dinos)
    
                        if dino == "raptor":
                            raptor = raptor + 1
    
                        if dino == "trex":
                            trex = trex + 1
    
                        if dino == "triceratops":
                            tricera = tricera + 1
    
                        if dino == "stegasaurus":
                            steg = steg + 1

                        if dino == "spinosaurus":
                            spino = spino + 1

                        if dino == "allosaurus":
                            allo = allo + 1

                        if dino == "pterodactyl":
                            ptero = ptero + 1
    
                    wait(TIME)
                    clear()
                    main()
    
                else:
                    print("Too Expensive!")
                    wait(TIME)
                    clear()
                    main()

            else:
                print("Max Inventory!")
                wait(TIME)
                clear()
                main()

        if x == "2":
            if len(inventory) < invs:
                if bal >= price1:
                    bal = bal - price1
                    inventory.append(market1)
                    print("You Bought The {} For {}$".format(market1, price1))
    
                    if market1 == "Dinosaur Bone":
                        dino = choice(dinos)
    
                        if dino == "raptor":
                            raptor = raptor + 1
    
                        if dino == "trex":
                            trex = trex + 1
    
                        if dino == "triceratops":
                            tricera = tricera + 1
    
                        if dino == "stegasaurus":
                            steg = steg + 1

                        if dino == "spinosaurus":
                            spino = spino + 1

                        if dino == "allosaurus":
                            allo = allo + 1

                        if dino == "pterodactyl":
                            ptero = ptero + 1
    
                    wait(TIME)
                    clear()
                    main()
    
                else:
                    print("Too Expensive!")
                    wait(TIME)
                    clear()
                    main()

            else:
                print("Max Inventory!")
                wait(TIME)
                clear()
                main()

        if x == "3":
            if len(inventory) < invs:
                if bal >= price2:
                    bal = bal - price2
                    inventory.append(market2)
                    print("You Bought The {} For {}$".format(market2, price2))
    
                    if market2 == "Dinosaur Bone":
                        dino = choice(dinos)
    
                        if dino == "raptor":
                            raptor = raptor + 1
    
                        if dino == "trex":
                            trex = trex + 1
    
                        if dino == "triceratops":
                            tricera = tricera + 1
    
                        if dino == "stegasaurus":
                            steg = steg + 1

                        if dino == "spinosaurus":
                            spino = spino + 1

                        if dino == "allosaurus":
                            allo = allo + 1

                        if dino == "pterodactyl":
                            ptero = ptero + 1
    
                    wait(TIME)
                    clear()
                    main()
    
                else:
                    print("Too Expensive!")
                    wait(TIME)
                    clear()
                    main()

            else:
                print("Max Inventory!")
                wait(TIME)
                clear()
                main()

        if x == "4":
            clear()
            main()

        else:
            print("Invalid Input!")
            wait(TIME)
            clear()
            main()

    if q == "8":
        clear()
        print("""Candy Wrapper: 1$
Bottle Cap: 5$
Can: 10$
Shoe: 50$
Car Tire: 100$
Magic Bean: 150$
Diamond: 500$
Car: 750$
Dinosaur Bone: 1000$
Trident: 1500$
Prehistoric Spear: 10000$
        """)

        input("[ENTER]")

        clear()
        main()

    if q == "9":

        if shoefin == True and diamondfin == True and dinofin == True and canfin == True and candyfin == True and bottlefin == True and tirefin == True and psfin == True and carfin == True and magicfin == True and tridentfin == True:
            print("All Contracts Done!")
            wait(TIME)
            clear()
            main()

        else:
            clear()

            if shoefin == False:
                print("1: Shoe - {}/10 - 10000$".format(shoe))

            else:
                print("1: Shoe - Done!")

            if diamondfin == False:
                print("2: Diamond - {}/10 - 35000$".format(diamond))

            else:
                print("2: Diamond - Done!")    

            if dinofin == False:
                print("3: Dinosaur Bone - {}/10 - 40000$".format(dinosaurbone))

            else:
                print("3: Dinosaur Bone - Done!")

            if canfin == False:
                print("4: Can - {}/10 - 15000$".format(can))

            else:
                print("4: Can - Done!")    

            if candyfin == False:
                print("5: Candy Wrapper - {}/10 - 20000$".format(candywrapper))

            else:
                print("5: Candy Wrapper - Done!")

            if bottlefin == False:
                print("6: Bottle Cap - {}/10 - 25000$".format(bottlecap))

            else:
                print("6: Bottle Cap - Done!")    

            if tirefin == False:
                print("7: Car Tire - {}/10 - 30000$".format(cartire))

            else:
                print("7: Car Tire - Done!")

            if psfin == False:
                print("8: Prehistoric Spear - {}/10 - 150000$".format(ps))

            else:
                print("8: Prehistoric Spear - Done!")

            if carfin == False:
                print("9: Car - {}/10 - 37500$".format(car))

            else:
                print("9: Car - Done!")

            if magicfin == False:
                print("10: Magic Bean - {}/10 - 32500$".format(magicbean))

            else:
                print("10: Magic Bean - Done!")

            if tridentfin == False:
                print("11: Trident - {}/10 - 45000$".format(trident))

            else:
                print("11: Trident - Done!")

            print("\n12: Go Back")

            con = input("\nOption: ")

            if con == "1":
                if shoe >= 10 and shoefin == False:
                    shoefin = True
                    print("Contract Finished!\nYou've Recieved 10000 Dollars!")
                    bal = bal + 10000
                    wait(TIME)
                    clear()
                    main()

                elif shoefin == True:
                    print("Shoe Cantract Is Already Done!")
                    wait(TIME)
                    clear()
                    main()

                elif shoe < 10:
                    print("Not Enough Of The Item!")
                    wait(TIME)
                    clear()
                    main()

            if con == "2":
                if diamond >= 10 and diamondfin == False:
                    diamondfin = True
                    print("Contract Finished!\nYou've Recieved 35000 Dollars!")
                    bal = bal + 35000
                    wait(TIME)
                    clear()
                    main()

                elif diamondfin == True:
                    print("Diamond Cantract Is Already Done!")
                    wait(TIME)
                    clear()
                    main()

                elif diamond < 10:
                    print("Not Enough Of The Item!")
                    wait(TIME)
                    clear()
                    main()

            if con == "3":
                if dinosaurbone >= 10 and dinofin == False:
                    dinofin = True
                    print("Contract Finished!\nYou've Recieved 40000 Dollars!")
                    bal = bal + 40000
                    wait(TIME)
                    clear()
                    main()

                elif dinofin == True:
                    print("Dinosaur Bone Cantract Is Already Done!")
                    wait(TIME)
                    clear()
                    main()

                elif dinosaurbone < 10:
                    print("Not Enough Of The Item!")
                    wait(TIME)
                    clear()
                    main()

            if con == "4":
                if can >= 10 and canfin == False:
                    canfin = True
                    print("Contract Finished!\nYou've Recieved 15000 Dollars!")
                    bal = bal + 15000
                    wait(TIME)
                    clear()
                    main()

                elif canfin == True:
                    print("Can Cantract Is Already Done!")
                    wait(TIME)
                    clear()
                    main()

                elif can < 10:
                    print("Not Enough Of The Item!")
                    wait(TIME)
                    clear()
                    main()

            if con == "5":
                if candywrapper >= 10 and candyfin == False:
                    candyfin = True
                    print("Contract Finished!\nYou've Recieved 20000 Dollars!")
                    bal = bal + 20000
                    wait(TIME)
                    clear()
                    main()

                elif candyfin == True:
                    print("Candy Wrapper Cantract Is Already Done!")
                    wait(TIME)
                    clear()
                    main()

                elif candywrapper < 10:
                    print("Not Enough Of The Item!")
                    wait(TIME)
                    clear()
                    main()

            if con == "4":
                if can >= 10 and canfin == False:
                    canfin = True
                    print("Contract Finished!\nYou've Recieved 15000 Dollars!")
                    bal = bal + 15000
                    wait(TIME)
                    clear()
                    main()

                elif canfin == True:
                    print("Can Cantract Is Already Done!")
                    wait(TIME)
                    clear()
                    main()

                elif can < 10:
                    print("Not Enough Of The Item!")
                    wait(TIME)
                    clear()
                    main()

            if con == "6":
                if bottlecap >= 10 and bottlefin == False:
                    bottlefin = True
                    print("Contract Finished!\nYou've Recieved 25000 Dollars!")
                    bal = bal + 25000
                    wait(TIME)
                    clear()
                    main()

                elif bottlefin == True:
                    print("Bottle Cap Cantract Is Already Done!")
                    wait(TIME)
                    clear()
                    main()

                elif bottlecap < 10:
                    print("Not Enough Of The Item!")
                    wait(TIME)
                    clear()
                    main()

            if con == "7":
                if cartire >= 10 and tirefin == False:
                    tirefin = True
                    print("Contract Finished!\nYou've Recieved 30000 Dollars!")
                    bal = bal + 30000
                    wait(TIME)
                    clear()
                    main()

                elif tirefin == True:
                    print("Car Tire Cantract Is Already Done!")
                    wait(TIME)
                    clear()
                    main()

                elif cartire < 10:
                    print("Not Enough Of The Item!")
                    wait(TIME)
                    clear()
                    main()

            if con == "8":
                if ps >= 10 and psfin == False:
                    psfin = True
                    print("Contract Finished!\nYou've Recieved 150000 Dollars!")
                    bal = bal + 150000
                    wait(TIME)
                    clear()
                    main()

                elif psfin == True:
                    print("Prehistoric Spear Cantract Is Already Done!")
                    wait(TIME)
                    clear()
                    main()

                elif ps < 10:
                    print("Not Enough Of The Item!")
                    wait(TIME)
                    clear()
                    main()

            if con == "9":
                if car >= 10 and carfin == False:
                    carfin = True
                    print("Contract Finished!\nYou've Recieved 37500 Dollars!")
                    bal = bal + 37500
                    wait(TIME)
                    clear()
                    main()

                elif carfin == True:
                    print("Car Cantract Is Already Done!")
                    wait(TIME)
                    clear()
                    main()

                elif car < 10:
                    print("Not Enough Of The Item!")
                    wait(TIME)
                    clear()
                    main()

            if con == "10":
                if magicbean >= 10 and magicfin == False:
                    magicfin = True
                    print("Contract Finished!\nYou've Recieved 32500 Dollars!")
                    bal = bal + 32500
                    wait(TIME)
                    clear()
                    main()

                elif magicfin == True:
                    print("Magic Bean Cantract Is Already Done!")
                    wait(TIME)
                    clear()
                    main()

                elif magicbean < 10:
                    print("Not Enough Of The Item!")
                    wait(TIME)
                    clear()
                    main()

            if con == "11":
                if trident >= 10 and tridentfin == False:
                    tridentfin = True
                    print("Contract Finished!\nYou've Recieved 45000 Dollars!")
                    bal = bal + 45000
                    wait(TIME)
                    clear()
                    main()

                elif tridentfin == True:
                    print("Trident Cantract Is Already Done!")
                    wait(TIME)
                    clear()
                    main()

                elif trident < 10:
                    print("Not Enough Of The Item!")
                    wait(TIME)
                    clear()
                    main()

            if con == "12":
                clear()
                main()

            else:
                print("Invalid Input")
                wait(TIME)
                clear()
                main()

    if q == "10":
        clear()
        print("Level: {}".format(level))
        print("Xp: {}".format(xp))
        print("\n10 Xp = 1 Level")
        print("1 Level = 1000$")
        print("\n1: Exchange Xp For Levels\n")
        print("2: Exchange Levels For Money\n")
        print("3: 5 Dinosaur Bones - Price: 2 Levels")
        print("4: Free Item - Price: 3 Levels")
        print("5: Go Back")

        l = input("\nOption: ")

        if l == "1":
            x = 0
            y = xp % 10
            x += (xp - y) / 10
            xp -= (xp - y)
            level += x
            print("{} Levels Recieved".format(round(x)))
            wait(TIME)
            clear()
            main()

        if l == "2":
            x = level * 1000
            level -= level
            bal += x
            print("+{}$".format(x))
            wait(TIME)
            clear()
            main()

        if l == "3":
            if level >= 2:
                if len(inventory) <= (invs - 5):
                    level -= 2
                    for i in range(5):
                        inventory.append("Dinosaur Bone")
                    print("You Bought 5 Dinosaur Bones!")
                    wait(TIME)
                    clear()
                    main()
                else:
                    print("Not Enough Inventory Space")
                    wait(TIME)
                    clear()
                    main()
            else:
                print("Not Enough")
                wait(TIME)
                clear()
                main()

        if l == "4":
            if level >= 3:
                if len(inventory) < invs:
                    level -= 3
                    print("1: Shoe")
                    print("2: Diamond")
                    print("3: Dinosaur Bone")
                    print("4: Can")
                    print("5: Candy Wrapper")
                    print("6: Bottle Cap")
                    print("7: Car Tire")
                    print("8: Car")
                    print("9: Magic Bean")
                    print("10: Trident")

                    f = input("\nItem: ")

                    if f == "1":
                        inventory.append("Shoe")

                    if f == "2":
                        inventory.append("Diamond")

                    if f == "3":
                        inventory.append("Dinosaur Bone")

                    if f == "4":
                        inventory.append("Can")

                    if f == "5":
                        inventory.append("Candy Wrapper")

                    if f == "6":
                        inventory.append("Bottle Cap")

                    if f == "7":
                        inventory.append("Car Tire")

                    if f == "8":
                        inventory.append("Car")

                    if f == "9":
                        inventory.append("Magic Bean")

                    if f == "10":
                        inventory.append("Trident")

                    else:
                        print("Since You Chose Nothing, I Will Randomly Pick An Item For You")
                        wait(2)
                        ia = choice(rewards)
                        print("You Recieved A {}".format(ia))
                        inventory.append(ia)
                else:
                    print("Not Enough Inventory Space!")
                    wait(TIME)
                    clear()
                    main()
            else:
                print("Not Enough")
                wait(TIME)
                clear()
                main()

        if l == "5":
            clear()
            main()
            
        else:
            print("Invalid Input")
            wait(TIME)
            clear()
            main()

    if q == "11":
        clear()
        print("Balance: {}".format(bal))

        print("\n1: Normal Egg - Increases Sell Value By 20 - Price: 1000")
        print("2: Strong Egg - Increases Sell Value By 50 - Price: 2000")
        print("3: Mega Egg - Increases Sell Value By 100 - Price: 5000")
        print("4: Superior Egg - Increases Sell Value By 150 - Price: 8000")
        print("5: Level Pet Up - Increases Sell Value By 50 - Price: 5000")
        print("6: Go Back")

        e = input("\nOption: ")

        if e == "1":
            if bal >= 1000:
                if pet not in petc1:
                    x = choice(petc1)
                    print("Opening Normal Egg..")
                    wait(2)
                    print("You Got A {}".format(x))
                    pet = x
                    pav = 20
                    bal -= 1000
                    wait(TIME)
                    clear()
                    main()

                else:
                    print("Your Pet Is From This Egg!")
                    wait(TIME)
                    clear()
                    main()
            else:
                print("Not Enough!")
                wait(TIME)
                clear()
                main()

        if e == "2":
            if bal >= 2000:
                if pet not in petc2:
                    x = choice(petc2)
                    print("Opening Strong Egg..")
                    wait(2)
                    print("You Got A {}".format(x))
                    pet = x
                    pav = 50
                    bal -= 2000
                    wait(TIME)
                    clear()
                    main()

                else:
                    print("Your Pet Is From This Egg!")
                    wait(TIME)
                    clear()
                    main()
            else:
                print("Not Enough!")
                wait(TIME)
                clear()
                main()

        if e == "3":
            if bal >= 5000:
                if pet not in petc3:
                    x = choice(petc3)
                    print("Opening Mega Egg..")
                    wait(2)
                    print("You Got A {}".format(x))
                    pet = x
                    pav = 100
                    bal -= 5000
                    wait(TIME)
                    clear()
                    main()

                else:
                    print("Your Pet Is From This Egg!")
                    wait(TIME)
                    clear()
                    main()
            else:
                print("Not Enough!")
                wait(TIME)
                clear()
                main()

        if e == "4":
            if bal >= 8000:
                if pet not in petc4:
                    x = choice(petc4)
                    print("Opening Superior Egg..")
                    wait(2)
                    print("You Got A {}".format(x))
                    pet = x
                    pav = 150
                    bal -= 8000
                    wait(TIME)
                    clear()
                    main()

                else:
                    print("Your Pet Is From This Box!")
                    wait(TIME)
                    clear()
                    main()
            else:
                print("Not Enough!")
                wait(TIME)
                clear()
                main()

        if e == "5":
            if bal >= 5000:
                bal -= 5000
                pav += 50
                pl += 1
                print("Pet Leveled Up!")
                wait(TIME)
                clear()
                main()
            else:
                print("Not Enough")
                wait(TIME)
                clear()
                main()

        if e == "6":
            clear()
            main()
                
        else:
            print("Invalid Input")
            wait(TIME)
            clear()
            main()

    if q == "12":
        clear()
        def ls():
            print("Initiating Launch Sequence..")
            wait(2)
            print()
            for i in range(5):
                print(5 - i)
                wait(1)
            print()
        print("Balance: {}".format(bal))
        print("\nNukes Ignore Inventory Space\nIf Inventory Is More Than Inventory Space, Use Sell All Option\n")
        print("1: Small Nuke - Finds 5 Random Items - Price: 1000")
        print("2: Good Nuke - Finds 10 Random Items - Price: 2000")
        print("3: Normal Nuke - Finds 15 Random Items - Price: 3000")
        print("4: Mega Nuke - Finds 20 Random Items - Price: 4000")
        print("5: Ultimate Nuke - Finds 25 Random Items - Price: 5000")
        print("6: Go Back")

        n = input("\nOption: ")

        if n == "1":
            if bal >= 1000:
                bal -= 1000
                ls()
                itms = []
                for i in range(5):
                    x = choice(rewards)
                    if x != "Nothing":
                        y = randint(0, psr)
                        if y == 1:
                            x == "Prehistoric Spear"
                        inventory.append(x)
                        itms.append(x)
                    if x == "Nothing":
                        itms.append(x)
                print("You Found A..\n")
                for i in itms:
                    print(i)
                input("\n[ENTER] ")
                clear()
                main()

            else:
                print("Not Enough")
                wait(TIME)
                clear()
                main()

        if n == "2":
            if bal >= 2000:
                bal -= 2000
                ls()
                itms = []
                for i in range(10):
                    x = choice(rewards)
                    if x != "Nothing":
                        y = randint(0, psr)
                        if y == 1:
                            x == "Prehistoric Spear"
                        inventory.append(x)
                        itms.append(x)
                    if x == "Nothing":
                        itms.append(x)
                print("You Found A..\n")
                for i in itms:
                    print(i)
                input("\n[ENTER] ")
                clear()
                main()

            else:
                print("Not Enough")
                wait(TIME)
                clear()
                main()

        if n == "3":
            if bal >= 3000:
                bal -= 3000
                ls()
                itms = []
                for i in range(15):
                    x = choice(rewards)
                    if x != "Nothing":
                        y = randint(0, psr)
                        if y == 1:
                            x == "Prehistoric Spear"
                        inventory.append(x)
                        itms.append(x)
                    if x == "Nothing":
                        itms.append(x)
                print("You Found A..\n")
                for i in itms:
                    print(i)
                input("\n[ENTER] ")
                clear()
                main()

            else:
                print("Not Enough")
                wait(TIME)
                clear()
                main()

        if n == "4":
            if bal >= 4000:
                bal -= 4000
                ls()
                itms = []
                for i in range(20):
                    x = choice(rewards)
                    if x != "Nothing":
                        y = randint(0, psr)
                        if y == 1:
                            x == "Prehistoric Spear"
                        inventory.append(x)
                        itms.append(x)
                    if x == "Nothing":
                        itms.append(x)
                print("You Found A..\n")
                for i in itms:
                    print(i)
                input("\n[ENTER] ")
                clear()
                main()

            else:
                print("Not Enough")
                wait(TIME)
                clear()
                main()

        if n == "5":
            if bal >= 5000:
                bal -= 5000
                ls()
                itms = []
                for i in range(25):
                    x = choice(rewards)
                    if x != "Nothing":
                        y = randint(0, psr)
                        if y == 1:
                            x == "Prehistoric Spear"
                        inventory.append(x)
                        itms.append(x)
                    if x == "Nothing":
                        itms.append(x)
                print("You Found A..\n")
                for i in itms:
                    print(i)
                input("\n[ENTER] ")
                clear()
                main()

            else:
                print("Not Enough")
                wait(TIME)
                clear()
                main()

        if n == "6":
            clear()
            main()

        else:
            print("Invalid Input")
            wait(TIME)
            clear()
            main()

    if q == "13":
        clear()
        print(pro)
        input("[ENTER] ")
        clear()
        main()

    if q == "14":
        clear()
        dsta = False
        print("Saved")
        quit()

    if q in w:
        w.remove(q)
        bal += 2000
        print("Stop Hacking You Greedy Child\n2000$+")
        wait(TIME)
        clear()
        main()

    if q == "omg secret":
        if wb == False:
            hp = 100 + ahp
            hp1 = 100
            dmg = 10
            dmg1 = 11
            print("Yo Weirdo Kid Person Alien Thing")
            wait(TIME)
            print("How Dare You Find This Secret")
            wait(TIME)
            print("Now Fight Me You Corpulent Banana")
            wait(TIME)
            clear()
            while True:
                if hp1 <= 0:
                    bal += 5000
                    print("You Killed Them!")
                    print("You Recieved 5000$")
                    wait(2)
                    wb = True
                    break
                if hp <= 0:
                    bal -= C(bal * 0.15)
                    print("You Died..")
                    print("You Lost 15% Of Your Money")
                    wait(2)
                    wb = True
                    break
                clear()
                print("Boss Fight!")
                print("\nYour Health: {}".format(hp))
                print("Their Health: {}".format(hp1))
                print("\n1: Hit Them Because They Are Bad")
                print("2: Get Better Health Because You Want To")
                print("3: Ignore Their Next Weird Attack")
                q = input("\nChoose Wisely: ")
                if q == "1":
                    hp1 -= dmg
                    print("You Hit That Weirdo In The Face!")
                    print("{} Damage!".format(dmg))
                    wait(2)
                if q == "2":
                    heal = randint(9, 15)
                    print("You Healed {} Health!".format(heal))
                    hp += heal
                    wait(2)
                if q == "3":
                    print("You Ignored Their Attack!")
                    print("Showing The Act Of Bravery Through Ignoring, -\nYour Attack Do More Damage!")
                    dmg += randint(1, 2)
                    wait(2)
                print("Oh No! The Person, They Hit You")
                print("They Subtracted {} Of Your Health!".format(dmg1))
                hp -= dmg1
                wait(2)
            clear()
            main()

        if variableidk == 3 and wb == True and wb1 == False:
            hp = 100 + ahp
            hp1 = 110
            dmg = 12
            dmg1 = 12
            print("Stubborn Human")
            wait(TIME)
            print("You Won't Go Will You?")
            wait(TIME)
            print("Now Fight Me Again You Corpulent Banana")
            wait(TIME)
            while True:
                if hp1 <= 0:
                    bal += 5000
                    print("You Killed Them!")
                    print("You Recieved 5000$")
                    wait(2)
                    wb1 = True
                    break
                if hp <= 0:
                    bal -= C(bal * 0.15)
                    print("You Died..")
                    print("You Lost 15% Of Your Money")
                    wait(2)
                    wb1 = True
                    break
                clear()
                print("Another Boss Fight!")
                print("\nYour Health: {}".format(hp))
                print("Their Health: {}".format(hp1))
                print("\n1: Hit Them Because They Are Bad")
                print("2: Get Better Health Because You Want To")
                print("3: Ignore Their Next Weird Attack")
                q = input("\nChoose Wisely: ")
                if q == "1":
                    hp1 -= dmg
                    print("You Hit That Weirdo In The Face!")
                    print("{} Damage!".format(dmg))
                    wait(2)
                if q == "2":
                    heal = randint(9, 15)
                    print("You Healed {} Health!".format(heal))
                    hp += heal
                    wait(2)
                if q == "3":
                    print("You Ignored Their Attack!")
                    print("Showing The Act Of Bravery Through Ignoring, -\nYour Attack Do More Damage!")
                    dmg += randint(1, 2)
                    wait(2)
                print("Oh No! The Person, They Hit You")
                print("They Subtracted {} Of Your Health!".format(dmg1))
                hp -= dmg1
                wait(2)
            clear()
            main()

        if variableidk == 6 and wb1 == True and wb2 == False:
            hp = 100 + ahp
            hp1 = 120
            dmg = 13
            dmg1 = 12
            print("SO, YOU CAME BACK AGAIN!?")
            wait(TIME)
            print("THAT'S IT")
            wait(TIME)
            print("FIGHT ME ONCE MORE TO SETTLE THE SCORES")
            wait(TIME)
            while True:
                if hp1 <= 0:
                    bal += 5000
                    print("You Killed Them!")
                    print("You Recieved 5000$")
                    wait(2)
                    wb2 = True
                    break
                if hp <= 0:
                    bal -= C(bal * 0.15)
                    print("You Died..")
                    print("You Lost 15% Of Your Money")
                    wait(2)
                    wb2 = True
                    break
                clear()
                print("Another Boss Fight!")
                print("\nYour Health: {}".format(hp))
                print("Their Health: {}".format(hp1))
                print("\n1: Hit Them Because They Are Bad")
                print("2: Get Better Health Because You Want To")
                print("3: Ignore Their Next Weird Attack")
                q = input("\nChoose Wisely: ")
                if q == "1":
                    hp1 -= dmg
                    print("You Hit That Weirdo In The Face!")
                    print("{} Damage!".format(dmg))
                    wait(2)
                if q == "2":
                    heal = randint(9, 15)
                    print("You Healed {} Health!".format(heal))
                    hp += heal
                    wait(2)
                if q == "3":
                    print("You Ignored Their Attack!")
                    print("Showing The Act Of Bravery Through Ignoring, -\nYour Attack Do More Damage!")
                    dmg += randint(1, 2)
                    wait(2)
                print("Oh No! The Person, They Hit You")
                print("They Subtracted {} Of Your Health!".format(dmg1))
                hp -= dmg1
                wait(2)
            clear()
            main()
            
        else:
            print("Greedy Alien, You Already Fought Them")
            variableidk += 1
            wait(TIME)
            clear()
            main()

    if q == "hyperalternative is bad" and hafin == False:
        hp = 500 + ahp
        hp1 = 520
        dmg = 20
        dmg1 = 21
        print(fore.RED + "WHAT HAVE YOU JUST SAID?")
        wait(TIME)
        print(fore.RED + "YOU DISRESPECTED HYPERALTERNATIVE?")
        wait(TIME)
        print(fore.RED + "IF YOU THINK YOUR SO SMART..")
        wait(TIME)
        print(fore.RED + "FIGHT HIM YOURSELF" + fore.RESET)
        wait(TIME)
        while True:
            clear()
            if animm == False:
                animm = True
                print("----------------")
                wait(0.1)
                clear()
                print("D--------------e")
                wait(0.1)
                clear()
                print("De------------le")
                wait(0.1)
                clear()
                print("Dev----------tle")
                wait(0.1)
                clear()
                print("Deve--------ttle")
                wait(0.1)
                clear()
                print("Develo-----attle")  
                wait(0.1) 
                clear()             
                print("Develop---Battle")
                wait(0.1)
                clear()
                print("Develope- Battle")
                wait(0.1)
                clear()
                print(fore.RED + "Developer Battle" + fore.RESET)

            else:
                print(fore.RED + "Developer Battle" + fore.RESET)

            if hp1 <= 0:
                bal += 5000
                print("You Killed Them!")
                print("You Recieved 5000$")
                wait(2)
                hafin = True
                break
            if hp <= 0:
                bal -= C(bal * 0.15)
                print("You Died..")
                print("You Lost 15% Of Your Money")
                wait(2)
                hafin = True
                break
            print("\nYour Health: {}".format(hp))
            print("Their Health: {}".format(hp1))
            print("\n1: Hit Them Because They Are Bad")
            print("2: Get Better Health Because You Want To")
            print("3: Ignore Their Next Weird Attack")
            q = input("\nChoose Wisely: ")
            if q == "1":
                hp1 -= dmg
                print("You Hit HyperAlternative In The Face!")
                print("{} Damage!".format(dmg))
                wait(2)
            if q == "2":
                heal = randint(9, 15)
                print("You Healed {} Health!".format(heal))
                hp += heal
                wait(2)
            if q == "3":
                print("You Ignored Their Attack!")
                print("Showing The Act Of Bravery Through Ignoring, -\nYour Attack Do More Damage!")
                dmg += randint(1, 2)
                wait(2)
            body_parts = ["Face", "Leg", "Stomach", "Shoulder"]
            print("HyperAlternative Hit You In The {}!".format(choice(body_parts)))
            print("He Subtracted {} Of Your Health!".format(dmg1))
            hp -= dmg1
            wait(2)
            
        clear()
        main()

    else:
        print("Invalid Input")
        wait(TIME)
        clear()
        main()

mode = input("1: Creative (Shut Down)\n2: Normal\n\nOption: ")

if mode == "1":
    print("Creative Mode Is Shut Down For Right Now")
    wait(2)
    clear()
    main()

if mode == "2":
    sys('clear')
    main()

if mode == "yes":
    print("yes")
    wait(TIME)
    sys('clear')
    main()

else:
    print("Invalid Input\nAutomatically Switching To Normal Mode")
    wait(TIME)
    sys('clear')
    main()
    
""""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣶⣿⣿⣿⣿⣿⣄⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⠿⠟⠛⠻⣿⠆⠀
⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣆⣀⣀⠀⣿⠂⠀
⠀⠀⠀⠀⠀⠀⠀⢸⠻⣿⣿⣿⠅⠛⠋⠈⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠘⢼⣿⣿⣿⣃⠠⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣟⡿⠃⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣛⣛⣫⡄⠀⢸⣦⣀⠀
⠀⠀⠀⢀⣠⣴⣾⡆⠸⣿⣿⣿⡷⠂⠨⣿⣿⣿⣿⣶⣦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣤⣾⣿⣿⣿⣿⡇⢀⣿⡿⠋⠁⢀⡶⠪⣉⢸⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢀⣿⣿⣿⣿⣿⣿⣿⣿⡏⢸⣿⣷⣿⣿⣷⣦⡙⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠈⣿⣿⣿⣿⣿⣿⣿⣿⣇⢸⣿⣿⣿⣿⣿⣷⣦⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢹⣿⣵⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⡁

Never Gonna Give You Up
"""
# Get Rickrolled For Being Down Here
