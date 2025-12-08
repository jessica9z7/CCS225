 # Chapter 2: Morning Sun and Rock Paper Scissors Battle
# Player enters Monster Kingdom and battles zombies

import random

def start_chapter_2(player):
    """Chapter 2 - Rock Paper Scissors Battle"""
    print("\n CHapter 2: MORNING IN MONSTER KINGDOM")
    print("The morning sun comes out and the weather clears...")
    print("You make your way toward the Monster Kingdom.")

    enter_monster_kingdom(player)

    #Card game entry
    print("\n You find a mysterious card in the ground...")
    print("It seems to be an invitation to play a game!")

    # Rock Paper Scissors battle
    battle_result = rock_paper_scissors_battle(player)

    if battle_result:
        print("\n You survived the battle! Returning to Monster Kingdom.")
        return True
    else:
        print("\n You lost the battle.")
        return False

        
def reward_battle_win(player):
    """Rewards for winning the battle"""
    print("The zombie drops some loot before disappearing!")
    player['coins'] +=2
    player['cards'].append("Zombie Defeat Card")
    print("+2 coins!")
    print("Got Zombie Defeat Card!")

def enter_monster_kingdom(player):
    """Enter the Monster Kingdom"""
    print("\n You arrive at the Monster Kingdom gates!")
    print("The guards recognize you and let you in.")

    if 'Max' in player['companions']:
        print("Max: Welcome to our kingdom! Let me show you around.")
        player['health'] = min(100, player['health'] + 10)
        print("+10 health from Max's hospitality!")

def rock_paper_scissors_battle(player):
    """ROCK PAPER SCISSORS BATTLE with zombie"""
    print("\n ROCK PAPER SCISSORS BATTLE!")
    print("A zombie challenges you to a best-of-3 battle!")
        
        
    wins_needed = 1
    player_wins = 0
    zombie_wins = 0
    rounds = 0
   
  
    choices = ['rock', 'paper', 'scissors']

    while player_wins < wins_needed and zombie_wins < wins_needed and rounds < 3:
        rounds +=1
        print(f"\n--- Round {rounds} ---")

    # Player choice
        while True:
            player_choice = input("Choose: rock, paper or scissors: ").lower()
            if player_choice in choices:
                break
            else:
                print("Invalid choice. Please choose rock, paper, or scissors.")

        # Zombie choice
        zombie_choice = random.choice(choices)
        print(f"Zombie chose: {zombie_choice}") 

            # Determine winner
        if player_choice == zombie_choice:
            print("It's a tie! No points.")
        elif (player_choice == 'rock' and zombie_choice == 'scissors') or \
            (player_choice == 'paper' and zombie_choice == 'rock') or \
                (player_choice == 'scissors' and zombie_choice == 'paper'):
                print(" You win this round!")
                player_wins += 1

        # Current score
        print(f"Score: You {player_wins} - Zombie {zombie_wins}")

        # Battle result
        if player_wins >= wins_needed:
            print("\n VICTORY! You defeated the zombie!")
            reward_battle_win(player)
            return True
        else:
            print("\DEFEAT! The zombie was too strong...")
            return False