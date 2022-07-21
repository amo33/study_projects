prices = [1,2]
val = min(prices)
max_val = [val]
# options = [i for i,v in enumerate(prices) if v == val]
# options.append(len(prices))
# print(options)
# for i in range(1,len(options)):
#     if options[i-1] != options[i]:
#         max_val.append(max(prices[options[i-1]:options[i]]))
# idx = max_val.index(max(max_val))
# print(max_val)

# print(max_val[idx] - val)
prices = [7,6,4,3,1]
temp = max(prices)
min_val = prices[0]
max_val = 0
option = [0]
for i, price in enumerate(prices):
    if min_val > price:
        option.append(max_val - min_val)
        min_val = price 
        max_val = 0
        continue 
    if max_val < price:
        max_val = price
    if i == len(prices) - 1:
        option.append(max_val-min_val)
print(option)
print(max(option))