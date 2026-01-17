def solution(n, lost, reserve):
    
    check_lost = set(lost) - set(reserve)
    check_reserve = set(reserve) - set(lost)
    check_lost_len = len(check_lost)

    for student in sorted(check_lost):
        if student - 1 in check_reserve:
            check_reserve.remove(student - 1)
            check_lost_len -= 1
            
        elif student + 1 in check_reserve:
            check_reserve.remove(student + 1)
            check_lost_len -= 1

    return n - check_lost_len