# Chapter 3: Zombie General and the Coin Flip Battle

import random

def start_chapter_3(player):
    """Chapter 3 - Zombie General Encounter"""
    print("\nCHAPTER 3: ZOMBIE GENERAL ATTACK!")
    print("The next day, there are more monsters and zombies out...")
    print("You continue your journey through the Monster Kingdom.")

    print("\nSuddenly, a powerful Zombie General appears!")

    # Player decision
    choice = input("Do you want to (run) or (fight)? ").lower()

    if choice == "run":
        print("\nYou run as fast as you can...")
        print("You manage to escape safely and return to the main path.")
        print("You continue your adventure in Chapter 3.")
        return "chapter3"

    elif choice == "fight":
        print("\nYou bravely face the Zombie General!")
        print("You decide to flip a coin to test your luck...")
        coin = random.choice(["heads", "tails"])
        print(f"\nThe coin lands on {coin.upper()}!")

        if coin == "heads":
            print("\nYou win the fight! The Zombie General retreats.")
            print("You find a cave nearby to rest and hide for a while.")
            print("You regain some health and prepare for the next day.")
            player['health'] = min(100, player['health'] + 15)
            print(f"Health restored to {player['health']}")
            print("You are ready to move on to Chapter 4!")
            return "chapter4"

        else:
            print("\nBad luck! The Zombie General knocks you down.")
            print("You have to retreat and try again...")
            return "chapter3"

    else:
        print("\nInvalid choice! The Zombie General catches you off guard.")
        print("You barely escape and find yourself back where you started.")
        return "chapter3"


if __name__ == "__main__":
    player_data ={
        "health": 70,
        "coins": 7,
        "companions": ["Max"],
        "cards": ["Zombie Defeat Card"]}
    
    next_chapter = start_chapter_3(player_data)
    

