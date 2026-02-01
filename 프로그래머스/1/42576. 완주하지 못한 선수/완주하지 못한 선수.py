def solution(participant, completion):
    com_par = {}
    
    for name in participant :
        com_par[name] = com_par.get(name, 0) + 1
        
    for name in completion :
        com_par[name] -= 1
    
    for name in com_par :
        if com_par[name] > 0 :
            return name