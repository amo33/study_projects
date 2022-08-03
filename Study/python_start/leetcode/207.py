import collections, itertools 
def canFinish( numCourses: int, prerequisites) -> bool:
    course_dict = collections.defaultdict(list)
    for courses in prerequisites:
        course_dict[courses[0]].append(courses[1])
    visited = set()
    def dfs(val):
        
        if val in visited:
            return False 
        
        visited.add(val)
        for node in course_dict[val]:
            if dfs(node) == False:
                return False 
        visited.remove(val)
        return True 
    print(list(course_dict))
    for value in list(course_dict.keys()):
        if dfs(value) == False:
            return False
    
    return True 

prerequisites = [[2,0],[2,1],[1,0]]
print(canFinish(2,prerequisites))