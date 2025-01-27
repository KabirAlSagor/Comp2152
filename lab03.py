# Lab 03 solutions
import random

# dice options plus weapons list
dice_options = list(range(1, 7))
weapons = ['Fist', 'Knife', 'Club', 'Gun', 'Bomb', 'Nuclear Bomb']

# show available weapons
print("Available Weapons:")
for i, weapon in enumerate(weapons, 1):
    print(f"{i}. {weapon}")

# get the valid combat strength for hero
while True:
    combat_strength = int(input("Enter your combat strength (1-6): "))
    if 1 <= combat_strength <= 6:
        break
    else:
        print("Invalid input! Combat strength should be between 1 and 6.")

# get the valid combat strength for monster
while True:
    monster_combat_strength = int(input("Enter monster's combat strength (1-6): "))
    if 1 <= monster_combat_strength <= 6:
        break
    else:
        print("Invalid input! Monster combat strength should be between 1 and 6.")

# simulate 10 rounds of battle using a for loop
for round_num in range(1, 11):  # Simulate 10 rounds
    # Random dice rolls for hero and monster
    hero_roll = random.choice(dice_options)
    monster_roll = random.choice(dice_options)

    # Weapon selection based on dice roll
    hero_weapon = weapons[hero_roll - 1]
    monster_weapon = weapons[monster_roll - 1]

    # calculate total strengths
    hero_total_strength = combat_strength + hero_roll
    monster_total_strength = monster_combat_strength + monster_roll

    # print round results
    print(f"\nRound {round_num}: Hero rolled {hero_roll}, Monster rolled {monster_roll}.")
    print(f"Hero selected: {hero_weapon}, Monster selected: {monster_weapon}.")
    print(f"Hero Total Strength: {hero_total_strength}, Monster Total Strength: {monster_total_strength}.")

    # determine winner of the round
    if hero_total_strength > monster_total_strength:
        print("Hero wins the round!")
    elif hero_total_strength < monster_total_strength:
        print("Monster wins the round")
    else:
        print("It's a tie!")

    # declae truce at round 11
    if round_num == 11:
        print("\nBattle Truce declared in Round 11. Game Over!")
        break

# End of battle if truce is not declared
if round_num != 11:
    print("\nBattle concluded after 10 rounds!")
