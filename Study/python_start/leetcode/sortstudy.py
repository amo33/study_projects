def sortList(head):
    def bubblesort(input_list):
        for i in range(len(input_list)):
            for j in range(len(input_list)- i-1):
                if input_list[j] > input_list[j+1]:
                    input_list[j], input_list[j+1] = input_list[j+1], input_list[j]
                print(input_list)
        return input_list 
    def quicksort(input_list, start,end):
        def partition(low,high):
            pivot = input_list[high]
            left = low
            for right in range(low, high):
                if input_list[right] < pivot:
                    input_list[right] , input_list[left] = input_list[left], input_list[right]
                    left +=1 
            
            input_list[high] , input_list[left] = input_list[left], input_list[high]
            return left 
        if start < end:
            pivot = partition(start, end)
            quicksort(input_list, start , pivot-1)
            quicksort(input_list, pivot+1, end)
    
    def mergesort(input_list):
        if len(input_list) < 2:
            return input_list
        
        mid = len(input_list) // 2
        left = mergesort(input_list[:mid])
        right = mergesort(input_list[mid:])
        temp = []
        print(left,right)
        while left and right:
            print(left,right)
            if left[0] < right[0]:
                temp.append(left.pop(0))
            else:
                temp.append(right.pop(0))
        while left:
            temp.append(left.pop(0))
        while right:
            temp.append(right.pop(0))
        print(temp)
        return temp

    return bubblesort(head)

lst = [4,2,3,1,5,7]
print(sortList(lst))