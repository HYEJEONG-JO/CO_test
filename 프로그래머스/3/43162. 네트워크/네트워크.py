def solution(n, computers):
    visit = [False] * n
    count = 0

    def dfs(cur):
        visit[cur] = True
        for nxt in range(n):
            if computers[cur][nxt] == 1 and not visit[nxt]:
                dfs(nxt)

    for i in range(n):
        if not visit[i]:
            dfs(i)
            count += 1

    return count