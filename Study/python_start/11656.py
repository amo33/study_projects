import sys 

string_input = sys.stdin.readline().rstrip('\n')
for result in sorted([string_input[i:] for i in range(len(string_input))]):
    print(result)