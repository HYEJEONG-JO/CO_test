def solution(cards1, cards2, goal):
    for words in goal:
        if cards1 and words == cards1[0]:
            cards1.pop(0)
            
        elif cards2 and words == cards2[0]:
            cards2.pop(0)
            
        else:
            return "No"
    return "Yes"