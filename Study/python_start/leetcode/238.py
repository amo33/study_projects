left = [1]
right = [1]
outputs = [-1,1,0,-3,3]
for i in range(len(outputs)-1):
    left.append(left[i]*outputs[i])
    right.append(right[i]*outputs[len(outputs)-1-i])

output_result = []
for val in zip(left,right[::-1]):
    output_result.append(val[0]*val[1])
print(output_result)