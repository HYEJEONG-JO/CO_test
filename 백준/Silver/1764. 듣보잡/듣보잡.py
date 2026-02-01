import sys

N, M = map(int, sys.stdin.readline().split())

no_heard = set()
no_listen = set()

for i in range(N):
    no_heard.add(sys.stdin.readline().strip())
    
for j in range(M):
    no_listen.add(sys.stdin.readline().strip())
    
result = sorted(no_heard & no_listen)

print(len(result))

for k in result :
    print(k)