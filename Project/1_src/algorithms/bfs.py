from collections import deque

def bfs(problem):
    start = problem.initial_state
    frontier = deque([start])
    parent = {start: None}
    expansions = 0

    while frontier:
        state = frontier.popleft()
        if problem.is_goal(state):
            return reconstruct_path(parent, state), expansions
        for nxt, action, _ in problem.successors(state):
            if nxt not in parent:
                parent[nxt] = (state, action)
                frontier.append(nxt)
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