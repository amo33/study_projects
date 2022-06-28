arr = []
while True:
    try:
        val = input()
    except EOFError:
        break 
    print(val)