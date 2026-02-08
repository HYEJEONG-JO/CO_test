from collections import deque

def bfs(start, graph, visited, distance):
    queue = deque()
    queue.append(start)
    visited[start] = True
    distance[start] = 0   # 시작 노드 거리

    while queue:
        cur = queue.popleft()
        for nxt in graph[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                distance[nxt] = distance[cur] + 1
                queue.append(nxt)


def solution(n, edge):
    # BFS를 위한 그래프 생성
    graph = [[] for _ in range(n + 1)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)

    visited = [False] * (n + 1)
    distance = [0] * (n + 1)

    # BFS 실행
    bfs(1, graph, visited, distance)

    # 가장 먼 노드 세기
    max_dist = max(distance)
    answer = distance.count(max_dist)

    return answer
