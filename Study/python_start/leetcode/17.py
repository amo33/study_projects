def letterCombinations(digits: str):
    result_lst =[]
    def dfs(val,lst,result=''):
        # print('dfs check',val, len(lst))
        if val == len(lst):
            result_lst.append(result)
            return 
        for value in lst[val]:
            dfs(val+1,lst,result+str(value))
    digits_sequence = list(digits)
    if digits =="":
        return result_lst
    digit_dict = {
        '2':['a','b','c'],
        '3':['d','e','f'],
        '4':['g','h','i'],
        '5':['j','k','l'],
        '6':['m','n','o'],
        '7':['p','q','r','s'],
        '8':['t','u','v'],
        '9':['w','x','y','z']
    }
    selected = [digit_dict[val] for val in digits_sequence]
    # print(selected)
    dfs(0,selected)
    return result_lst
digits = "23"
print(letterCombinations(digits))