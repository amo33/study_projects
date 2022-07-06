import sys 

# 유클리드 호제법 최대공약수 (b, a%b)를 나눈 값 중 0 이 나온것과 같다.
N, M = map(int, input().split(' '))
def gcd(a,b):
    while a > 0:
        r = a%b 
        if r == 0:
            return b 
        else:
            a = b 
            b = r 
if N < M:
    N, M = M, N
print('1' * gcd(N, M))
# result = 10**(gcd(N,M))//9
# print(result)

# print(lcm(N, M))