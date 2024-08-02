import os
import json
import math
import heuristics

def load_dict(file: str) -> dict:
    """
    Load a dictionary from a JSON file.

    Args:
        file (str): The path to the JSON file.

    Returns:
        dict: The loaded dictionary.
    """
    if not os.path.isfile(file):
        print(f"{file} is missing!")
        exit(1)
    with open(file) as json_file:
        return json.load(json_file)

def print_result(task: callable, heuristic: callable=None, weight: float=0) -> tuple[list[str], float, int]:
    """
    Prints the result of a task, including the shortest path, shortest distance,
    total energy cost (if applicable), and number of nodes expanded. Optionally,
    it also prints the heuristic used and the weight applied.

    Args:
        task (callable): The task function to be executed.
        heuristic (callable, optional): The heuristic function to be used. Defaults to None.
        weight (float, optional): The weight to be applied to the heuristic. Defaults to 0.

    Returns:
        tuple[list[str], float, int]: A tuple containing the shortest path, shortest distance,
        and number of nodes expanded.
    """
    if heuristic is None:
        task_result = task()
    else:
        task_result = task(heuristic, weight)
    print(f"\nRunning {task.__name__}")
    print(f"Shortest path: S{'->'.join(task_result[0])[1:]}")
    print(f"Shortest distance: {task_result[1]}")
    if len(task_result) > 3:
        print(f"Total energy cost: {task_result[3]}")
    print(f"Nodes expanded: {task_result[2]}")
    if heuristic is not None:
        print(f"Heuristic: {heuristic.__name__}")
        print(f"Weight: {weight:.2f}")
    return task_result

def weight_tuning(task: callable, optimal_result: tuple[list[str], float, int, int | None], heuristics_list=(heuristics.euclidean, heuristics.manhattan, heuristics.chebyshev, heuristics.octile)):
    """
    Perform weight tuning for a given task using different heuristics.

    Args:
        task (callable): The task function to be optimized.
        optimal_result (tuple[list[str], float, int, int | None]): The optimal result for the task, represented as a tuple containing a list of strings denoting a path, the optimal distance, and the optimal number of expansions, and an optional amount of energy used. Obtained from the UCS implementation.
        heuristics_list (tuple, optional): The list of heuristics to be used for weight tuning. Defaults to (heuristics.euclidean, heuristics.manhattan, heuristics.chebyshev, heuristics.octile).

    Returns:
        None
    """
    print(f"\n{task.__name__} Weight Tuning")
    for heuristic in heuristics_list:
        print(f"{heuristic.__name__}: ", end='', flush=True)
        min_expansion = math.inf
        best_weight = 0
        # reduce weight by 0.01 each time
        for weight in range(100, 0, -1):
            task_result = task(heuristic, weight/100)
            distance, expanded = task_result[1], task_result[2]
            if int(distance) == int(optimal_result[1]):
                if expanded < min_expansion:
                    min_expansion = expanded
                    best_weight = weight
        print(f"Lowest is {min_expansion} @ weight {best_weight/100:.2f}; {(1 - min_expansion/optimal_result[2]):.1%} reduction") if best_weight != 0 else print("Not admissible.")