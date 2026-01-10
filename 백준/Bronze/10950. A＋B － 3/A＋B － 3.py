def add(count):
    for i in range(count):
        num1, num2 = map(int, input().split())
        print(num1 + num2)
        
count = int(input())        
add(count)