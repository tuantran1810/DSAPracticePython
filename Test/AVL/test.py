import sys
sys.path.insert(0, './../../DataStructures/')
from AVLTree import AVLTree

avl = AVLTree()
avl.InsertBatch([60, 10, 90, 20, 40, 70, 30, 50, 11, 19, -50])
print(avl)
while(True):
    inp = input()
    inpArgs = inp.split()
    if len(inpArgs) == 0: continue
    if inpArgs[0] == "End": break
    elif inpArgs[0] == "D":
        if len(inpArgs) != 2: continue
        avl.Delete(int(inpArgs[1]))
        print(avl)
    elif inpArgs[0] == "I":
        if len(inpArgs) != 2: continue
        avl.Insert(int(inpArgs[1]))
        print(avl)
    elif inpArgs[0] == "Min": print(avl.MinNode())
    elif inpArgs[0] == "Max": print(avl.MaxNode())
