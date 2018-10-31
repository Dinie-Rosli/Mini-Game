import random
import time
def pause():
    programPause = input("Press enter to strike the enemy!")
def pausecont():
    programPausecont = input("Press enter to continue.")
print("Welcome to Dinie's MiniGame. This is an ongoing project, and thus it will continously be improved upon day to day. \nEnjoy!\n") #Storyline
print("You are about to go on an adventure! Your character is the classic RPG hero, along with the classic origin story..." +
      "\nTherefore, I see no reason whatsoever to tell you about an origin story that you most probably won't even read." +
      "\nPlease press enter after this to continue.")
input()
name = str(input("Please enter your character's name: \n")) # Name
Weapon = str(input("Please choose your weapon: \nSword, Greatsword, Bow or Dagger: " + "\n")).lower()#Weapon choice - Permanent for now
weapon = True
counter = 0
while (weapon == True): #While loop to ensure the weapon choice is a part of the options given
    if (Weapon == "sword") or (Weapon == "greatsword") or (Weapon == "bow") or (Weapon == "dagger"):
        weapon = False
    else:
        if (counter>=5):
            Weapon = input("\nPlease stop with your gibberish and choose a WEAPON! \nSword, Greatsword, Bow or Dagger: " + "\n").lower(); counter +=1
        if (counter<5):
            Weapon = input("\nPlease choose your weapon: \nSword, Greatsword, Bow or Dagger: " + "\n").lower(); counter +=1
SlimeHealth = 100; StumpHealth = 70; Health = 60; pots = 1; locate1 = True
time.sleep(0.7); Location1 = str(input("Your character came across an impasse. One road leads to the mountains, and the other to the forest. Which road would you choose? \n")).lower()
while (locate1 == True): #While loop to ensure the location choice is a part of the options given
    if (Location1 == "mountain") or (Location1 == "1") or (Location1 == "mount") or (Location1 == "m") or (Location1 == "mountains"):
        locate1 = False
    elif (Location1 == "forest") or (Location1 == "2") or (Location1 == "for") or (Location1 == "f"):
        locate1 = False
    else:
        Location1 = str(input("You didn't choose either. Please choose properly. \nMountain or Forest? ")).lower()
## Forest Location        
if (Location1 == "forest") or (Location1 == "2") or (Location1 == "for") or (Location1 == "f"):
    print(name + " have entered the forest. An enemy appears before you! It's a slime!\n");time.sleep(0.7)
    while (SlimeHealth>0) and (Health>0):
        print("Your Health is " + str(Health))
        print("Enemy health is: " + str(SlimeHealth) + "\n")
        SlimeDamage = random.sample(range(2,6),4).pop()
        if (Weapon == "sword"):
            dmg = random.sample(range(4,9),5).pop()
            if (Health<=30) and (pots>0):
                potion = input("\nDo you want to use a health potion?" +" You have " + str(pots) +" potion left. Y/N? \n").lower()
                if potion == "y" or potion == "yes":
                    Health += 20
                    pots -= 1
                    print("Your health went up by 20! Your new health is: " + str(Health) + "\n");time.sleep(1)
                    Health -=SlimeDamage
                    print("The enemy dealt " +str(SlimeDamage) + " to you\n");time.sleep(1)
                    continue
                else:
                    pass
            SlimeHealth -=dmg; pause()
            print("\n" + name + " dealt " + str(dmg) + " dmg to the enemy");time.sleep(1)
            if SlimeHealth<=0:
                print("Slime is dead")
                break
            Health -=SlimeDamage
            print("The enemy dealt " +str(SlimeDamage) + " to you\n");time.sleep(1)
            if Health<=0:
                print("You're dead!")
                break
        elif (Weapon == "greatsword"):
            dmg = random.sample(range(6,12),6).pop()
            if (Health<=30) and (pots>0):
                potion = input("\nDo you want to use a health potion?" +" You have " + str(pots) +" potion left. Y/N? \n").lower()
                if potion == "y" or potion == "yes":
                    Health += 20
                    pots -= 1
                    print("Your health went up by 20! Your new health is: " + str(Health) + "\n");time.sleep(1)
                    Health -=SlimeDamage
                    print("The enemy dealt " +str(SlimeDamage) + " to you\n");time.sleep(1)
                    continue
                else:
                    pass
            SlimeHealth -=dmg; pause()
            print("\n" + name + " dealt " + str(dmg) + " dmg to the enemy");time.sleep(1)
            if SlimeHealth<=0:
                print("Slime is dead")
                break
            Health -=SlimeDamage
            print("The enemy dealt " +str(SlimeDamage) + " to you\n");time.sleep(1)
            if Health<=0:
                print("You're dead!")
                break
        elif (Weapon == "bow"):
            dmg = (random.sample(range(3,6),3).pop()+(random.sample(range(2,5),3).pop()))
            if (Health<=30) and (pots>0):
                potion = input("\nDo you want to use a health potion?" +" You have " + str(pots) +" potion left. Y/N? \n").lower()
                if potion == "y" or potion == "yes":
                    Health += 20
                    pots -= 1
                    print("Your health went up by 20! Your new health is: " + str(Health) + "\n");time.sleep(1)
                    Health -=SlimeDamage
                    print("The enemy dealt " +str(SlimeDamage) + " to you\n");time.sleep(1)
                    continue
                else:
                    pass
            SlimeHealth -=dmg; pause()
            print("\n" + name + " dealt " + str(dmg) + " dmg to the enemy");time.sleep(1)
            if SlimeHealth<=0:
                print("Slime is dead")
                break
            Health -=SlimeDamage
            print("The enemy dealt " +str(SlimeDamage) + " to you\n");time.sleep(1)
            if Health<=0:
                print("You're dead!")
                break
        elif (Weapon == "dagger"):
            dmg = (random.sample(range(1,7),6).pop())+(random.sample(range(1,5),4).pop())+(random.sample(range(1,3),2).pop())
            if (Health<=30) and (pots>0):
                potion = input("\nDo you want to use a health potion?" +" You have " + str(pots) +" potion left. Y/N? \n").lower()
                if potion == "y" or potion == "yes":
                    Health += 20
                    pots -= 1
                    print("Your health went up by 20! Your new health is: " + str(Health) + "\n");time.sleep(1)
                    Health -=SlimeDamage
                    print("The enemy dealt " +str(SlimeDamage) + " to you\n");time.sleep(1)
                    continue
                else:
                    pass
            SlimeHealth -=dmg; pause()
            print("\n" + name + " dealt " + str(dmg) + " dmg to the enemy");time.sleep(1)
            if SlimeHealth<=0:
                print("Slime is dead")
                break
            Health -=SlimeDamage
            print("The enemy dealt " +str(SlimeDamage) + " to you\n");time.sleep(1)
            if Health<=0:
                print("You're dead!")
                break
    if Health>0 and SlimeHealth<=0:        
        print("\nYour remaining health is " +str(Health))
## Mountain Location
if (Location1 == "mountain") or (Location1 == "1") or (Location1 == "mount") or (Location1 == "m") or (Location1 == "mountains"):
    print(name + " have entered the mountains. An enemy appears before you! It's a stump!\n");time.sleep(0.7)
    while (StumpHealth>0) and (Health>0):
        print("Your Health is " + str(Health))
        print("Enemy health is: " + str(StumpHealth) + "\n")
        StumpDamage = random.sample(range(1,4),3).pop()+random.sample(range(1,4),3).pop()+random.sample(range(1,3),2).pop()
        if (Weapon == "sword"):
            dmg = random.sample(range(4,9),5).pop()
            if (Health<=30) and (pots>0):
                potion = input("\nDo you want to use a health potion?" +" You have " + str(pots) +" potion left. Y/N? \n").lower()
                if potion == "y" or potion == "yes":
                    Health += 20
                    pots -= 1
                    print("Your health went up by 20! Your new health is: " + str(Health) + "\n");time.sleep(1)
                    Health -=StumpDamage
                    print("The enemy dealt " +str(StumpDamage) + " to you\n");time.sleep(1)
                    continue
                else:
                    pass
            StumpHealth -=dmg; pause()
            print("\n" + name + " dealt " + str(dmg) + " dmg to the enemy");time.sleep(1)
            if StumpHealth<=0:
                print("Stump is dead")
                break
            Health -=StumpDamage
            print("The enemy dealt " +str(StumpDamage) + " to you\n");time.sleep(1)
            if Health<=0:
                print("You're dead!")
                break
        elif (Weapon == "greatsword"):
            dmg = random.sample(range(6,12),6).pop()
            if (Health<=30) and (pots>0):
                potion = input("\nDo you want to use a health potion?" +" You have " + str(pots) +" potion left. Y/N? \n").lower()
                if potion == "y" or potion == "yes":
                    Health += 20
                    pots -= 1
                    print("Your health went up by 20! Your new health is: " + str(Health) + "\n");time.sleep(1)
                    Health -=StumpDamage
                    print("The enemy dealt " +str(StumpDamage) + " to you\n");time.sleep(1)
                    continue
                else:
                    pass
            StumpHealth -=dmg; pause()
            print("\n" + name + " dealt " + str(dmg) + " dmg to the enemy");time.sleep(1)
            if StumpHealth<=0:
                print("Stump is dead")
                break
            Health -=StumpDamage
            print("The enemy dealt " +str(StumpDamage) + " to you\n");time.sleep(1)
            if Health<=0:
                print("You're dead!")
                break
        elif (Weapon == "bow"):
            dmg = (random.sample(range(3,6),3).pop()+(random.sample(range(2,5),3).pop()))
            if (Health<=30) and (pots>0):
                potion = input("\nDo you want to use a health potion?" +" You have " + str(pots) +" potion left. Y/N? \n").lower()
                if potion == "y" or potion == "yes":
                    Health += 20
                    pots -= 1
                    print("Your health went up by 20! Your new health is: " + str(Health) + "\n");time.sleep(1)
                    Health -=StumpDamage
                    print("The enemy dealt " +str(StumpDamage) + " to you\n");time.sleep(1)
                    continue
                else:
                    pass
            StumpHealth -=dmg; pause()
            print("\n" + name + " dealt " + str(dmg) + " dmg to the enemy");time.sleep(1)
            if StumpHealth<=0:
                print("Stump is dead")
                break
            Health -=StumpDamage
            print("The enemy dealt " +str(StumpDamage) + " to you\n");time.sleep(1)
            if Health<=0:
                print("You're dead!")
                break
        elif (Weapon == "dagger"):
            dmg = (random.sample(range(1,7),6).pop())+(random.sample(range(1,5),4).pop())+(random.sample(range(1,3),2).pop())
            if (Health<=30) and (pots>0):
                potion = input("\nDo you want to use a health potion?" +" You have " + str(pots) +" potion left. Y/N? \n").lower()
                if potion == "y" or potion == "yes":
                    Health += 20
                    pots -= 1
                    print("Your health went up by 20! Your new health is: " + str(Health) + "\n");time.sleep(1)
                    Health -=StumpDamage
                    print("The enemy dealt " +str(StumpDamage) + " to you\n");time.sleep(1)
                    continue
                else:
                    pass
            StumpHealth -=dmg; pause()
            print("\n" + name + " dealt " + str(dmg) + " dmg to the enemy");time.sleep(1)
            if StumpHealth<=0:
                print("Stump is dead")
                break
            Health -=StumpDamage
            print("The enemy dealt " +str(StumpDamage) + " to you\n");time.sleep(1)
            if Health<=0:
                print("You're dead!")
                break
    if Health>0 and StumpHealth<=0:        
        print("\nYour remaining health is " +str(Health))
## Have passed either mountain or forest region - Resting period
pots = 1+pots; print("\nCongratulations, you have killed the enemy. It dropped a health potion! You now have "+ str(pots)+" left. Before you continue on..."); time.sleep(2.0);
print("Your proficiency with the " +str(Weapon)+ " has increased. You now deal more damage with the weapon")
Rest = input("\nWould you like to take a rest? Y/N:\n").lower()
if (Rest == "y") or (Rest == "yes") or (Rest == "ye"):
    Health = 60; print("You are rested. Your health is back to " + str(Health))
else:
    print("You opted not to rest. You chose... Poorly... Your health is at " + str(Health))
time.sleep(1.5); print("\nYou have been walking for the past 6 hours and now there is another fork on the road ahead of you. One of the road looks less dangerous than the other.")
## Next engagement
BobslimeHealth = 120; EnragedstumpHealth = 90; locate2 = True
pausecont(); Location2 = str(input("\nThe right road looks more dangerous. Make your choice: left or right? \n")).lower()
while (locate2 == True): #While loop to ensure the location choice is a part of the options given
    if (Location2 == "right") or (Location2 == "r") or (Location2 == "2") or (Location2 == "righ") or (Location2 == "rights"):
        locate2 = False
    elif (Location2 == "left") or (Location2 == "1") or (Location2 == "lef") or (Location2 == "lefts"):
        locate2 = False
    else:
        Location2 = str(input("You didn't choose either.\nLeft or Right? ")).lower()
### Left road
if (Location2 == "left") or (Location2 == "1") or (Location2 == "lef") or (Location2 == "lefts"):
    print(name + " have chosen the left road.");time.sleep(1);print("\nAn enemy appears before you! It's a Bobslime!\n")
    while (BobslimeHealth>0) and (Health>0):
        print("Your Health is " + str(Health))
        print("Enemy health is: " + str(BobslimeHealth) + "\n")
        BobslimeDamage = random.sample(range(2,5),3).pop()+random.sample(range(2,5),3).pop()
        if (Weapon == "sword"):
            dmg = random.sample(range(6,12),6).pop()
            if (Health<=30) and (pots>0):
                potion = input("\nDo you want to use a health potion?" +" You have " + str(pots) +" potion left. Y/N? \n").lower()
                if potion == "y" or potion == "yes":
                    Health += 20
                    pots -= 1
                    print("Your health went up by 20! Your new health is: " + str(Health) + "\n");time.sleep(1)
                    Health -=BobslimeDamage
                    print("The enemy dealt " +str(BobslimeDamage) + " to you\n");time.sleep(1)
                    continue
                else:
                    pass
            BobslimeHealth -=dmg; pause()
            print("\n" + name + " dealt " + str(dmg) + " dmg to the enemy");time.sleep(1)
            if BobslimeHealth<=0:
                print("Bobslime is dead")
                break
            Health -=BobslimeDamage
            print("The enemy dealt " +str(BobslimeDamage) + " to you\n");time.sleep(1)
            if Health<=0:
                print("You're dead!")
                break
        elif (Weapon == "greatsword"):
            dmg = random.sample(range(10,18),8).pop()
            if (Health<=30) and (pots>0):
                potion = input("\nDo you want to use a health potion?" +" You have " + str(pots) +" potion left. Y/N? \n").lower()
                if potion == "y" or potion == "yes":
                    Health += 20
                    pots -= 1
                    print("Your health went up by 20! Your new health is: " + str(Health) + "\n");time.sleep(1)
                    Health -=BobslimeDamage
                    print("The enemy dealt " +str(BobslimeDamage) + " to you\n");time.sleep(1)
                    continue
                else:
                    pass
            BobslimeHealth -=dmg; pause()
            print("\n" + name + " dealt " + str(dmg) + " dmg to the enemy");time.sleep(1)
            if BobslimeHealth<=0:
                print("Bobslime is dead")
                break
            Health -=BobslimeDamage
            print("The enemy dealt " +str(BobslimeDamage) + " to you\n");time.sleep(1)
            if Health<=0:
                print("You're dead!")
                break
        elif (Weapon == "bow"):
            dmg = (random.sample(range(5,8),3).pop()+(random.sample(range(4,7),3).pop()))
            if (Health<=30) and (pots>0):
                potion = input("\nDo you want to use a health potion?" +" You have " + str(pots) +" potion left. Y/N? \n").lower()
                if potion == "y" or potion == "yes":
                    Health += 20
                    pots -= 1
                    print("Your health went up by 20! Your new health is: " + str(Health) + "\n");time.sleep(1)
                    Health -=BobslimeDamage
                    print("The enemy dealt " +str(BobslimeDamage) + " to you\n");time.sleep(1)
                    continue
                else:
                    pass
            BobslimeHealth -=dmg; pause()
            print("\n" + name + " dealt " + str(dmg) + " dmg to the enemy");time.sleep(1)
            if BobslimeHealth<=0:
                print("Bobslime is dead")
                break
            Health -=BobslimeDamage
            print("The enemy dealt " +str(BobslimeDamage) + " to you\n");time.sleep(1)
            if Health<=0:
                print("You're dead!")
                break
        elif (Weapon == "dagger"):
            dmg = (random.sample(range(2,9),7).pop())+(random.sample(range(2,7),5).pop())+(random.sample(range(2,5),3).pop())
            if (Health<=30) and (pots>0):
                potion = input("\nDo you want to use a health potion?" +" You have " + str(pots) +" potion left. Y/N? \n").lower()
                if potion == "y" or potion == "yes":
                    Health += 20
                    pots -= 1
                    print("Your health went up by 20! Your new health is: " + str(Health) + "\n");time.sleep(1)
                    Health -=BobslimeDamage
                    print("The enemy dealt " +str(BobslimeDamage) + " to you\n");time.sleep(1)
                    continue
                else:
                    pass
            BobslimeHealth -=dmg; pause()
            print("\n" + name + " dealt " + str(dmg) + " dmg to the enemy");time.sleep(1)
            if BobslimeHealth<=0:
                print("Bobslime is dead")
                break
            Health -=BobslimeDamage
            print("The enemy dealt " +str(BobslimeDamage) + " to you\n");time.sleep(1)
            if Health<=0:
                print("You're dead!")
                break
    if Health>0 and BobslimeHealth<=0:        
        print("\nYour remaining health is " +str(Health))
## Right road
if (Location2 == "right") or (Location2 == "2") or (Location2 == "right") or (Location2 == "rights"):
    print(name + " have chosen the right road.");time.sleep(1);print("\nAn enemy appears before you! It's an Enraged Stump!\n")
    while (EnragedstumpHealth>0) and (Health>0):
        print("Your Health is " + str(Health))
        print("Enemy health is: " + str(EnragedstumpHealth) + "\n")
        EnragedstumpDamage = random.sample(range(3,6),3).pop()+random.sample(range(2,5),3).pop()+random.sample(range(2,5),3).pop()
        if (Weapon == "sword"):
            dmg = random.sample(range(6,12),6).pop()
            if (Health<=30) and (pots>0):
                potion = input("\nDo you want to use a health potion?" +" You have " + str(pots) +" potion left. Y/N? \n").lower()
                if potion == "y" or potion == "yes":
                    Health += 20
                    pots -= 1
                    print("Your health went up by 20! Your new health is: " + str(Health) + "\n");time.sleep(1)
                    Health -=EnragedstumpDamage
                    print("The enemy dealt " +str(EnragedstumpDamage) + " to you\n");time.sleep(1)
                    continue
                else:
                    pass
            EnragedstumpHealth -=dmg; pause()
            print("\n" + name + " dealt " + str(dmg) + " dmg to the enemy");time.sleep(1)
            if EnragedstumpHealth<=0:
                print("Enraged Stump is dead")
                break
            Health -=EnragedstumpDamage
            print("The enemy dealt " +str(EnragedstumpDamage) + " to you\n");time.sleep(1)
            if Health<=0:
                print("You're dead!")
                break
        elif (Weapon == "greatsword"):
            dmg = random.sample(range(10,18),8).pop()
            if (Health<=30) and (pots>0):
                potion = input("\nDo you want to use a health potion?" +" You have " + str(pots) +" potion left. Y/N? \n").lower()
                if potion == "y" or potion == "yes":
                    Health += 20
                    pots -= 1
                    print("Your health went up by 20! Your new health is: " + str(Health) + "\n");time.sleep(1)
                    Health -=EnragedstumpDamage
                    print("The enemy dealt " +str(EnragedstumpDamage) + " to you\n");time.sleep(1)
                    continue
                else:
                    pass
            EnragedstumpHealth -=dmg; pause()
            print("\n" + name + " dealt " + str(dmg) + " dmg to the enemy");time.sleep(1)
            if EnragedstumpHealth<=0:
                print("Enraged Stump is dead")
                break
            Health -=EnragedstumpDamage
            print("The enemy dealt " +str(EnragedstumpDamage) + " to you\n");time.sleep(1)
            if Health<=0:
                print("You're dead!")
                break
        elif (Weapon == "bow"):
            dmg = (random.sample(range(5,8),3).pop()+(random.sample(range(4,7),3).pop()))
            if (Health<=30) and (pots>0):
                potion = input("\nDo you want to use a health potion?" +" You have " + str(pots) +" potion left. Y/N? \n").lower()
                if potion == "y" or potion == "yes":
                    Health += 20
                    pots -= 1
                    print("Your health went up by 20! Your new health is: " + str(Health) + "\n");time.sleep(1)
                    Health -=EnragedstumpDamage
                    print("The enemy dealt " +str(EnragedstumpDamage) + " to you\n");time.sleep(1)
                    continue
                else:
                    pass
            EnragedstumpHealth -=dmg; pause()
            print("\n" + name + " dealt " + str(dmg) + " dmg to the enemy");time.sleep(1)
            if EnragedstumpHealth<=0:
                print("Enraged Stump is dead")
                break
            Health -=EnragedstumpDamage
            print("The enemy dealt " +str(EnragedstumpDamage) + " to you\n");time.sleep(1)
            if Health<=0:
                print("You're dead!")
                break
        elif (Weapon == "dagger"):
            dmg = (random.sample(range(2,9),7).pop())+(random.sample(range(2,7),5).pop())+(random.sample(range(2,5),3).pop())
            if (Health<=30) and (pots>0):
                potion = input("\nDo you want to use a health potion?" +" You have " + str(pots) +" potion left. Y/N? \n").lower()
                if potion == "y" or potion == "yes":
                    Health += 20
                    pots -= 1
                    print("Your health went up by 20! Your new health is: " + str(Health) + "\n");time.sleep(1)
                    Health -=EnragedstumpDamage
                    print("The enemy dealt " +str(EnragedstumpDamage) + " to you\n");time.sleep(1)
                    continue
                else:
                    pass
            EnragedstumpHealth -=dmg; pause()
            print("\n" + name + " dealt " + str(dmg) + " dmg to the enemy");time.sleep(1)
            if EnragedstumpHealth<=0:
                print("Enraged Stump is dead")
                break
            Health -=EnragedstumpDamage
            print("The enemy dealt " +str(EnragedstumpDamage) + " to you\n");time.sleep(1)
            if Health<=0:
                print("You're dead!")
                break
    if Health>0 and EnragedstumpHealth<=0:        
        print("\nYour remaining health is " +str(Health))
