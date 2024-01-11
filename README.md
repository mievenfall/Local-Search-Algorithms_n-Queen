# Local-Search-Algorithms_n-Queen
CS 4200 - Artificial Intelligence Project 2

This program implements local search algorithms to solve n-Queen problems.

## Description
The n-Queen problem is the problem of putting n chess queens on an n x n chessboard such that none of them can capture any other using the standard chess queen’s moves. The queens must be placed in such a way that no two queens would be able to attack each other

This program performs the local search algorithms, including (1) Straight-Forward Steepest-Ascent Hill Climbing and (2) Genetic Algorithm to solve n-Queen problems. It uses the number of conflicts in the chessboard as the heuristic to guide the search.

## Usage
To use the program:

- Navigate to the `/src` directory
- Run `python main.py`
- Follow the prompts to enter the number of instances for n-Queen problems
- With instance < 5, the program will print the initial board and final board to the output, with the result for each board and the average result.
- With instance >=5, the program will only print the average result.
