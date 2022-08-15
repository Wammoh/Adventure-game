import random
import sys
import time


def play_game():
    backpack = []  # inventory for player
    random_loot = ["Sword of a Thousand Truths",
                   "Bow of Unending Fury", "Large Catfish"]
    # player loot table
    random_drop = "Amulet of Winning"  # loot for winning
    random_mob = []  # randomly selected mob list.
    mobs = ["Ghoul", "Ghost", "Skeleton"]  # random mob table.
    random_mob.append(random.choice(mobs))  # selects a random
    # mob for the later encounter.
    intro(backpack, random_drop, random_mob, random_loot)


def play_again(backpack, random_mob):
    choice = valid_input("Play again?\n'Y or N'\n", ["y", "n"]).lower()
    if choice == 'n':
        print('Thanks for playing! Goodbye!')
        print_slow("Do not think it ends here... "
                   "The history of light and shadow will be written in blood"
                   "-Ganondorf")
        exit(0)
    else:
        backpack.clear()
        play_game()


def valid_input(prompt, options):
    while True:
        option = input(prompt).lower()
        if option in options:
            return option
        print_pause("That is not a valid choice, try again.")


def print_slow(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1 / 50)


def print_pause(story):
    print(story)
    time.sleep(1.5)  # time speed for text


def graveyard(backpack, random_drop, random_mob, random_loot):
    print_pause("You walk into the main courtyard, there are two paths"
                " that you can see.\n")
    choice = valid_input("1. Towards the chapel\n"
                         "2. Towards the shack\n(Select '1' or 2')\n",
                         ["1", "2"])
    if choice == '1':
        chapel(backpack, random_drop, random_mob, random_loot)
    else:
        shack(backpack, random_drop, random_mob, random_loot)


def inside_shack(backpack, random_drop, random_mob, random_loot):
    print_pause("You find the door is unlocked.")
    if (len(backpack)) == 0:
        print_pause("You open the door and start to look around for"
                    " any loot.\n")
        backpack.extend(random.choices(random_loot))
        print_pause(f"You open a large chest and find the"
                    f" {(','.join(backpack))}")
        print_pause("You toss your old rusty sword to the ground. ")
        print_pause(f"You equip your new {(','.join(backpack))} "
                    f"and head back to the courtyard.")
        graveyard(backpack, random_drop, random_mob, random_loot)
    elif (len(backpack)) > 0:
        print_pause("You have already looted this place!\n"
                    "You turn around and go back to the courtyard")
        graveyard(backpack, random_drop, random_mob, random_loot)


def shack(backpack, random_drop, random_mob, random_loot):
    print_pause("You walk down the worn out path leading to the shack, as"
                " you get closer you can")
    print_pause("see a few flickers of light coming from the windows.\n")
    choice = valid_input("What will you do?\n1. Look in the "
                         "shack\n2. Go back to the "
                         "courtyard\n(Select '1' or 2')\n", ["1", "2"])
    if choice == "1":
        inside_shack(backpack, random_drop, random_mob, random_loot)
    else:
        graveyard(backpack, random_drop, random_mob, random_loot)


def intro(backpack, random_drop, random_mob, random_loot):
    # intro and mob selection.
    print_slow("""
    "We all make choices in life, but in the end our choices make us."
    -Andrew Ryan(Bioshock)
        """)
    print_slow("""
                   ()
                   )(
               o========o
                   ||
                   ||
                   ||
                   ||
                   ||
                   ||
                   ||
                   ||
                   ||
                    V
     """)

    print_pause("You're walking on a dimly lit cobblestone path.")
    print_pause("The lanterns along the pathway flicker as the wind blows.")
    print_pause("As you come to the end, you can see it leads to a graveyard,"
                " you check to ensure you have your old "
                "sword.")
    print_pause("You enter the graveyard with your torch in one hand, you "
                "come onto a fork in the path.\n")
    print_pause("The path to the right leads to what appears to be an old"
                " abandoned shack.")
    print_pause("The path to the left leads down a trail that leads to a"
                " dilapidated stone chapel\n")
    graveyard(backpack, random_drop, random_mob, random_loot)


def inside_chapel(backpack, random_drop, random_mob):
    if "Sword of a Thousand Truths" in backpack:
        print_pause("You start to explore the old chapel.")
        print_pause(f"As you explore you are attacked by a"
                    f" {(','.join(random_mob))}!")
        print_pause(f"You unsheathe the {(','.join(backpack))} "
                    f"and swing at the "
                    f"{(','.join(random_mob))}!\n")
        print_pause(f"The {(','.join(random_mob))} dies and drops an"
                    f" {random_drop}!")
        print_pause("You win!*Happy music*")
        play_again(backpack, random_drop)
    elif "Bow of Unending Fury" in backpack:
        print_pause("You start to explore the old chapel.")
        print_pause(f"As you explore you are attacked by a "
                    f"{(','.join(random_mob))}")
        print_pause(f"You pull out {(','.join(backpack))}"
                    f" and "
                    f"defeat the {(','.join(random_mob))}"
                    f" with one arrow!")
        print_pause(f"The {(','.join(random_mob))} dies and drops an"
                    f" {random_drop}!")
        print_pause("You win!*Happy music*")
        play_again(backpack, random_drop)
    elif "Large Catfish" in backpack:
        print_pause("You start to explore the old chapel.")
        print_pause(f"As you explore you are attacked by a"
                    f" {(','.join(random_mob))}!")
        print_pause(f"You grab the {(','.join(backpack))} and "
                    f"slap the {(','.join(random_mob))}"
                    f" in the head")
        print_pause("Your fish is as effective as you would"
                    " assume. You die")
        print_pause("Game over! *sad disappointed music!*")
        play_again(backpack, random_drop)
    else:
        print_pause(f"You look inside and are attacked by a"
                    f" {(','.join(random_mob))}!")
        print_pause("You attack with your rusty sword!")
        print_pause("Your attacks are ineffective!\n"
                    "You die!")
        print_pause("Game over! *sad disappointed music!*")
        play_again(backpack, random_drop)


def chapel(backpack, random_drop, random_mob, random_loot):
    print_pause("You walk down the path to the old chapel, the path"
                " turns into dirt as you get closer.")
    print_pause("and can see it in quite a decayed state.\n")
    choice = valid_input("What will you do?\n1. look inside\n2."
                         " Go back\n(Select '1' or 2')\n", ["1", "2"])
    if choice == '1':
        inside_chapel(backpack, random_drop, random_mob)
    else:
        graveyard(backpack, random_drop, random_mob, random_loot)


play_game()
