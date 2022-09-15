def canVisitAllRooms(rooms):
    visited = set()
    stack = [0]

    while len(stack) > 0:
        current = stack.pop()
        visited.add(current)
        for adj in rooms[current]:
            if adj not in visited:
                stack.append(adj)
    return len(visited) == len(rooms)


print(canVisitAllRooms([[1], [2], [3], []]))
print(canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]]))
