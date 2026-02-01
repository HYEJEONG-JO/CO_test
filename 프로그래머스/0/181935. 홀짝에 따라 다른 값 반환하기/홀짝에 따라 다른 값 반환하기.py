def solution(n):
    total = 0
    
    if n % 2 == 0 : # 짝수인 경우
        for i in range(2, n + 1, 2) :
            total += i**2
    else :
        for i in range(1, n + 1, 2) :
            total += i
            
    return total