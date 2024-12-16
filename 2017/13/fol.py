from copy import deepcopy

class Layer:
    def __init__(self, height, fake=True):
        self.height = height
        self.curpos = 0
        self.fake = fake
        self.direction = 1
    def move(self):
        if self.direction + self.curpos >= self.height:
            self.direction *= -1
        if self.direction + self.curpos == -1:
            self.direction *= -1
        self.curpos += self.direction
    def tracked(self):
        return self.curpos == 0 and not self.fake

    def __repr__(self):
        return f"<{self.curpos=}>"

states = {}
for line in open(0).readlines():
    line = line.split()
    d = int(line[0][:-1])
    v = Layer(int(line[-1]), False)
    states[d] = v


def loop_move(states, reps):
    for _ in range(reps):
        for scan in states.values():
            scan.move()

j = 0

first_states = states
while True:
    res = 0
    curdepth = -1-j
    states = deepcopy(first_states)
    for i in range(max(states)+1+j):
        curdepth += 1
        curscan = states.get(curdepth, Layer(200000))
        if curscan.tracked():
            res += 1
        for scan in states.values():
            scan.move()
    print(j)
    if res == 0:
        print(j)
        exit(0)
    j += 1
