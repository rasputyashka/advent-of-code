from collections import defaultdict
from threading import Thread
import queue

instructions = [x.strip() for x in open(0).readlines()]

zero_to_one = queue.Queue()
one_to_zero = queue.Queue()

def num_or_reg(x, registers):
    if x.isdigit() or x[1:].isdigit():
        return int(x)
    return registers[x]

def main(getter, sender, pval):
    registers = defaultdict(int)
    idx = 0
    registers['p'] = pval
    cnt = 0
    while 0 <= idx < len(instructions):
        instr = instructions[idx].split()
        match instr:
            case ['snd', x]:
                if pval == 1:
                    cnt += 1
                sender.put(num_or_reg(x, registers))
            case ['set', x, y]:
                registers[x] = num_or_reg(y, registers)
            case ['add', x, y]:
                registers[x] += num_or_reg(y, registers)
            case ['mul', x, y]:
                registers[x] *= num_or_reg(y, registers)
            case ['mod', x, y]:
                registers[x] %= num_or_reg(y, registers)
            case ['rcv', x]:
                try:
                    registers[x] = getter.get(block=False)
                except queue.Empty:
                    if pval == 1:
                        print(f'1 programm send {cnt} times')
                print(pval, registers[x])
            case ['jgz', x, y]:
                if registers[x] > 0:
                    idx += num_or_reg(y, registers)
                    continue
            case _:
                print(instr)
        idx += 1

thread1 = Thread(target=main, args=(one_to_zero, zero_to_one, 0))
thread2 = Thread(target=main, args=(zero_to_one, one_to_zero, 1))

thread1.start()
thread2.start()

thread1.join()
thread2.join()
print('finish')
