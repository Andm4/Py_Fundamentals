#Task 1 WEEK ONE FINAL ASSIGNMENT   
wizard = "Wizard"
elf = "Elf"
human = "Human"
drago ="Dragon"
orc = "Orc"

wizard_hp = 70
elf_hp = 100
human_hp = 150
dragon_hp = 300
orc_hp = 500

wizard_damage = 150
elf_damage = 100
human_damage = 20
dragon_damage = 50
orc_damage = 200

#Task 2 & 3
play_again = "y"
while play_again.lower() == "y":  # Adding a nested while loop to ask user for replay
    while True:
        print ("1) Wizard")
        print ("2) Elf")
        print ("3) Human")
        print ("4) Orc")   #Bonus: Added 4th character with stats
        print ("5) End Game")  #Bonus: Added an end game option
        character = input("Choose your character: ")

        if character.lower() in ["1", "wizard"]:  #Bonus: added .lower() to always revert cap words to lower string
            character = wizard
            my_hp = wizard_hp
            my_damage = wizard_damage
            break
        elif character.lower() in ["2", "elf"]:
            character = elf
            my_hp = elf_hp
            my_damage = elf_damage
            break
        elif character.lower() in ["3", "human"]:
            character = human
            my_hp = human_hp
            my_damage = human_damage
            break
        elif character.lower() in ["4", "orc"]:
            character = orc
            my_hp = orc_hp
            my_damage = orc_damage
            break
        elif character == "5":
            print("Exiting the game.....")
            exit()
        else:
            print ("Unknown character")

    print("You chose the: ", character)
    print("Health: ", my_hp)
    print("Damage: ", my_damage, "\n")

    while True:
        dragon_hp = dragon_hp - my_damage
        my_hp = my_hp - dragon_damage
        print("The", character, "damaged the Dragon!")
        print("The Dragon's hit points are now:", dragon_hp, "\n")

        if dragon_hp <= 0:
            print("The Dragon has lost the battle")
            break

        print("The Dragon strikes back at", character)
        print("The", character + "'s", "hitpoints are now:", my_hp, "\n")

        if my_hp <= 0:
            print("The", character, "has lost the fight for asgard" "\n")
            break 
    
    play_again = input("Thou thy want to play again?? (y/n)")
    if play_again.lower() != "y":
        print("The Dragon smites thee!!! Begone!!")  # End of loop callsback the replay nested loop
