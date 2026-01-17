from collections import deque

def solution(priorities, location):
    
    queue = deque(enumerate(priorities))
    sorted_priorities = sorted(priorities, reverse = True)

    execute = 0

    while queue :
        idx, p = queue.popleft()
        
        if p == sorted_priorities[0] :
            execute += 1
            sorted_priorities.pop(0)
            
            if idx == location :
                print(execute)
                return execute
            
        else :
            queue.append((idx, p))
    