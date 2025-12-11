8-Puzzle Solver
An implementation of the classic 8-Puzzle problem using multiple search algorithms (BFS, DFS, A*).
This project benchmarks each algorithm on solvable puzzle states and compares their performance in terms of:
- ✅ Nodes explored
- ✅ Solution length
- ✅ Execution time (ms)
- ✅ Memory usage (KB)
Results are saved and visualized to highlight the trade‑offs between algorithms.


🚀 How to Run
1. Run benchmarks

 python run_all.py

2. Plot metrics

python results/plot_metrics.py


1. This will:
- Run BFS, DFS, and A* on the chosen puzzle cases.
- Print clean Markdown tables.
- Save results into results/comparison.json.


2. This generates bar charts for:
- Nodes explored
- Solution length
- Execution time
- Memory usage

📊 Example Output
Benchmark Table
### Initial State: (1,2,3,4,8,0,7,6,5)

| Algorithm   |   Nodes Explored |   Solution Length |   Time (ms) |
|-------------|------------------|-------------------|-------------|
| BFS         |               46 |                 5 |       1.657 |
| DFS         |               31 |                31 |       1.165 |
| A*          |                5 |                 5 |       0.37  |

Visualization
Plots are generated in results/plot_metrics.py showing comparisons across algorithms.

🧠 Algorithms Implemented
- Breadth‑First Search (BFS) → guarantees shortest path, but explores many nodes.
- Depth‑First Search (DFS) → explores deep paths, often inefficient.
- A* → guided by heuristics (Manhattan distance), finds optimal solution efficiently.

📌 Features
- Clean modular architecture (separate algorithms, problem definitions, tests).
- Benchmark runner (run_all.py) with table + JSON output.
- Visualization of metrics with Matplotlib.
- Memory usage tracking via tracemalloc.

🛠 Requirements
- Python 3.8+
- Matplotlib
Install dependencies:
pip install -r requirements.txt



🎯 Goal
This project demonstrates how different search strategies perform on the same problem, highlighting the efficiency of A* compared to BFS and DFS.
