import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
ops = list(map(int, input().split()))  # +, -, *, /

max_result = float('-inf')
min_result = float('inf')


def dfs(idx, current):
    global max_result, min_result

    if idx == N:
        max_result = max(max_result, current)
        min_result = min(min_result, current)
        return

    if ops[0] > 0:
        ops[0] -= 1
        dfs(idx + 1, current + nums[idx])
        ops[0] += 1

    if ops[1] > 0:
        ops[1] -= 1
        dfs(idx + 1, current - nums[idx])
        ops[1] += 1

    if ops[2] > 0:
        ops[2] -= 1
        dfs(idx + 1, current * nums[idx])
        ops[2] += 1

    if ops[3] > 0:
        ops[3] -= 1
        dfs(idx + 1, int(current / nums[idx]))
        ops[3] += 1


# DFS 시작
dfs(1, nums[0])

# 결과 출력
print(max_result)
print(min_result)