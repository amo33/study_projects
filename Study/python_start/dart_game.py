import re 
def solution(dartResult):
    answer = 0
    power = {"S":1,"D":2,"T":3}
    sign = {"#":-1, "*":1}
    flag = 1
    temp = re.split('(\d+)',dartResult)
    res = []
    print(temp)
    for ele in temp:
        if ele.isdigit():
            res.append(int(ele))
            
        else:
            res.extend(list(ele))
    dartResult = res[::-1]
    print(dartResult)
    history = [1] * 3
    idx = 0
    for i,state in enumerate(dartResult):
        print(dartResult)
        if type(state) != int: # 숫자가 아니라면
            if type(dartResult[i+1]) == int: #만약 s,d,t라면 앞이 숫자 
                dartResult[i+1] = dartResult[i+1] ** power[dartResult[i]]             
                history[idx] *= dartResult[i+1]
                idx +=1
                # answer += int(dartResult[i+1]) ** power[dartResult[i]] * flag
            else: # * or # 
                
                history[idx] *= sign[dartResult[i]]
                if dartResult[i] == '*':
                    history[idx]*=2
                    if idx < 2:
                        history[idx+1] *= 2
        print(history)
    print(history)
    answer = sum(history)
    return answer
dartResult = "1T2D3D#"
print(solution(dartResult))