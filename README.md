# pacman
https://github.com/mtwig95/pacman
## Overview
In this project, your Pacman agent will navigate a maze efficiently in order to reach a certain location and collect food. I developed search algorithms to apply to Pacman scenarios.
Code was added to search.py and searchAgents.py.

## Run
Below are the commands listed in commands.txt.

In the command line, type the following command to play Pacman `python pacman.py`

pacman.py supports several options. To see a list of all options and their default values, use:
`python pacman.py -h`

Run the following commands to verify the SearchAgent file is working properly:
`python pacman.py -l tinyMaze -p SearchAgent -a fn=tinyMazeSearch`

A route plan through Pacman's world will be built by implementing search algorithms

## q1
### Using depth-first search (DFS) to find a fixed food point
* watch: `python pacman.py -l mediumMaze -p SearchAgent`

* test: `python autograder.py -q q1`


DFS performs a deep search, so it follows the first route it finds that reaches our target point. The first route it sees may not be the cheapest, as DFS is not an optimal algorithm.


## q2
### Breadth First Search
* watch: `python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs`

* test: `python autograder.py -q q2`


As long as our price function does not change (i.e., the cost of each path is equal to the other), the BFS will find the cheapest route since it is optimal.
It goes layer by layer until it reaches its destination.  Since BFS treats every price as having the same value, it will not find the cheapest route if the price function changes.


## q3
### Changing the cost function
* watch: `python pacman.py -l mediumMaze -p SearchAgent`

* test: `python autograder.py -q q1`


A rational Pacman agent should adapt his behavior according to the situation. By changing the cost function, we can encourage Pacman to take different paths.


## q4
### A* Search
* watch: `python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic`

* test: `python autograder.py -q q4`


A* accepts a heuristic function as an argument. A heuristic takes two arguments: the state of the search problem (the main argument), and the problem itself (as reference information).


## q5
### Make sure all corners are covered
* watch: `python pacman.py -l tinyCorners -p SearchAgent -a fn=bfs,prob=CornersProblem`
* watch: `python pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem`

* test: `python autograder.py -q q5`


The hint led me to realize that every mode of the game contains Pacman's location and the number of corners I visited. It automatically adds a corner to the corners I visit if the starting mode is a corner.
A goal state occurs when all four corners of the game have been reached. Every time I reach a corner I haven't been to yet, I add it to the set, and the returned state includes those corners as well. Pacman does not pass through walls, of course.

## q6
### The problem of heuristic cornering
* watch: `python pacman.py -l mediumCorners -p AStarCornersAgent -z 0.5`

* test: `python autograder.py -q q6`


Clearly, the heuristic used in the above question relies on only having four corners (at most); if we had more corners, the complexity would be much greater.
Using the Manhattan distances in Util.py, a subproblem heuristic that disregards walls was implemented, which made the evaluation optimistic and therefore admissible.
We look at all possible orders of how to choose the route that passes through all four corners (with Manhattan distances, there are 24 options and four assembly points). 
From those routes, we select the shortest route, the one that is the cheapest and has the least intersections.  741 nodes have been developed.


## q7
### Eat all the points
* watch: `python pacman.py -l testSearch -p AStarFoodSearchAgent`
* watch: `python pacman.py -l trickySearch -p AStarFoodSearchAgent`

* test: `python autograder.py -q q7`


After checking for food, the heuristic returns 0. The remaining food is entered into the heuristic information dictionary, where the key is the location, and the value is the distance (using Manhattan distances implemented in util) from the location to the current one.
We won't check the distance between a certain food and a certain location again if it has already been checked once. Each round, Pacman's distance from the remaining foods is entered into a new dictionary.
The key is the location of the food, and the value is its distance from Pacman's location. Then she calculates Manhattan distances between the most distant and nearest foods. 
Returns the distance from Manhattan to Pacman's closest food and the distance from Pacman to the furthest food. Finally, 8608 nodes have been developed.
A reason why the heuristic is acceptable is that the Manhattan distance from the closest food to the nearest food is less than or equal to the actual distance (as I explained earlier); and the Manhattan distance from the closest food to the furthest food is less than or equal to the real distance.
Therefore, the total solution is less than the sum of the distances between them. When I have more than two foods left, I have to pass through more points on the board, so it's actually shorter than reaching the goal state. 
As I explained 2 sentences earlier, when I have exactly 2 foods left, the distance is definitely shorter than or equal to the real distance. 
The distance returned is the distance from Manhattan to the last meal when I only have 1 forewarning. Therefore, it is less than or equal to the solution.

## q8
### Non-optimal search
* watch: `python pacman.py -l bigSearch -p ClosestDotSearchAgent -z .5`

* test: `python autograder.py -q q8`


The objective test was defined as the presence of food at one point. This means we must perform BFBFSntil it finds the target, which is that food is available at a specific location. This solution solves the bigSearch maze in less than a second with 350 routes. It takes the same amount of time to get to the nearest food.