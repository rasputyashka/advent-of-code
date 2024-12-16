import sys
from copy import deepcopy

sys.setrecursionlimit(18000)


class Enemy:
    def __init__(self, damage: int, hp: int):
        self.damage = damage
        self.hp = hp

    def attack(self, player):
        player.hp -= max(1, self.damage - player.defense)
        found = False
        for spell in player.effects:
            if spell.name == "shield":
                found = True
                shield = spell
        if found:
            player.effects.discard(shield)
        return player.hp < 1

    def copy(self):
        return Enemy(self.damage, self.hp)

    def __repr__(self):
        return f"{self.hp}"


class Spell:
    def __init__(self, name, price, damage, health, mana, timer):
        self.name = name
        self.price = price
        self.damage = damage
        self.health = health
        self.mana = mana
        self.timer = timer

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)

    def empty(self):
        return self.timer < 1

    def __repr__(self):
        return f"[{self.name=}, {self.timer=}]"


class Player:
    id_num = 0

    def __init__(
        self,
        mana: int,
        hp: int,
        defense: int,
        effects: set | None = None,
        spent: int = 0,
    ):
        self.id_num = Player.id_num
        Player.id_num += 1
        self.spent = spent
        self.defense = defense
        self.mana = mana
        self.hp = hp
        if effects is None:
            self.effects = {}
        else:
            self.effects = effects.copy()
        self.skip_list = []

    def add_effect(self, effect: Spell):
        new_effects = deepcopy(self.effects)
        new_effects.add(effect)
        copy = self.copy()
        copy.spent += effect.price
        copy.mana -= effect.price
        copy.effects = new_effects
        self.skip_list.append(effect)
        return copy

    def attack(self, enemy):
        spell_damage = 0
        to_discard = set()
        for spell in self.effects:
            if spell in self.skip_list:
                self.skip_list.clear()
                continue
            if spell.name == "shield":
                self.defense = 7
            self.hp += spell.health
            self.mana += spell.mana
            spell_damage += spell.damage
            spell.timer -= 1
            if spell.empty():
                to_discard.add(spell)
        for discard_spell in to_discard:
            self.effects.discard(discard_spell)
            if discard_spell.name == "shield":
                self.defense = 0
        enemy.hp -= spell_damage
        return enemy.hp < 1

    def copy(self):
        return Player(
            self.mana, self.hp, self.defense, self.effects, self.spent
        )

    def __str__(self):
        return f"<{self.id_num=}, {self.spent=}, {self.hp=}, {self.effects=}>"

    __repr__ = __str__
    # return f"<{self.mana=}, {self.hp=}, {self.defense=}, {self.effects=}, {self.spent=}>"


def fight(enemy, player, depth=0):
    new_players = []

    SPELLS = [
        Spell("magic missile", 53, 4, 0, 0, 1),
        Spell("drain", 73, 2, 2, 0, 1),
        Spell("shield", 113, 0, 0, 0, 7),
        Spell("poison", 173, 3, 0, 0, 6),
        Spell("recharge", 229, 0, 0, 101, 5),
    ]

    for spell in SPELLS:
        if spell not in player.effects and spell.price <= player.mana:
            new_players.append(player.add_effect(spell))
    new_players.append(player.copy())
    results = []
    for new_player in new_players:
        if new_player.effects == set():
            continue
        new_enemy = enemy.copy()
        new_player.attack(new_enemy)
        player_won = new_player.attack(new_enemy)
        if player_won:
            results.append(new_player.spent)
        else:
            enemy_won = new_enemy.attack(new_player)
            if not enemy_won:
                results.append(fight(new_enemy, new_player, depth + 1))
    print(results)
    return min(results, default=float("+inf"))


enemy = Enemy(8, 14)

print(fight(enemy, Player(250, 10, 0, set(), 0)))
