# Jessica Kusmierz
# 11/14/2025
# Problem 5
class character:
    def __init__(self, nickname, weapons, weaknesses):
        self.nickname = nickname
        self.weapons = weapons
        self.weaknesses = weaknesses

    def get_nickname(self):
        return self.nickname

    def get_weapons(self):
        return self.weapons

    def get_weaknesses(self):
        return self.weaknesses

    def profile(self):
        return self.nickname, self.weapons, self.weaknesses
    def display_profile(self):
        print("Nickname: ", self.nickname)
        print("Weapons: ", self.weapons)
        print("Weaknesses: ", self.weaknesses)


player1 = character('','','')
player1.nickname = 'Dragon Slayer'
player1.weapons = ['pan', 'paper', 'idea', 'rope', 'groceries']
player1.weaknesses = ['slow']

print("character inventory:")
for item in player1.weapons:
    print("-", item)

print("\nCharacter weaknesses:")
for debuff in player1.weaknesses:
    print("-", debuff)

player1.display_profile()
print(f"\nPlayer Nickname: {player1.get_nickname()}")
print(f"Weapons: {player1.get_weapons()}")
print(f"Weaknesses: {player1.get_weaknesses()}")
print(f"Full Profile: {player1.profile()}")