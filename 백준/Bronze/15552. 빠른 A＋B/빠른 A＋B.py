import sys
N = int(sys.stdin.readline())

for i in range(N) :
    num1, num2 = map(int, sys.stdin.readline().split())
    print(num1 + num2)