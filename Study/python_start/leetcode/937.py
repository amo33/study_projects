import sys

def reorderLogFiles(logs):
    lst_dig = []
    lst_let = []
    for log in logs:
        if log.split()[1].isdigit():
            lst_dig.append(log)
        else:
            lst_let.append(log)
        # print(lst_dig, lst_let)
    lst_let.sort(key=lambda x:(x.split()[1:], x.split()[0]))
    # print(lst_result)

    return lst_let + lst_dig

lst = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo","a2 act car"]
print(reorderLogFiles(lst))