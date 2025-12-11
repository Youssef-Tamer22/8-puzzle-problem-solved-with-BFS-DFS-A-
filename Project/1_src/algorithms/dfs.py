def dfs(problem, max_depth=50):
    stack = [(problem.initial_state, 0)]
    parent = {problem.initial_state: None}
    visited = set()
    expansions = 0

    while stack:
        state, depth = stack.pop()
        if state in visited:
            continue
        visited.add(state)
        if problem.is_goal(state):
            return reconstruct_path(parent, state), expansions
        if depth < max_depth:
            for nxt, action, _ in problem.successors(state):
                if nxt not in parent:
                    parent[nxt] = (state, action)
                    stack.append((nxt, depth + 1))
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