# Chapter 1 of Milestone 3: In the monster and zombie kingdom

import random
def start_chapter_1(player):

    print("Chapter 1: In the monster and zombie kingdom")
    print("You are a monster entering a dark world to find shelter.")
    print("You meet a monster called Max.")
    meet_max()
    find_shelter(player)
    print("You find a safe place from the big boss.")
    
    # Decision to continue or end chapter
    choice = input("Do you want to continue exploring or end the chapter? (continue/end): ").lower()
    if choice == "continue":
        print("You and Max decide to continue exploring the monster and zombie kingdom.")
        return True
    else:
        print("You and Max decide to end the chapter here. See you next time!")
        return False
    

def meet_max():
    print("Max: Hello there! Welcome to the monster and zombie kingdom.")
    print("Max: I am Max, your guide in this adventure.")
    print("Max: Together, we will explore this world and find treasures.")

    response = input("Do you want to be friends with Max? (yes/no): ").lower()
    if response == "yes":
        print("Max: Great! Let's be friends and explore together.")
    else:
        print("Max: That's okay. We can still explore together.")

def find_shelter(player):
    """find shelter from the big boss"""
    print("You search for a safe place to hide from the big boss.")

    # List of options
    shelters = ["a dark cave", "an abandoned house", "a dense forest"]

    # Random selection
    safe_place = random.choice(shelters)
    print(f"You found {safe_place} to hide from the big boss.")
    print("You and Max hide safely from the big boss.")

    # Player health boost by +20
    player['health'] = min(100, player['health'] + 20)
    print("Your health has been restored by 20 points.")

    def make_choice():
        """Make a choice to continue or end the chapter"""
        choice = input("Do you want to continue exploring or end the chapter? (continue/end): ").lower()
        if choice == "continue":
            print("You and Max decide to continue exploring the monster and zombie kingdom.")
            return True
        else:
            print("You and Max decide to end the chapter here. See you next time!")
            return False
        
        while True:
            choice = input("Do you want to (1) meet Max, (2) find shelter, or (3) make a choice to continue or end the chapter? (enter 1, 2, or 3): ")

            if choice == 'left':
                get_star(player)
                return 'left'
            elif choice == 'right':
                get_coin(player)
                return 'right'
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")





