import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
ops = list(map(int, input().split()))  # +, -, *, /

max_result = -10**9
min_result = 10**9


def dfs(idx, current):
    global max_result, min_result

    # 모든 숫자를 다 사용한 경우
    if idx == N:
        max_result = max(max_result, current)
        min_result = min(min_result, current)
        return

    # 덧셈
    if ops[0] > 0:
        ops[0] -= 1
        dfs(idx + 1, current + nums[idx])
        ops[0] += 1

    # 뺄셈
    if ops[1] > 0:
        ops[1] -= 1
        dfs(idx + 1, current - nums[idx])
        ops[1] += 1

    # 곱셈
    if ops[2] > 0:
        ops[2] -= 1
        dfs(idx + 1, current * nums[idx])
        ops[2] += 1

    # 나눗셈
    if ops[3] > 0:
        ops[3] -= 1

        if current < 0:
            dfs(idx + 1, -(-current // nums[idx]))
        else:
            dfs(idx + 1, current // nums[idx])

        ops[3] += 1


dfs(1, nums[0])

print(max_result)
print(min_result)