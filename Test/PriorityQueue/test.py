import sys
sys.path.insert(0, './../../DataStructures/')
from Heap import PriorityQueue

q = PriorityQueue()
while(True):
    inp = input()
    inpArgs = inp.split()
    if len(inpArgs) == 0: continue
    if inpArgs[0] == "End": break
    elif inpArgs[0] == "pop":
        print(q.Pop())
        print(q)
    elif inpArgs[0] == "push":
        if len(inpArgs) != 3: continue
        q.Push(int(inpArgs[1]), inpArgs[2])
        print(q)
