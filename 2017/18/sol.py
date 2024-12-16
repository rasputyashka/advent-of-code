from collections import defaultdict
from threading import Thread
import queue

instructions = [x.strip() for x in open(0).readlines()]

def num_or_reg(x, registers):
    if x.isdigit() or x[1:].isdigit():
        return int(x)
    return registers[x]

def main(sender, receiver, pval, genname):
    registers = defaultdict(int)
    idx = 0
    registers['p'] = pval
    cnt = 0
    while 0 <= idx < len(instructions):
        instr = instructions[idx].split()
        match instr:
            case ['snd', x]:
                if genname == 'first':
                    cnt += 1
                x = num_or_reg(x, registers)
                sender.put(x)
            case ['set', x, y]:
                registers[x] = num_or_reg(y, registers)
            case ['add', x, y]:
                registers[x] += num_or_reg(y, registers)
            case ['mul', x, y]:
                registers[x] *= num_or_reg(y, registers)
            case ['mod', x, y]:
                registers[x] %= num_or_reg(y, registers)
            case ['rcv', x]:
                if genname == 'first':
                    print(f'1 programm send {cnt} times')
                y = receiver.get(False)
                registers[x] = y
            case ['jgz', x, y]:
                if registers[x] > 0:
                    idx += num_or_reg(y, registers)
                    continue
        idx += 1


to_1 = queue.Queue()
to_2 = queue.Queue()

thread1 = Thread(target=main, args=(to_1, to_2, 0, 'first'))
thread2 = Thread(target=main, args=(to_2, to_1, 1, 'second'))
thread1.start()
thread2.start()
