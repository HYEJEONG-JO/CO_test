N = int(input())

for case in range(1, N + 1):
    L = input().split()
    answer = L[::-1]
    print(f"Case #{case}: {' '.join(answer)}")