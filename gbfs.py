import copy
import time 

def gbfs(puzzle, h):
	start = time.time()
	openList = []
	closeList = []
	search = []
	openList.append(puzzle) #appending the initial node

	while not closeList or not closeList[-1].isGoal(): #as long is it dosnt find the goal keep loopin
		search.append([0,0,openList[0].getSumOfPermInv(), openList[0].getState()])		
		populateOpenList(openList, closeList)
		closeList.append(openList.pop(0))
		if h == 1:
			openList.sort(key=lambda x : x.getSumOfPermInv()) #this sorts the list using sum of inv perm
		if h == 2:
			openList.sort(key=lambda x : x.getManhattanDist()) #this sorts the list using sum of inv perm
		now = time.time()
		if (now-start) > 60:
			return
	return search, closeList[-1].getSolution(), closeList[-1].getTotCost(), now-start
 
def populateOpenList(openList, closeList):
	for x in openList[0].getMoves():
		p = copy.deepcopy(openList[0])
		p.move(x[0])
		if p.getState() not in [x.getState() for x in closeList] and p.getState() not in [x.getState() for x in openList]: #checks lists
			openList.append(p)


		
