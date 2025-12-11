import subprocess
import sys

def main():
    print("▶ Running comparison tests (BFS, DFS, A*)...")
    subprocess.run([sys.executable, "-m", "pytest", "-s", "tests/test_algorithms.py"])
    print("\n▶ Done! Results saved in results/comparison.json")

if __name__ == "__main__":
    main()
    