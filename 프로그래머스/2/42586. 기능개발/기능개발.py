import math
from collections import deque

def solution(progresses, speeds):
    days = deque()
    
    for i in range(len(progresses)):
        temp = 100 - progresses[i]
        
        day = math.ceil(temp / speeds[i])
        days.append(day)
        
    answer = []
    
    while days:
        base = days.popleft()
        count = 1
        
        while days and days[0] <= base :
            days.popleft()
            
            count += 1
        answer.append(count)
        
    return answer