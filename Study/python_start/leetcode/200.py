import collections 
def numIslands(grid) -> int:
    result = 0
    def dfs(row,col, ground_map):
        d_x = [-1,1,0,0]
        d_y = [0,0,-1,1]
        for i in range(4):
            r_near = row + d_x[i]
            c_near = col + d_y[i]
            if 0<=r_near<len(ground_map) and 0<=c_near<len(ground_map[0]):
                if ground_map[r_near][c_near] =="1":
                    ground_map[r_near][c_near] = 0
                    dfs(r_near,c_near,ground_map)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] =="1":
                dfs(i,j,grid)
                result +=1 
    return result