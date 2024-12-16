"""
Frosting:     capacity  4, durability -2, flavor  0, texture 0, calories 5
Candy:        capacity  0, durability  5, flavor -1, texture 0, calories 8
Butterscotch: capacity -1, durability  0, flavor  5, texture 0, calories 6
Sugar:        capacity  0, durability  0, flavor -2, texture 2, calories 1
"""

d = {}

maxval = 0
for frosting in range(0, 101):
    for candy in range(0, 101):
        for butterscotch in range(0, 101):
            sugar = 100 - frosting - candy - butterscotch
            if sugar < 0:
                continue
            # remove the line above and the indentation for solution of part 1
            if 5 *frosting + 8*candy + 6*butterscotch + sugar == 500:
                capacity = max(4*frosting - butterscotch, 0)
                durability = max(-2*frosting + 5*candy, 0)
                flavor = max(-1*candy + 5*butterscotch - 2*sugar, 0)
                texture = max(2*sugar, 0)
                maxval = max(capacity*durability*flavor*texture, maxval)
print(maxval)
