# Chapter 5: Card and Ball Game

import random

def start_chapter_5():
    print("Player and zombie go to Zombie World")
    print("Hide in bushes to see what's happening")
    print("Finds a cow with 2 cards")
    print("Player picks between red or green card")

    # Player chooses a card
    card_choice = input("Choose a card color (red/green): ").lower()
    handle_card_choice(card_choice)

def handle_card_choice(card_choice):
    if card_choice == "red":
        print("You picked the red card!")
        print("Player goes to Chapter 5")
    
    elif card_choice == "green":
        print("You picked the green card!")
        print("You win and get a cow")
        print("You ride the cow to town")
        print("You realize the cow can help fight and teleport")
        print("In Zombie World, they see fight and decide to help")
        print("Player has a ball and goal")
        play_ball_game()

    else:
        print("Invalid card color. Choose red or green next time.")


def play_ball_game():
    print("Welcome to the Card and Ball Game!")
    print("You need to score a goal.")

    # Random goal position
    goal_position = random.randint(1, 10)

    # Ask player to shoot the ball
    try:
        player_shot = int(input("Pick a number from 1 to 10 to shoot the ball: "))
    except ValueError:
        print("Invalid input. You missed the goal.")
        print("Player goes back to ride cow to town.")
    
    # Determine if player scored
    if player_shot == goal_position:
        print("Congratulations! You scored a goal!")
        print("The cow telports some water, and causes a flood causing the fight to be over.")
        print("You win and there's Peace between the World!")
        print("The End.")
    else:
        print("Oh no! You missed the goal. Try again next time.")
        print("Player goes back to ride cow to town.")
        return

if __name__ == "__main__":
    start_chapter_5()