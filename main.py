from puzzle import Puzzle
from gbfs import gbfs
from ucs import ucs
import out
import random
import a_star
import json

# A.find_best(puzzle)


puzzNum = 0

puzzle1 = Puzzle([2, 3, 5, 7, 0, 4, 6, 1],2, 4)
puzzle2 = Puzzle([5,2,3, 1, 0, 6, 7, 4], 2, 4)
puzzle3 = Puzzle([5, 2, 3, 4, 6, 0, 7, 1], 2, 4)
puzzle4 = Puzzle([1, 3, 5, 7, 2, 0, 4, 6], 2, 4)
puzzle5 = Puzzle([1, 2, 3, 4, 6, 0, 7, 5], 2, 4)
#puzzle = Puzzle([3, 2, 4, 1, 0, 7, 6, 5])
# gbfs_h0 = gbfs(puzzle, 0) 
# gbfs_h1 = gbfs(puzzle, 1)
# gbfs_h2 = gbfs(puzzle, 2)

#Output

#READ
#	****look at my return function in gbfs for details on the parameters of the output file functions**********
#	search takes in a list of lists per itteration so i append a list of [score, score, score, currentState] at each itteration for search
#	solution file takes in the (finalNode.getSolution(), finalScore, time) is a tuple,
#	I returned everything i needed when i call my fucntion so everyting is avalable for calling 

# out.solutionFile(astar_sol[1:], f'{puzzNum}_astar-h2_solution')
# out.searchFile(astar_sol[0], f'{puzzNum}_astar-h2_search')
# out.solutionFile(gbfs_h2[1:], f'{puzzNum}_gbfs-h2_solution')
# out.searchFile(gbfs_h2[0], f'{puzzNum}_gbfs-h2_search')

#UCS algo output files
puzzles = []
puzzles.append(puzzle1)
puzzles.append(puzzle2)
puzzles.append(puzzle3)
puzzles.append(puzzle4)
puzzles.append(puzzle5)

for i, p in enumerate(puzzles):
	output = a_star.find_best(p, 0)
	if output is None:
		out.solutionFile(output, f'{i}_astar_solution')
		out.searchFile(output, f'{i}_astar_search')
	else:
		out.solutionFile(output[1:], f'{i}_astar_solution')
		out.searchFile(output[0], f'{i}_astar_search')


#Analysis
"""""
puzzles = []
with open('puzzles.txt', 'r') as f:
	puzzles = [json.loads(line) for line in f]
nb_puzzles = len(puzzles)
print(puzzles)

total_length_solution =0
total_length_search = 0
total_nb_nosolution = 0
total_cost = 0
total_execution_time = 0

for x in puzzles:
	puzzle = Puzzle(x, 2, 4)
	output = a_star.find_best(puzzle, 2)
	output = gbfs(
	if(output != None):
		total_length_search += len(output[0])
		total_length_solution += len(output[1])
		total_cost += output[2]
		total_execution_time += output[3]
	else:
		total_nb_nosolution += 1
		nb_puzzles -= 1

average_length_solution = total_length_solution/nb_puzzles
average_length_search = total_length_search/nb_puzzles
average_nb_nosolution = total_nb_nosolution/nb_puzzles
average_cost = total_cost/nb_puzzles
average_execution_time = total_execution_time/nb_puzzles

algo_name = 'astar-h2'
with open(f'{algo_name}_analysis.txt', 'w')as f:
	f.write(f'Total length of search: {total_length_search}\n')
	f.write(f'Total length of solution: {total_length_solution}\n')
	f.write(f'Total number of no solution: {total_nb_nosolution}\n')
	f.write(f'Total cost: {total_cost}\n')
	f.write(f'Total execution time: {total_execution_time}\n\n')

	f.write(f'Average length of search: {average_length_search}\n')
	f.write(f'Average length of solution: {average_length_solution}\n')
	f.write(f'Average number of no solution: {average_nb_nosolution}\n')
	f.write(f'Average cost: {average_cost}\n')
	f.write(f'Average execution time: {average_execution_time}\n')
"""""