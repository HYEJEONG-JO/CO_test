def solution(number, k):
    list_number = []
    
    for num in number:
        if list_number:
            while k > 0:
                if not list_number:
                    break
                
                if list_number[-1] < num:
                    list_number.pop()
                    k -= 1
                else:
                    break
                    
        list_number.append(num)
    
    # 앞쪽 숫자들이 나올 수 있는 가장 큰 숫자일 경우
    if k > 0:
        list_number = list_number[:-k]
    
    return ''.join(list_number)