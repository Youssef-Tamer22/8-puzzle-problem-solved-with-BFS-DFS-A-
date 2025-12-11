from dataclasses import dataclass

GOAL = (1,2,3,4,5,6,7,8,0)
IDX_TO_POS = {i: (i // 3, i % 3) for i in range(9)}

@dataclass(frozen=True, slots=True)
class PuzzleState:
    tiles: tuple[int, ...]

class Puzzle8:
    def __init__(self, initial_state, goal_state=GOAL):
        self.initial_state = PuzzleState(initial_state)
        self.goal_state = PuzzleState(goal_state)

    def is_goal(self, state: PuzzleState) -> bool:
        return state.tiles == self.goal_state.tiles

    def successors(self, state: PuzzleState):
        tiles = state.tiles
        i = tiles.index(0)
        r, c = divmod(i, 3)

        def swap(j):
            lst = list(tiles)
            lst[i], lst[j] = lst[j], lst[i]
            return tuple(lst)

        if r > 0:  yield PuzzleState(swap(i-3)), "Up", 1
        if r < 2:  yield PuzzleState(swap(i+3)), "Down", 1
        if c > 0:  yield PuzzleState(swap(i-1)), "Left", 1
        if c < 2:  yield PuzzleState(swap(i+1)), "Right", 1

    def heuristic(self, state: PuzzleState) -> int:
        dist = 0
        for idx, val in enumerate(state.tiles):
            if val == 0: continue
            gi = val - 1
            r1, c1 = IDX_TO_POS[idx]; r2, c2 = IDX_TO_POS[gi]
            dist += abs(r1 - r2) + abs(c1 - c2)
        return dist