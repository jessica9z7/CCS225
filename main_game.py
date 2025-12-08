#Jessica
#11/7/2025
#Monster and Zombie Kingdom Adventure Game

import random
import Milestone3Chapter_1, Milestone3Chapter_2, Milestone3Chapter_3, Milestone3Chapter_4, Milestone3Chapter_5

def main():
    """Main function to run the Monster and Zombie Kingdom Adventure Game."""
    print("="*50)
    print("Welcome to the Monster and Zombie Kingdom Adventure Game!")
    print("="*50)

    #initialize player stats
    player= {
        "name": "",
        "health": 100,
        "inventory": [],
        "coins": 0,
        "stars": 0,
        "cards": [],
        "companions": [],
    }

    print(f"\nWelcome,{player['name']}! Your adventure begins now.")

    #Game progression through chapters
    chapters = [Milestone3Chapter_1, Milestone3Chapter_2, Milestone3Chapter_3, Milestone3Chapter_4, Milestone3Chapter_5]
    current_chapter = 0

    # Main game loop that runs when player is alive and chapters remain
    while current_chapter < len(chapters) and player["health"] > 0:
        print(f"\n--- Chapter {current_chapter + 1} ---")
    # Calls each chapter
        if current_chapter == 0:
            success = Milestone3Chapter_1.start_chapter_1(player)
        elif current_chapter == 1:
            success = Milestone3Chapter_2.start_chapter_2(player)
        elif current_chapter == 2:
            success = Milestone3Chapter_3.start_chapter_3(player)
        elif current_chapter == 3:
            success = Milestone3Chapter_4.start_chapter_4(player)
        elif current_chapter == 4:
            success = Milestone3Chapter_5.start_chapter_5()
        if success:
            current_chapter += 1
        else:
            print("You have failed this chapter. Game Over.")
            break

    # Game ending
    if player["health"] > 0 and current_chapter == 5:
        print("\nCongratulations! You have completed the Monster and Zomite Kingdom Adventure Game!")
    else:
        print("\nThank you for playing the Monster and Zomite Kingdom Adventure Game. Better luck next time!")  
    
if __name__ == "__main__":
    main()
    