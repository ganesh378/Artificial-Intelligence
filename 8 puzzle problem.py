import heapq

def find_blank_square(state):
    """Return the row and column of the blank square in the puzzle."""
    for row in range(3):
        for col in range(3):
            if state[row][col] == 0:
                return row, col

def valid_moves(blank_row, blank_col):
    """Return a list of valid moves given the location of the blank square."""
    moves = []
    if blank_row > 0:
        moves.append((blank_row - 1, blank_col))
    if blank_col > 0:
        moves.append((blank_row, blank_col - 1))
    if blank_row < 2:
        moves.append((blank_row + 1, blank_col))
    if blank_col < 2:
        moves.append((blank_row, blank_col + 1))
    return moves

def make_move(state, move):
    """Return a new state after making the given move."""
    blank_row, blank_col = find_blank_square(state)
    new_state = [list(row) for row in state]
    new_state[blank_row][blank_col], new_state[move[0]][move[1]] = new_state[move[0]][move[1]], new_state[blank_row][blank_col]
    return tuple(tuple(row) for row in new_state)

def manhattan_distance(state, goal_state):
    """Return the Manhattan distance between two states."""
    distance = 0
    for row in range(3):
        for col in range(3):
            val = state[row][col]
            goal_row, goal_col = (val // 3, val % 3) if val else (2, 2)
            distance += abs(row - goal_row) + abs(col - goal_col)
    return distance

def solve_puzzle(start, goal):
    """Return a list of moves to solve the puzzle."""
    heap = [(manhattan_distance(start, goal), 0, start, [])]
    visited = set()
    while heap:
        _, moves, state, path = heapq.heappop(heap)
        if state == goal:
            return path
        if state in visited:
            continue
        visited.add(state)
        blank_row, blank_col = find_blank_square(state)
        for move in valid_moves(blank_row, blank_col):
            new_state = make_move(state, move)
            heapq.heappush(heap, (manhattan_distance(new_state, goal) + moves + 1, moves + 1, new_state, path + [move]))

# Example usage
start = ((1, 2, 3), (5, 6, 0), (7, 8, 4))
goal = ((1, 2, 3), (5, 8, 6), (0, 7, 4))
path = solve_puzzle(start, goal)
print(path)
