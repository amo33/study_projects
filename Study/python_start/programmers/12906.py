def solution(arr):
    answer = []
    for num in arr:
        if answer[-1:] != [num]: # 현 문제에서는 배열에 연속된 값들 중 같은 값들은 한 개씩 뽑는 것이다. 
                                    # 따라서 answer[-1:] 으로 slicing 하면 빈 배열이어도 slicing이기 때문에 index 에러가 나오지 않는다.
            answer.append(num)
    return answer