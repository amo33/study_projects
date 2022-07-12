import sys 
N, M = map(int, sys.stdin.readline().strip().split())

result_lst = []

def check(val,candidate):
    for cand in candidate:
 
        if int(cand) > val:

            return False 
    return True 

def extract_candidate(idx, result_candidate):
    # print(num_dict)
    if idx == M:
        result_lst.append(list(result_candidate))
        return 
    for i in range(1,N+1):
        
        # print("c",candidate_add)
        if check(i, result_candidate):
            candidate_add = result_candidate + str(i)
            # print("c2",candidate_add)
            extract_candidate(idx+1, candidate_add)

extract_candidate(0, '')
for lst in result_lst:
    for j in range(M):
        print(int(lst[j]), end=" ")
    print()