from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def solution(maps):
    queue = deque()
    queue.append((0, 0))
    while queue:
        cur_x, cur_y = queue.popleft()
        for k in range(4):
            nx = cur_x + dx[k]
            ny = cur_y + dy[k]
            if nx == len(maps)-1 and ny == len(maps[0])-1:
                return maps[cur_x][cur_y]+1
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and maps[nx][ny] == 1:
                queue.append((nx, ny))
                maps[nx][ny] = maps[cur_x][cur_y]+1
    return -1

#maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
maps = [
    [1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 0, 0],
    [0, 0, 0, 1, 1],
]
print(solution(maps))


