# import collections 
# def findItinerary(tickets):
#     graph_list = collections.defaultdict(list)
#     for a, b in sorted(tickets):
#         graph_list[a].append(b)
#     result = []
#     def dfs(val):
#         while graph_list[val]:
#             dfs(graph_list[val].pop(0))
#         result.append(val)
        
#         # print(type(graph_list[val]))

#     dfs('JFK')

#     return result[::-1]

# tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
# print(findItinerary(tickets))
import collections 
def findItinerary(tickets):
    graph_list = collections.defaultdict(list)
    for ticket in sorted(tickets):

        graph_list[ticket[0]].append(ticket[1])
    result = []
    print(graph_list)
    def dfs(val):
        while graph_list[val]:
            dfs(graph_list[val].pop(0))
        result.append(val)
    dfs('JFK')

    return result[::-1]

tickets =[["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
print(findItinerary(tickets))