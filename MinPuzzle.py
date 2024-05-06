import heapq


def minEffort(puzzle):
    m = len(puzzle)
    n = len(puzzle[0])
    distances = [[float('inf')] * n for _ in range(m)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    pq = []
    heapq.heappush(pq, (0, 0, 0))
    distances[0][0] = 0

    while len(pq) > 0:
        effort, row, column = heapq.heappop(pq)

        if effort > distances[row][column]:
            continue

        for x, y in directions:
            new_row, new_column = row + x, column + y

            if m > new_row >= 0 and n > new_column >= 0:
                new_effort = max(effort, abs(puzzle[new_row][new_column] - puzzle[row][column]))
                if new_effort < distances[new_row][new_column]:
                    distances[new_row][new_column] = new_effort
                    heapq.heappush(pq, (new_effort, new_row, new_column))

    return distances[m-1][n-1]
