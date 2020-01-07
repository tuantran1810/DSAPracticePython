import sys
sys.path.insert(0, './../../DataStructures/')
from LinkedList import LinkedList

ll = LinkedList()

ll.PushHeadBatch([60, 10, 90, 20, 40, 70, 30, 50, 11, 19, -50])
print(ll)

node = None
while(True):
    inp = input()
    inpArgs = inp.split()
    if len(inpArgs) == 0: continue
    if inpArgs[0] == "End": break
    elif inpArgs[0] == "Dnth":
        if len(inpArgs) != 2: continue
        ll.RemoveNthNode(int(inpArgs[1]))
    elif inpArgs[0] == "Dnode":
        ll.RemoveNode(node)
    elif inpArgs[0] == "Dall":
        ll.RemoveAll()
    elif inpArgs[0] == "F":
        if len(inpArgs) != 2: continue
        node = ll.FindKey(int(inpArgs[1]))
        print("Found node: " + str(node))
    elif inpArgs[0] == "PushH":
        if len(inpArgs) != 2: continue
        ll.PushHead(int(inpArgs[1]))
    elif inpArgs[0] == "PushT":
        if len(inpArgs) != 2: continue
        ll.PushTail(int(inpArgs[1]))
    elif inpArgs[0] == "PopH":
        ll.PopHead()
    elif inpArgs[0] == "PopT":
        ll.PopTail()
    elif inpArgs[0] == "IB":
        if len(inpArgs) != 2: continue
        ll.InsertBefore(node, int(inpArgs[1]))
    elif inpArgs[0] == "IA":
        if len(inpArgs) != 2: continue
        ll.InsertAfter(node, int(inpArgs[1]))
    elif inpArgs[0] == "IPush":
        if len(inpArgs) != 2: continue
        ll.IncreasementPush(int(inpArgs[1]))
    elif inpArgs[0] == "DPush":
        if len(inpArgs) != 2: continue
        ll.DecreasementPush(int(inpArgs[1]))
    print(ll)

