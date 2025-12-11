import argparse, time, json
from algorithms import bfs, dfs, astar
from problem.puzzle_8 import Puzzle8

ALGOS = {"bfs": bfs.bfs, "dfs": dfs.dfs, "astar": astar.astar}

def run(algorithm, initial, goal=None):
    prob = Puzzle8(initial, goal or (1,2,3,4,5,6,7,8,0))
    solver = ALGOS[algorithm]
    t0 = time.perf_counter()
    path, nodes = solver(prob, heuristic=prob.heuristic if algorithm=="astar" else None)
    dt = (time.perf_counter() - t0) * 1000
    return {"algorithm": algorithm, "length": len(path) if path else None,
            "nodes": nodes, "time_ms": round(dt, 3), "path": path}

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--algorithm", choices=ALGOS.keys(), required=True)
    ap.add_argument("--initial", required=True, help="Comma-separated tiles, e.g. 1,2,3,4,5,6,7,8,0")
    args = ap.parse_args()

    initial = tuple(int(x) for x in args.initial.split(","))
    result = run(args.algorithm, initial)
    print(json.dumps(result, indent=2))