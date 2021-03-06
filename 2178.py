import sys
from collections import deque
N,M = map(int,sys.stdin.readline().split())
graph = []
for i in range(N):
    graph.append(list(map(int,sys.stdin.readline().strip())))
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(x,y):
    queue = deque()
    queue.append([x,y])
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위를 벗어난 경우 무시
            if nx<0 or ny<0 or nx>=N or ny>=M:
                continue
            # 0일 경우 무시
            if graph[nx][ny]==0:
                continue
            # 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y]+1
                queue.append([nx,ny])
    return graph[N-1][M-1]
print(bfs(0,0))