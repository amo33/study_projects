def find_closest_k_points(points, k):
    if not points:
        raise ValueError("No points are found!")
    if not k>0:
        raise ValueError("k must be larger than 0")

    points = sorted(points, key=lambda x: (abs(x[0]), abs(x[1])))
    return points[:k]
lst = [[-1,1],[1,2],[2,3],[3,3],[4,5],[1,0]]
print(find_closest_k_points(lst, 3))
# sort 들 다 공부하고 다시 풀기. 
# 1순위 sort, 
# 2순위 dp, 
# 3순위 그래프 
# 4순위 브루트포스 공부하기라고 생각합니다.