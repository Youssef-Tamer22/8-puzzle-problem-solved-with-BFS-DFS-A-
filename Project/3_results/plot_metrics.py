import json
import matplotlib.pyplot as plt

# Load results
with open("results/comparison.json", "r") as f:
    data = json.load(f)

algorithms = [d["Algorithm"] for d in data]
nodes = [d["Nodes Explored"] for d in data]
lengths = [d["Solution Length"] for d in data]
times = [d["Time (ms)"] for d in data]
memory = [d["Space (KB)"] for d in data]

# --- Plot 1: Nodes explored ---
plt.figure(figsize=(8,5))
plt.bar(algorithms, nodes, color=["skyblue","salmon","lightgreen"])
plt.title("Nodes Explored by Algorithm")
plt.ylabel("Nodes Explored")
plt.xlabel("Algorithm")
plt.tight_layout()
plt.show()

# --- Plot 2: Solution length ---
plt.figure(figsize=(8,5))
plt.bar(algorithms, lengths, color=["skyblue","salmon","lightgreen"])
plt.title("Solution Optimality by Algorithm")
plt.ylabel("Steps in Solution Path")
plt.xlabel("Algorithm")
plt.tight_layout()
plt.show()

# --- Plot 3: Time ---
plt.figure(figsize=(8,5))
plt.bar(algorithms, times, color=["skyblue","salmon","lightgreen"])
plt.title("Execution Time by Algorithm")
plt.ylabel("Time (ms)")
plt.xlabel("Algorithm")
plt.tight_layout()
plt.show()


    # Memory usage
plt.figure(figsize=(8,5))
plt.bar(algorithms, memory, color=["skyblue","lightgreen","salmon"])
plt.title('Memory usage')
plt.ylabel("KB")
plt.show()