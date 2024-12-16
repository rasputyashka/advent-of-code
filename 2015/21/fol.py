class Player:
    def __init__(self, damage, armor, health):
        self.damage = damage
        self.armor = armor
        self.health = health
    def attack(self, other):
        total_damage = max(1, self.damage - other.armor)
        other.health -= total_damage

def play(p):
    e = Player(8, 1, 104)
    current_player = 1
    while p.health > 0 and e.health > 0:
        if current_player == 1:
            p.attack(e)
        else:
            e.attack(p)
        current_player *= -1
    print(p.health, e.health)
    if p.health > 0 and e.health < 1:
        return True
    if e.health > 0 and p.health < 1:
        return False

weapons = {
    "dagger": (8, 4, 0),
    "shortsword": (10, 5, 0),
    "Warhammer": (25, 6, 0),
    "Longsword": (40, 7, 0),
    "Greataxe": (74, 8, 0)
}

armors = {
    "no": (0, 0, 0),
    "leather": (13, 0, 1),
    "chainsmail": (31, 0, 2),
    "splinmail": (53, 0, 3),
    "bandemail": (75, 0, 4),
    "platemail": (102, 0, 5),
}

rings = {
    "no": (0, 0, 0),
    "da1": (25, 1, 0),
    "da2": (50, 2, 0),
    "da3": (100, 3, 0),
    "de1": (20, 0, 1),
    "de2": (40, 0, 2),
    "de3": (80, 0, 3)
}

max_cost = 0
total_cost = 0
for weapon in weapons.values():
    for armor in armors.values():
        for r1 in rings.values():
            for r2 in rings.values():
                if r1 == r2 and r1 != (0, 0, 0):
                    continue
                clothes = [weapon, armor, r1, r2]
                total_cost += sum(x[0] for x in clothes)
                user_damage = sum(x[1] for x in clothes)
                user_armor = sum(x[2] for x in clothes)
                if not play(Player(user_damage, user_armor, 100)):
                    max_cost = max(max_cost, total_cost)
                total_cost = 0

print(max_cost)
