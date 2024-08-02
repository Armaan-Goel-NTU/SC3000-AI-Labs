import heapq
from utils import load_dict, print_result, weight_tuning
import heuristics

# Constants
S, T = '1', '50'
BUDGET = 287932

# Load data
print("Loading Data")
coord = load_dict('Coord.json')
cost = load_dict('Cost.json')
dist = load_dict('Dist.json')
G = load_dict('G.json')

def task1(heuristic: callable, weight: float) -> tuple[list[str], float, int]:
    """
    Finds the shortest path from the start node (S) to the target node (T) using A* search algorithm.

    Args:
        heuristic (callable): A heuristic function that estimates the cost from a given node to the goal node.
        weight (float): The weight to be applied to the heuristic function.

    Returns:
        tuple[list[str], float, int]: A tuple containing the following:
            - A list of nodes representing the shortest path from S to T.
            - The total cost of the shortest path.
            - The number of nodes expanded during the search.
    """

    pq = [(0, S, [])]

    path_cost = {S: 0} 
    expanded = 0
    explored = set()

    while len(pq):
        _, current_node, path = heapq.heappop(pq)
        
        if current_node in explored:
            continue

        explored.add(current_node)
        expanded += 1

        if current_node == T:
            return (path+['T'], path_cost[current_node], expanded)

        for neighbor in G[current_node]:
            total_distance = path_cost[current_node] + dist[f"{current_node},{neighbor}"]
            if neighbor not in path_cost or total_distance < path_cost[neighbor]:
                heapq.heappush(pq,(total_distance + heuristic(coord[neighbor], coord[T], weight), neighbor, path + [current_node]))
                path_cost[neighbor] = total_distance

def task2() -> tuple[list[str], float, int, int]:
    """
    Finds the shortest path from the start node (S) to the target node (T) within a given budget.

    Returns:
        tuple[list[str], float, int, int]: A tuple containing the following:
            - path (list[str]): The shortest path from S to T.
            - node_distance (float): The total distance of the shortest path.
            - expanded (int): The number of nodes expanded during the search.
            - node_cost (int): The total cost (energy) of the shortest path.
    """
    pq = [(0,0,S,[])]
    energy_cost = {S: 0} 
    expanded = 0

    while len(pq):
        node_distance, node_cost, current_node, path = heapq.heappop(pq)

        expanded += 1
        if current_node == T:
            return (path + ['T'],node_distance,expanded,node_cost)

        for neighbor in G[current_node]:
            total_distance = node_distance + dist[f"{current_node},{neighbor}"]
            total_energy = node_cost + cost[f"{current_node},{neighbor}"]

            if total_energy <= BUDGET and (neighbor not in energy_cost or total_energy < energy_cost[neighbor]):
                heapq.heappush(pq,(total_distance, total_energy, neighbor, path + [current_node]))
                energy_cost[neighbor] = total_energy

def task3(heuristic: callable, weight: float) -> tuple[list[str], float, int, int]:
    """
    A* search algorithm to find the optimal path from the start node (S) to the target node (T) within a given budget.

    Args:
        heuristic (callable): A heuristic function that estimates the cost from a given node to the goal node.
        weight (float): The weight to be applied to the heuristic function.

    Returns:
        tuple[list[str], float, int, int]: A tuple containing the following:
            - path (list[str]): The shortest path from S to T.
            - node_distance (float): The total distance of the shortest path.
            - expanded (int): The number of nodes expanded during the search.
            - node_cost (int): The total cost (energy) of the shortest path.
    """
    pq = [(0,0,0,S,[])]
    energy_cost = {S: 0}
    expanded = 0

    while len(pq):
        _, node_cost, node_distance, current_node, path = heapq.heappop(pq)
        expanded += 1

        if current_node == T:
            return (path + ['T'],node_distance,expanded,node_cost)

        for neighbor in G[current_node]:
            total_distance = node_distance + dist[f"{current_node},{neighbor}"]
            total_energy = node_cost + cost[f"{current_node},{neighbor}"]

            if total_energy <= BUDGET and (neighbor not in energy_cost or total_energy < energy_cost[neighbor]):
                heuristic_cost = heuristic(coord[neighbor], coord[T], weight)
                heapq.heappush(pq,(total_distance + heuristic_cost, total_energy, total_distance, neighbor, path + [current_node]))
                energy_cost[neighbor] = total_energy

def task1_ucs() -> tuple[list[str], float, int]:
    """
    Performs Uniform Cost Search (UCS) algorithm to find the optimal path from the start node (S) to the target node (T).

    Returns:
        tuple[list[str], float, int]: A tuple containing the following:
            - A list of nodes representing the shortest path from S to T.
            - The total cost of the shortest path.
            - The number of nodes expanded during the search.
    """
    pq = [(0, S, [])]
    path_cost = {S: 0} 
    expanded = 0
    explored = set()

    while len(pq):
        _, current_node, path = heapq.heappop(pq)

        if current_node in explored:
            continue
        
        explored.add(current_node)
        expanded += 1

        if current_node == T:
            return (path+['T'], path_cost[current_node], expanded)

        for neighbor in G[current_node]:
            total_distance = path_cost[current_node] + dist[f"{current_node},{neighbor}"]
            if neighbor not in path_cost or total_distance < path_cost[neighbor]:
                heapq.heappush(pq, (total_distance, neighbor, path + [current_node]))
                path_cost[neighbor] = total_distance
                
def task3_alt(heuristic: callable, weight: float) -> tuple[list[str], float, int, int]:
    """
    Alternate A* search algorithm to find the optimal path from the start node (S) to the target node (T) within a given budget.

    Args:
        heuristic (callable): A heuristic function that estimates the cost from a given node to the goal node.
        weight (float): The weight to be applied to the heuristic function.

    Returns:
        tuple[list[str], float, int, int]: A tuple containing the following:
            - path (list[str]): The shortest path from S to T.
            - node_distance (float): The total distance of the shortest path.
            - expanded (int): The number of nodes expanded during the search.
            - node_cost (int): The total cost (energy) of the shortest path.
    """
    pq = [(0,0,S,[])]
    path_cost = {S: 0} 
    expanded = 0

    while len(pq):
        _, node_cost, current_node, path = heapq.heappop(pq)

        expanded += 1

        if current_node == T:
            return (path + ['T'],path_cost[T],expanded,node_cost)

        for neighbor in G[current_node]:
            total_distance = path_cost[current_node] + dist[f"{current_node},{neighbor}"]
            total_energy = node_cost + cost[f"{current_node},{neighbor}"]

            if total_energy <= BUDGET and (neighbor not in path_cost or total_distance < path_cost[neighbor]):
                heapq.heappush(pq, (total_distance + heuristic(coord[neighbor], coord[T], weight), total_energy, neighbor, path + [current_node]))
                path_cost[neighbor] = total_distance
 
def task3_weighted_energy() -> tuple[list[str], float, int]:
    """
    Alternate A* search algorithm to find the optimal path from the start node (S) to the target node (T) within a given budget.
    Uses (energy cost * 0.1) as the heuristic.

    Returns:
        tuple[list[str], float, int]: A tuple containing the following:
            - A list of nodes representing the shortest path from S to T.
            - The total cost of the shortest path.
            - The number of nodes expanded during the search.
    """
    pq = [(0, S, [])]

    path_cost = {S: 0} 
    energy_cost = {S: 0}
    expanded = 0
    explored = set()

    while len(pq):
        _, current_node, path = heapq.heappop(pq)
        
        if current_node in explored:
            continue

        explored.add(current_node)
        expanded += 1

        if current_node == T:
            return (path+['T'], path_cost[current_node], expanded)

        for neighbor in G[current_node]:
            total_distance = path_cost[current_node] + dist[f"{current_node},{neighbor}"]
            total_energy = energy_cost[current_node] + cost[f"{current_node},{neighbor}"]
            if neighbor not in path_cost or total_distance < path_cost[neighbor]:
                heapq.heappush(pq,(total_distance + 0.1 * total_energy, neighbor, path + [current_node]))
                path_cost[neighbor] = total_distance
                energy_cost[neighbor] = total_energy
                

# UCS results are saved for weight tuning
task1_ucs_result = print_result(task1_ucs)
print_result(task1, heuristics.octile, 1)

task2_result = print_result(task2)
print_result(task3, heuristics.manhattan, 0.76)
print_result(task3_alt, heuristics.manhattan, 0.89)
print_result(task3_weighted_energy)

# Weight tuning
weight_tuning(task1, task1_ucs_result)
weight_tuning(task3, task2_result)
weight_tuning(task3_alt, task2_result)
