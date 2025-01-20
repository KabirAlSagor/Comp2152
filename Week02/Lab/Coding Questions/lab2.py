import random

weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear bomb"]
print(weapons)

try:
    weaponRoll = random.randint(1,6)
    combatStrength = 94 + weaponRoll
    heroWeapon = weapons[weaponRoll-1]
    print(f"Hero's Combat Strength: {combatStrength} & Hero's Weapon is: {heroWeapon}")

    if weaponRoll <= 2:
        print("You rolled a weak weapon, friend")
    elif weaponRoll <= 4:
        print("Your weapon is meh")
    else:
        print("Nice weapon, friend!")

    if heroWeapon != "Fist":
        print("Thank goodness you didn't roll the Fist...")
    else:
        print("You can not win with this weapon")

except Exception as e:
    print(f"This is the error: {e}")