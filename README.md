Search
======================

Introduction
------------

In this project we experimented with different AI search techniques like BFS, DFS, A* search in a Pacman environment. This is part of Pacman projects developed at [UC Berkeley](http://ai.berkeley.edu/project_overview.html). The Pacman agent needs to find paths through the maze world, both to reach a location and to collect food efficiently.

Directory Structure
-------------------

---search
	[search.py](search/search.py)
	[searchAgent.py](search/searchAgent.py)

---[lab.pdf](lab.pdf)

---README.md

---[report.pdf](report.pdf)


Executing
---------

Then run the autograder using

$python autograder.py

It gave us a score of 26/25 (bonus for solving Q7).

Task specific commands

Finding a Fixed Food Dot using Depth First Search
-------------------------------------------------
$python pacman.py -l tinyMaze -p SearchAgent_
$python pacman.py -l mediumMaze -p SearchAgent
$python pacman.py -l bigMaze -z .5 -p SearchAgent

Breadth First Search
--------------------
$python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
$python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5
$python eightpuzzle.py

Varying the Cost Function
-------------------------
$python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
$python pacman.py -l mediumDottedMaze -p StayEastSearchAgent
$python pacman.py -l mediumScaryMaze -p StayWestSearchAgent

A* search
---------
$python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic

Finding All the Corners
-----------------------
$python pacman.py -l tinyCorners -p SearchAgent -a fn=bfs,prob=CornersProblem_
$python pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem

Corners Problem: Heuristic
--------------------------
$python pacman.py -l mediumCorners -p AStarCornersAgent -z 0.5

Eating All The Dots
-------------------
$python pacman.py -l testSearch -p AStarFoodSearchAgent
$python pacman.py -l trickySearch -p AStarFoodSearchAgent

Suboptimal Search
-----------------
$python pacman.py -l bigSearch -p ClosestDotSearchAgent -z .5

Developed by
------------
Sai Srinadhu K, Venkat Sainath T.
