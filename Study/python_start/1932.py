import sys

layer = int(sys.stdin.readline())

dp = [[0 for col in range(layer+1)] for row in range(layer)]
bag = []

for i in range(layer):
    bag.append(list(map(int, input().split())))

if layer is 1:

    print(bag[0][0])

else:
    dp[0][1] = bag[0][0]
    dp[1][1] = bag[1][0] + dp[0][1]
    dp[1][2] = bag[1][1] + dp[0][1]


    point = 2
    for i in range(2,layer):
        point += 1
        for j in range(point):
            dp[i][j+1] = bag[i][j] + max(dp[i-1][j] , dp[i-1][j+1]) 

    print(max(map(max, dp)))