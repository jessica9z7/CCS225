# Chapter 4: Friendship with Zombie General Matt

import random

def start_chapter_4(player):
    """Chapter 4 - Friendship and Stick Game"""
    print("Chapter 4: Friendship with Zombie General Matt")
    print("You encounter Zombie General Matt")
    print("You run to other side of cave")
    print("You guys look at each other and realize no one wants to hurt each other")
    print("You decide to be friends")
    print("You have befriended Zombie General Matt.")       
    print("\nMatt picks up a stick and hands it to you.")
    print("You both pull on opposite sides of the stick—it breaks!")

    # Stick Pulling Game that randomly picls who wins
    outcome = random.choice(["longer"])

    # Player wins
    if outcome == "longer":
        print("\nYou got the longer piece of the stick!")
        print("You win and get a star!")
        player['stars'] = player.get('stars', 0) + 1
        print("You earned a STAR!")
        print("You go to Chapter 5")
        return "chapter5"

    # Player loses
    else:
        print("\nYou got the shorter piece of the stick.")
        print("You lose!")
        print("You decide to rest and try again later.")
        return "chapter4"


if __name__ == "__main__":
    start_chapter_4()