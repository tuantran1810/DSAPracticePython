import sys
sys.path.insert(0, './../../DataStructures/')
from BST import BST

bst = BST()
bst.InsertBatch([60, 10, 90, 20, 40, 70, 30, 50, 11, 19, -50])
print(bst)
while(True):
    inp = input()
    inpArgs = inp.split()
    if len(inpArgs) == 0: continue
    if inpArgs[0] == "End": break
    elif inpArgs[0] == "D":
        if len(inpArgs) != 2: continue
        bst.Delete(int(inpArgs[1]))
        print(bst)
    elif inpArgs[0] == "I":
        if len(inpArgs) != 2: continue
        bst.Insert(int(inpArgs[1]))
        print(bst)
    elif inpArgs[0] == "Min": print(bst.MinNode())
    elif inpArgs[0] == "Max": print(bst.MaxNode())
