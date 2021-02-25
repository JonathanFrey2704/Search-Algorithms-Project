from copy import deepcopy
import heapq as hq
import time

class Node:

    def __init__(self, puzzle, parent=None):
        self.current_state = puzzle
        self.g = 0
        self.h = 0
        self.f = 0
        self.movement_cost = 0
        self.parent = parent

    def __lt__(self, other):
        return self.f < other.f

    def computeChildren(self):
        puzzle = deepcopy(self.current_state)
        moves = puzzle.getMoves()
        children = []
        
        for direction, cost in moves:
            p = deepcopy(puzzle)
            p.move(direction)
            node = Node(p, parent=self)
            node.movement_cost = cost
            children.append(node)
            # print(f"Heuristic cost of {direction}: {h_1(p)}")
        children.sort()
        self.children = children
        return children


def h_0(puzzle):

    if puzzle.getState()[-1] == 0:
        return 0

    return 1

def h_0(puzzle):
    return puzzle.h_0()

def h_1(puzzle):
    return puzzle.getSumOfPermInv()

def h_2(puzzle):
    return puzzle.getManhattanDist()



def contains(node, _list):
    state = node.current_state.getState()

    for _, node in _list:
        if node.current_state.getState() == state:
            return True, node.g
    return False, -1

def replace(node, _list):
    state = node.current_state.getState()

    for i in range(len(_list)):
        if _list[i][1].current_state.getState() == state:
            _list[i] = (node.f, node)

def add_to_open(open_list, node):
    for n in open_list:
        if n.current_state.getState() == node.current_state.getState() and node.f > n.f:
            return False
    return True

def is_goal(node):
    g1, g2 = node.current_state.getFinal()
    state = node.current_state.getState()
    if state == g1 or state == g2:
        return True
    else:
        return False

def print_moves(node):
    out = []

    while node.parent != None:
        out.insert(0,node)
        node = node.parent

    for n in out:
        print(n.current_state.printState())
        print('')

def find_best(puzzle, h_i):
    open_list = []
    closed_list = []

    if h_i == 0:
        h = h_0
    elif h_i == 1:
        h = h_1
    else:
        h = h_2


    node = Node(puzzle)
    hq.heappush(open_list, (0, node))

    search_path = []#f g, h, puzzle state
    t0 = time.time()

    while open_list:
        f_cost, current_node = hq.heappop(open_list)
        search_path.append([f_cost, current_node.g, current_node.h, current_node.current_state.getState()])
        hq.heappush(closed_list, (f_cost, current_node))

        if is_goal(current_node):
            print(f"Found solution with cost of {current_node.g}")
            goal = current_node
            break

        children = current_node.computeChildren()

        for child_node in children:
            t1 = time.time()
            if t1 - t0 >= 60:
                print("Did not find a solution under 60 seconds")
                return

            in_closed, _ = contains(child_node, closed_list)
            in_open, open_cost = contains(child_node, open_list)
            
            if in_closed:
                continue
            elif not in_open:
                child_node.g = current_node.g + child_node.movement_cost
                child_node.h = h(child_node.current_state)
                child_node.f = child_node.g + child_node.h
                hq.heappush(open_list, (child_node.f, child_node))
            elif in_open and open_cost > current_node.g + child_node.movement_cost:
                child_node.g = current_node.g + child_node.movement_cost
                child_node.h = h(child_node.current_state)
                child_node.f = child_node.g + child_node.h
                replace(child_node, open_list)

    t1 = time.time()
    return search_path, goal.current_state.getSolution(), goal.current_state.getTotCost(), t1 - t0
