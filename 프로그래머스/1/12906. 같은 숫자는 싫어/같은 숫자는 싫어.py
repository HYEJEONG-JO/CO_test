def solution(arr):
    answer = []
    
    for i in range(len(arr)) :
        
        if not answer :
            answer.append(arr[i])
            
        elif arr[i] != answer[-1] :
            answer.append(arr[i])
            
    return answer