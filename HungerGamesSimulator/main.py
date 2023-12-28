import random as rand
import time

colors = [
    '\33[31m',
    '\33[32m',
    '\33[33m',
    '\33[34m',
    '\33[35m',
    '\33[36m',
    '\33[90m',
    '\33[91m',
    '\33[92m',
    '\33[93m',
    '\33[94m',
    '\33[95m',
    '\33[96m',
    '\33[97m'

]


class Player():
    def __init__(self, name, items=None, weapon=None):
        self.name = name
        self.items = items if items is not None else []
        self.weapon = weapon if weapon is not None else []

    health = 100
    damage = 10



    peopleLiked = []
    peopleDisliked = []

    mental = 100
    hunger = 100
    betrayalChance = 100 // mental
    killCount = 0

    alive = True
    deathDay = 0

    # methods

    def add_weapon(self, weaponName):
        self.damage = 30
        self.weapon.append(weaponName)

    def add_item(self, itemName):
        self.items.append(itemName)

    def remove_weapon(self, weaponName):
        self.damage = 10
        self.weapon.remove(weaponName)

    def remove_item(self, itemName):
        self.items.remove(itemName)

    def check_death(self):
        if self.health <= 0:
            self.alive = False
            self.deathDay = day
            return True


# Lists

weapons = ["bow and arrow", "knives", "trident", "axe", "sword"]

cornucopiaItems = ["bow and arrow", "knives", "trident", "axe", "sword",
                   "meal pack", "camouflage", "rope", "lipstick", "shovel", "bandages"]

allitems = ["bow and arrow", "knives", "maces", "tridents", "axe", "sword", "sickle", "meal pack", "camouflage",
                   "rope", "lipstick", "shovel" "stone", "fishing rod", "siple" ]

cornucopiaPlayers = [] # List containing players at cornucopia

players = [] # List containing players

special = {"Holes": 0} # Dictionary containing players with special attributes


# Functions

def find_someone(player):
    while 1:
        other_party = rand.choice(players)
        if other_party.name != player.name and other_party.alive:
            if other_party in special and special[other_party.name] != "Hidden":
                return other_party
            return other_party


def itemEvent(player):

    if player.items == []:
        eventChooser(player)

    eventList = {
        "shovel": 'print(f"{player.name} dug a hole on the ground")',
        "camouflage": 'print(f"{player.name} decided to hide for a while with their camouflage)',
        "bandages": 'print(f"{player.name} treated their wounds with bandages")',                    # Make this used on low health
        "lipstick": 'print(f"{player.name} plays around with the lipstick, not knowing its purpose")',
        "rope": 'print(f"{player.name} set a trap using their rope")'
    }


    while 1:
        event = rand.choice(eventList.keys())
        if event in player.items:
            break


    if special["Holes"] > 0 and "shovel" not in player.items:
        print(f"{player.name} fell into a hole and broke their neck")

    elif event == "shovel":
        eventList[event]
        special["Holes"] += 1

    elif event == "camouflage":
        eventList[event]
        special[player.name] = "Hidden"

    elif event == "bandages":
        eventList[event]
        player.health += 50
        player.items.remove("bandages")

    elif event == "lipstick":
        b = rand.randint(1,3)
        eventList[event]
        print("The lipstick explodes, killing them")
        player.alive = False
        player.deathDay = day

    elif event == "rope":
        eventList[event]



def foodEvent(player):  # When hunger is low
    if "meal pack" in player.items:
        print(f"{player.name} feels full after finishing their meal pack")
        player.hunger += 70
        player.items.remove("meal pack")

    elif "siple" in player.items:
        print(f"{player.name} uses the siple to drink some water")
        player.hunger += 40

    elif "fishing rod" in player.items:
        b = rand.randint(1,3)
        if b == 1:
            print(f"{player.items} tried to fish but could not catch anything")
        elif b == 2:
            print(f"{player.name} caught a fish with the fishing rod and ate it")
            player.hunger += 40
        elif b == 3:
            print(f"{player.name} caught a fish and ate it, without knowing it was poisonous")
            player.hunger += 40
            player.health -= 10
            if check_death(player):
                print("Guess who's dead")


    else:
        eventList = {
            0: 'print(f"{player.name} hurts themselves while hunting for food")',
            1: 'print(f"{player.name} found some fruits")',
            2: 'print(f"{player.name} tries wild berries")',
            3: 'print(f"{player.name} finds water source")'
        }
        event = rand.choice(list(eventList.keys()))
        exec(eventList[event])
        if event == 0:
            player.health -= 20
            player.hunger += 40
            if player.check_death():
                print("They bled to death")
            print()

        elif event == 1:
            player.hunger += 40
            print()

        elif event == 2:
            x = rand.randint(1, 2)
            if x == 1:
                print(f"They get poisoned")
                print()
                player.health -= 20
                player.hunger += 40
                if player.check_death():
                    print(f"{player.name} die a painfull and slow death")
                    print()

            if x == 2:
                player.hunger += 40
                print(f"{player.name} enjoys some edible berries")
                print()

        elif event == 3:
            player.hunger += 40
            print()


def randomEvent(player):  # Change this to random events
    eventList = {
        0: 'print(f"{player.name} stepped on a mine and blew up\n")',
        1: 'print(f"{player.name} fell from a tree",end="")',
        2: 'print(f"{player.name} finds a hiding spot")',
        3: 'print(f"{player.name} hums a song\n")',
        4: 'print(f"{player.name} sees smoke above trees")',
        5: 'print(f"{player.name} finds some sharp stone")',
        6: 'print(f"{player.name} poses for cameras to get donations\n")'

    }
    event = rand.choice(list(eventList.keys()))
    exec(eventList[event])


    if event == 0:
        player.alive = False

    elif event == 1:
        z = rand.randint(1,3)
        if z == 1:
            other_party = find_someone(player)
            print(f"\nThey landed on {other_party.name} and killed both of them\n")
            other_party.alive = False
            player.alive = False
            other_party.deathDay = day
            player.deathDay = day
            player.killCount += 1

        elif z == 2:
            other_party = find_someone(player)
            print(f"\nThey landed on {other_party.name}, softening their fall and killing {other_party.name}\n")
            other_party.alive = False
            other_party.deathDay = day
            player.killCount += 1

        elif z == 3:
            player.health -= 20
            if player.check_death():
                print(" and couldn't get up, ever again\n")
            else:
                print(" and walked away with just some bruises\n")

    elif event == 2:
        special[player.name] = "Hidden"

    elif event == 4:
        v = rand.randint(1,2)
        if v == 1:
            print(f"They decided to not interfere and stayed low\n")
        elif v == 2:
            print(f"They went to check out the area")
            encounterEvent(player)

    elif event == 5:
        player.items.append("stone")


def donationEvent(player):
    eventList = {
        0: 'print(f"{player.name} gets donated a meal packet")',
        1: 'print(f"{player.name} gets donated a knife")',
        2: 'print(f"{player.name} gets donated a binocular")',
        3: 'print(f"{player.name} gets donated a water tap")',
        4: 'print(f"{player.name} gets donated a clothes")',
        5: 'print(f"{player.name} gets donated a camouflage")',
        6: 'print(f"{player.name} gets donated a burn cream")'
    }
    event = rand.choice(list(eventList.keys()))
    exec(eventList[event])
    print()
    if event == 0:
        player.items.append("meal packet")
    elif event == 1:
        player.items.append("knives")
    elif event == 2:
        player.items.append("binocular")
    elif event == 3:
        player.items.append("siple")
    elif event == 4:
        player.items.append("clothes")
    elif event == 5:
        player.items.append("camouflage")
    elif event == 6:
        player.items.append("burn cream")


def otherEvent(player):
    eventList = {
        0: 'print(f"{player.name} gazes at the sky")',
        1: 'print(f"{player.name} hums a song")',
        2: 'print(f"{player.name} thinks about their family")'
    }
    event = rand.choice(list(eventList.keys()))
    exec(eventList[event])
    print()


def encounterEvent(player):  # Events that 2 people encounter each other
    other_party = find_someone(player)
    print(f"{player.name} encountered {other_party.name}")

    # Add positive outcomes if they like each other
    if other_party.name not in player.peopleLiked:
        print(f"They get in a battle with {other_party.name}")
        battleEvent(player, other_party)
        print()


def battleEvent(player, other_party):

    def throw_stone(without,with_s): # defining a function to not be repetitive
        without.health -= 20
        if without.check_death():
            print(f"{with_s.name} thrown some stones at {without.name}, dropping them dead")
            with_s.items.remove("stone")
            with_s.killCount += 1
        else:
            print(f"{with_s.name} thrown some stones at {without.name} and escaped")
            with_s.items.remove("stone")

    if player.damage > other_party.damage:
        if "stone" in other_party.items:
            throw_stone(player,other_party)
        else:
            battle(player, other_party)
    elif player.damage < other_party.damage:
        if "stone" in player.items:
            throw_stone(other_party,player)
        else:
            battle(other_party, player)
    else:
        x = rand.randint(1, 2)
        if x == 1:
            if "stone" in other_party.items:
                throw_stone(player, other_party)
            else:
                battle(player, other_party)
        elif x == 2:
            if "stone" in player.items:
                throw_stone(other_party, player)
            else:
                battle(other_party, player)


def battle(strong, weak):
    weak.health -= strong.damage
    strong.health -= weak.damage
    weak.check_death()
    strong.check_death()
    if strong.alive == False:  # If the strong dies, they take the weak with them
        print("They both died")
        weak.alive = False
        weak.deathDay = day
        strong.killCount += 1
        weak.killCount += 1
    else:
        e = rand.randint(1, 3)
        if e <= 2 or weak.alive == False:  # The strong one kills the weak and takes an item
            if weak.items == []:
                print(f"{strong.name} killed {weak.name}")
                weak.alive = False
                weak.deathDay = day
                strong.killCount += 1
            else:
                h = rand.choice(weak.items)
                print(f"{strong.name} took {h} from {weak.name} after killing them")
                weak.alive = False
                weak.deathDay = day
                strong.killCount += 1
                if h in weapons:
                    strong.add_weapon(h)
                else:
                    strong.add_item(h)
        elif e == 3:  # The strong one damages the weak and takes an item
            if weak.items == []:
                print(strong.name, rand.choice(
                    ["took a finger from " + weak.name + " but couldn't finish them off",
                     "left a scar on " + weak.name + "'s face but they ran away",
                     "hesitated to kill " + weak.name + " and they escaped"]))
            else:
                h = rand.choice(weak.items)
                print(weak.name, "escaped with", rand.choice(["bruises", "wounds", "scratches"]),
                      "but dropped their", h)
                strong.peopleDisliked.append(weak.name)
                weak.peopleDisliked.append(strong.name)
                if h in weapons:
                    strong.add_weapon(h)
                    weak.remove_weapon(h)
                else:
                    strong.add_item(h)
                    weak.remove_item(h)


# Özel günler

def cornucopiaEvent(player):
    x = rand.randint(1, 2)
    if x == 1:  # Didn't go to the cornucopia
        print(f"{player.name} escaped into the forest")
        print()

    elif x == 2:  # Went to the cornucopia
        print(f"{player.name} ran to the cornucopia")
        cornucopiaPlayers.append(player)

        x = rand.randint(1, 3)
        if len(cornucopiaPlayers) <= 1:
            x = 1
        if x == 1:  # Took an item and ran
            q = rand.choice(cornucopiaItems)
            print(f"They took {q}")
            print()
            if q in weapons:
                player.add_weapon(q)
            else:
                player.add_item(q)


        elif x == 2 or x == 3:  # Encountered someone
            other_party = find_someone(player)
            print(f"They encountered {other_party.name}")

        if x == 2:  # VIOLENCE!
            battleEvent(player, other_party)
            print()

        elif x == 3:  # Placeholder for now
            print("They nodded to each other and continue their ways")
            print()


def eventChooser(player):
    if player.alive:
        if round == 3:
            cornucopiaEvent(player)
        else:
            category = rand.randint(1, 100)
            if category <=10 or player.hunger <= 30:
                foodEvent(player)
            elif category <= 30:
                encounterEvent(player)
            elif category <= 50:
                randomEvent(player)
            elif category <= 70:
                itemEvent(player)
            elif category <= 90:
                otherEvent(player)
            elif category <= 100:
                donationEvent(player)

def specialEventAnnounce(round):
    if round == 3:
        print("\33[42m" + "Cornucopia awaits with riches" + "\33[0m")
    print()


# Where it all begins

playerList = input("Enter the names of players: ")
print("----------------------------\n")
i = 0
for a in playerList.split(" "):
    a = Player(colors[i] + a + '\33[0m')
    players.append(a)
    i += 1


round = 3

while len(players) > 1:
    # Time tracker

    day = round // 3
    if round % 3 == 0:
        interval = "Morning"
    elif round % 3 == 1:
        interval = "noon"
    else:
        interval = "night"

    print(f"day {day}'s {interval}\n")
    specialEventAnnounce(round)

    # Player actions

    for a in players:
        if a.alive:

            # Choosing event

            eventChooser(a)

            # Adjusting hunger and mental

            a.hunger -= 10
            if a.hunger <= 0:
                a.alive == False
                print(f"{a.name} died of starvation")

            if a.hunger <= 50:
                a.mental -= 10

            time.sleep(1)

    # Round ending
    count = 0
    deadNames = ""
    if interval == "night":
        for a in players:
            if a.deathDay == day:
                count += 1
                deadNames += (" " + a.name + " ")
        if count == 0:
            print("No faces are shown this night")
        elif count == 1:
            print("Only 1 cannon ball was fired this night, with the face of" + deadNames + "lighting the sky")
        else:
            print(count, " cannons were heard," + deadNames + "were shown on the sky")

    print()
    answer = input(f"End of day {day}'s {interval}")
    if answer == "stats":
        for i in players:
            if i.alive:
                print(i.name, end=" ")
        print("are alive", end="")
    print("\n\n")

    special = {}

    round += 1

    random.shuffle(players)