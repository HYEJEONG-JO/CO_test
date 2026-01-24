def solution(people, limit):
    answer = 0
    light = 0
    heavy = len(people) - 1
    people_sort = sorted(people)
    
    while (light <= heavy) :
        if people_sort[light] + people_sort[heavy] <= limit :
            light += 1
            heavy -= 1
            answer += 1
        else :
            heavy -= 1
            answer += 1
    return answer