import heapq
import itertools

def astar(problem, heuristic=None):
    h = heuristic or problem.heuristic
    start = problem.initial_state
    g = {start: 0}
    parent = {start: None}
    counter = itertools.count()  # unique sequence count
    frontier = [(h(start), next(counter), start)]
    expansions = 0

    while frontier:
        f, _, state = heapq.heappop(frontier)
        if problem.is_goal(state):
            return reconstruct_path(parent, state), expansions
        for nxt, action, cost in problem.successors(state):
            ng = g[state] + cost
            if nxt not in g or ng < g[nxt]:
                g[nxt] = ng
                parent[nxt] = (state, action)
                f_nxt = ng + h(nxt)
                heapq.heappush(frontier, (f_nxt, next(counter), nxt))
        expansions += 1
    return None, expansions
def reconstruct_path(parent, goal):
    actions = []
    cur = goal
    while parent[cur] is not None:
        prev, act = parent[cur]
        actions.append(act)
        cur = prev
    return actions[::-1]