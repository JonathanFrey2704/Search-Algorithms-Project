import copy
import time

def ucs(puzzle):
    start = time.time()
    open_list=[]
    open_list.append(puzzle)
    closed_list =[]

    while not open_list[0].isGoal():

        closed_list.append([0,open_list[0].getTotCost(),0,open_list[0].getState()])

        for move in open_list[0].getMoves():
            p = copy.deepcopy(open_list[0])
            p.move(move[0])
            if p.getState() not in [x.getState() for x in open_list]:
                open_list.append(p)
        open_list.sort(key=lambda x: x.cost)

        open_list.pop(0)

        now = time.time()
        if (now - start) > 60:
            return

    return closed_list, open_list[0].getSolution(),open_list[0].getTotCost(),now-start


