import time
import tracemalloc
import json
import pytest
from src.algorithms import bfs, dfs, astar
from src.problem.puzzle_8 import Puzzle8

CASES = [
    (1,2,3,
     4,8,0,
     7,6,5)
]

try:
    from tabulate import tabulate
except ImportError:
    tabulate = None

ALGOS = {
    "BFS": lambda prob: bfs.bfs(prob),
    "DFS": lambda prob: dfs.dfs(prob, max_depth=50),
    "A*":  lambda prob: astar.astar(prob, heuristic=prob.heuristic),
}

@pytest.mark.parametrize("initial", CASES)
def test_comparison(initial):
    prob = Puzzle8(initial)
    results = []

    for name, runner in ALGOS.items():
        tracemalloc.start()
        t0 = time.perf_counter()
        path, nodes = runner(prob)
        dt = (time.perf_counter() - t0) * 1000
        _, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        length = len(path) if path else None
        results.append({
            "Algorithm": name,
            "Nodes Explored": nodes,
            "Solution Length": length,
            "Time (ms)": round(dt, 3),
            "Space (KB)": round(peak/1024, 2),
        })

    # Print table
    headers = ["Algorithm", "Nodes Explored", "Solution Length", "Time (ms)"]
    table_data = [[r[h] for h in headers] for r in results]
    if tabulate:
        print(tabulate(table_data, headers=headers, tablefmt="github"))
    else:
        print("| " + " | ".join(headers) + " |")
        print("| " + " | ".join(["-"*len(h) for h in headers]) + " |")
        for row in table_data:
            print("| " + " | ".join(str(x) for x in row) + " |")

    # Save results for visualization
    with open("results/comparison.json", "w") as f:
        json.dump(results, f, indent=2)

    # Basic sanity checks
    for r in results:
        assert r["Nodes Explored"] >= 0
        assert r["Time (ms)"] >= 0
        
