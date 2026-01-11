import sys

N = int(sys.stdin.readline())
answer = []

for i in range(N):
    cmd = sys.stdin.readline().split()
    
    if cmd[0] == '1':
        answer.append(int(cmd[1]))

    elif cmd[0] == '2':        
        if answer:
            print(answer.pop())
        else:
            print(-1)

    elif cmd[0] == '3':        
        print(len(answer))

    elif cmd[0] == '4':        
        print(1 if not answer else 0)

    elif cmd[0] == '5':        
        if answer:
            print(answer[-1])
        else:
            print(-1)