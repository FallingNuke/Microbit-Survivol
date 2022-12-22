from microbit import *
import random

hunger = 50
thirst = 50
health = 100

# Create a list of available items
items = ["food", "water", "medicine"]

# Set up the player's inventory
inventory = []

# Set up variables for the game's enemies
enemies = ["zombie", "bandit"]
enemy_health = 100
enemy_attack = 10

def show_status():
    # Display the player's current status on the LED matrix
    display.show(str(hunger) + ":" + str(thirst) + ":" + str(health))

while True:
    show_status()
    
    # Decrease hunger and thirst over time
    hunger -= 0.5
    thirst -= 0.5
    
    # If hunger or thirst drops to zero, the player's health decreases
    if hunger <= 0:
        health -= 10
    if thirst <= 0:
        health -= 10
    
    # If the player's health drops to zero, they die
    if health <= 0:
        display.show("You died!")
        break
    
    # Check for button presses to eat, drink, or use an item
    if button_a.was_pressed():
        # If the player has food in their inventory, increase their hunger level
        if "food" in inventory:
            hunger += 10
            inventory.remove("food")
        else:
            display.show("No food!")
    elif button_b.was_pressed():
        # If the player has water in their inventory, increase their thirst level
        if "water" in inventory:
            thirst += 10
            inventory.remove("water")
        else:
            display.show("No water!")
    elif accelerometer.was_gesture("shake"):
        # If the player shakes the micro:bit, they might find an item or encounter an enemy
        if random.random() < 0.5:  # 50% chance of finding an item
            # Add a random item to the player's inventory
            item = random.choice(items)
            inventory.append(item)
            display.show("Found a " + item + "!")
        else:
            # The player has encountered an enemy
            enemy = random.choice(enemies)
            display.show(enemy + " attack!")
            while enemy_health > 0:
                # The player can attack the enemy by pressing button A
                if button_a.was_pressed():
                    enemy_health -= 10
                    display.show(enemy + ": " + str(enemy_health))
                else:
                    # The enemy attacks the player
                    health -= enemy_attack
                    show_status()
                    sleep(1000)  # Delay for 1 second between enemy attacks
            # The enemy is defeated
            display.show("Defeated " + enemy + "!")
            # The player may find an item upon defeating the enemy
            if random.random() < 0.5:
                item = random.choice(items)
                inventory.append(item)
                display.show("Found a " + item + "!")
            else:
                display.show("Nothing here.")
    
    # If the player's health is low, they can use medicine
