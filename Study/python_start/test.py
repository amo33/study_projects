
import re 
def parse1():
    for line in open("Study\python_start\log.txt"):
        print(line.split("[")[1].split("]")[0])

def parse2():
    for line in open("Study\python_start\log.txt", "r"):
        print(line.split()[3].strip("[]"))

def parse3():
    for line in open("Study\python_start\log.txt", "r"):
        print(" ".join(line.split("[" or "]")[3:5]))

def parse4():
    for line in open("Study\python_start\log.txt", "rw"):
        print(" ".join(line.split()[3:5]).strip("[]"))
  
def parse5():
    for line in open("Study\python_start\log.txt"):
        print(re.split("\[|\]", line)[1])
parse5()

'''

Expected output:
01/Mar/2022:13:05:05 +0900
01/Mar/2022:13:05:10 +0900
"""'''