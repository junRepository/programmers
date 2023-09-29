def solution(seoul):
    for n, s in enumerate(seoul):
        if s == 'Kim':
            break
    return "김서방은 {}에 있다".format(n)