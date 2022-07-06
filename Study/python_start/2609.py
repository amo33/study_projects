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
def lcm(a,b): # 최소공배수는 두 수의 곱을 최대공약수로 나눈 것과 같다.
    return int((a*b)/ gcd(a,b))
if N < M:
    N, M = M, N
print(N,M)
print(gcd(N,M))
# print(lcm(N, M))