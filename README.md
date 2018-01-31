Search
======================

Introduction
------------

In this project we experimented with different AI search techniques like bfs, dfs, A* search in a Pacman environment. This is part of Pacman projects developed at [UC Berkeley](http://ai.berkeley.edu/project_overview.html). The Pacman agent needs to find paths through the maze world, both to reach a location and to collect food efficiently.


* Please refer to [report.pdf](Report.pdf) for detailed analysis.
* Please refer to [lab.pdf](lab.pdf) for about the project.

Directory Structure
-------------------

---search
	[search.py](search/search.py)
	[searchAgent.py](search/searchAgent.py)

---[lab.pdf](lab.pdf)

---README.md

---[report.pdf](Report.pdf)


Executing
---------

Then run the autograder using

$python autograder.py

It gave us a score of 26/25 (bonus for solving Q7).

Question specific commands

Question 1
----------
$python pacman.py -l tinyMaze -p SearchAgent
$python pacman.py -l mediumMaze -p SearchAgent
$python pacman.py -l bigMaze -z .5 -p SearchAgent

Question 2
----------
$python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
$python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5
$python eightpuzzle.py

Question 3
----------
$python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
$python pacman.py -l mediumDottedMaze -p StayEastSearchAgent
$python pacman.py -l mediumScaryMaze -p StayWestSearchAgent

Question 4
----------
$python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic

Question 5
----------
$python pacman.py -l tinyCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
$python pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem

Question 6
----------
$python pacman.py -l mediumCorners -p AStarCornersAgent -z 0.5

Question 7
----------
$python pacman.py -l testSearch -p AStarFoodSearchAgent
$python pacman.py -l trickySearch -p AStarFoodSearchAgent

Question 8
----------
$python pacman.py -l bigSearch -p ClosestDotSearchAgent -z .5

Developed by
Sai Srinadhu K, Sainath.

Acknowledgments: We thank Naman Goyal for letting us use the readme structure.
