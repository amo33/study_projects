import collections 

def solution(cargo,total_weight):
    cargo = sorted(cargo , key = lambda x: [x[1] / x[0] , x[0], x[1]], reverse=True)
    print(cargo)
    result_cost = 0
    while total_weight and cargo:
        cost , weight = cargo.pop()
        if total_weight > weight:
            total_weight -= weight
            result_cost += cost 
        else:
            result_cost += total_weight * (cost / weight)
    return result_cost 

info = [
    (4,12),
    (2,1),
    (10,4),
    (1,1),
    (2,2)
]
total = 15

print(solution(info, total))
            