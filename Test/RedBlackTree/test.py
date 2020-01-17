import sys
sys.path.insert(0, './../../DataStructures/')
from RedBlackTree import RedBlackTree

tree = RedBlackTree()
tree.InsertBatch([60, 10, 90, 20, 40, 70, 30, 50, 11, 19, -50])
print(tree)
while(True):
    inp = input()
    inpArgs = inp.split()
    if len(inpArgs) == 0: continue
    if inpArgs[0] == "End": break
    elif inpArgs[0] == "D":
        if len(inpArgs) != 2: continue
        tree.Delete(int(inpArgs[1]))
        print(tree)
    elif inpArgs[0] == "I":
        if len(inpArgs) != 2: continue
        tree.Insert(int(inpArgs[1]))
        print(tree)
    elif inpArgs[0] == "F":
        if len(inpArgs) != 2: continue
        tree.Find(int(inpArgs[1]))
        print(tree)
    elif inpArgs[0] == "Min": print(tree.MinNode())
    elif inpArgs[0] == "Max": print(tree.MaxNode())

