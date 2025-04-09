from algorithms.depth_first_search import dfs_fun
from algorithms.breadth_first_search import bfs_fun
from algorithms.a_star_search import a_star_fun
from algorithms.greedy_best_first_search import gbfs_fun
from algorithms.custom1 import custom_search_1
from algorithms.custom2 import custom_search_2

def dfs(problem):
    dfs_fun(problem)

def bfs(problem):
    bfs_fun(problem)

def a_star(problem):
    a_star_fun(problem)

def gbfs(problem):
    gbfs_fun(problem)
    
def cus1(problem):
    custom_search_1(problem)

def cus2(problem):
    custom_search_2(problem)