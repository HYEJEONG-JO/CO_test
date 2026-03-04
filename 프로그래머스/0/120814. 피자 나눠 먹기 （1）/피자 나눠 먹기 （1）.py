import math

def solution(n):
    return (n / 7) if n % 7 == 0 else (math.ceil(n / 7))
