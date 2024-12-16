class Disk:
    def __init__(self, positions, current):
        self.positions = positions
        self.current = current
    def rotate(self, att):
        self.current = (self.current + att) % self.positions
        return self.current == 0

def init_disks():

    disks = [
        Disk(17, 15),
        Disk(3, 2),
        Disk(19, 4),
        Disk(13, 2),
        Disk(7, 2),
        Disk(5, 0),
        Disk(11, 0)
    ]
    return disks

att = 1
while True:
    disks = init_disks()
    # can speed this up
    for disk in disks:
        disk.rotate(att)
    if disks[0].rotate(1):
        if disks[1].rotate(2):
            if disks[2].rotate(3):
                if disks[3].rotate(4):
                    if disks[4].rotate(5):
                        if disks[5].rotate(6):
                            if disks[6].rotate(7):
                                print(att)
                                exit(0)
    att += 1
