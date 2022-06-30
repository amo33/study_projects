'''
# 해당 방식은 quick sort 방식으로 n^2의 시간초과로 runtimeerror 발생 
cnt =int(input())
arr = []
while cnt >0:
    arr.append(int(input()))
    cnt -=1
def quicksort(arr, start, end):
    # start = index 
    if start >=end:
        return 

    val = arr[start]
    i = start+ 1
    j = end
    while i<=j: 
        print(i, j)
        while i<=j and arr[i] <= val: # 왜  arr[i] <= val and i<=j 하면 오류 나지?
            i+=1
        while j>=i and arr[j] >= val:
            j-=1 
        print(i, j)
        if i > j:
            print(arr[start], arr[j])
            temp = arr[j]
            arr[j] = arr[start]
            arr[start] = temp 
            
        else :
            temp = arr[i]
            arr[i] = arr[j]
            arr[j]= temp 
        print(arr)
    quicksort(arr, start, j-1)

    quicksort(arr, j+1, end)
quicksort(arr, 0, len(arr)-1)
for i in range(len(arr)):
    print(arr[i])
'''

cnt =int(input())
arr = []
new_arr = [0 for _ in range(cnt)]
while cnt >0:
    arr.append(int(input()))
    cnt -=1

def mergesort(start, middle, end):
    i = start 
    j = middle + 1

    k = start
    while(i <= middle and j <= end):

        if arr[i] < arr[j]:
            new_arr[k]= arr[i]
            i+=1         
            k+=1
        else:
            new_arr[k] = arr[j]
            j+=1 
            k+=1
    if i>middle and j <=end:
        while j<=end:
            new_arr[k] = arr[j]
            j+=1 
            k+=1
    elif i<=middle and j> end:
        while i<=middle:
            new_arr[k] = arr[i]
            i+=1
            k+=1
    for k in range(start,end+1): # 기존 배열에 업데이트 해줘야하며 -> 왜냐하면 이전 정렬 업데이트를 반영한 다음 정렬을 진행해야하므로!
        arr[k] = new_arr[k] 
    #print(new_arr)

#val = int(math.log2(cnt) )
def divide(left, right):
    if left >= right:
        return
    start = left 
    middle = int((left+right)/2)
    end = right  
    divide(start, middle)
    divide(middle+1, end)
    mergesort(start, middle, end)
divide(0, len(arr)-1)
#mergesort(0, 2, 4)
for i in range(len(arr)):
    print(arr[i]) #  arr 를 출력해줘야한다. 그 이유는 내가 left >=right 일때(원소 1개만 들어오는 상황은)는 아무 동작 안하게 해놓았다. (divide 함수 참고)
print("============")
for i in range(len(new_arr)):
    print(new_arr[i]) # 이처럼 new_Arr를 출력하면 원하는 결과가 나오지 않는 경우도 존재한다.
