class Solution:
    def numIslands(self, graph: List[List[str]]) -> int:
        
        visited=set((0,0))
        r=len(graph)
        c=len(graph[0])

        def dfs(i,j):    
            if i<0 or i>=r or j<0 or  j>=c or (i,j) in visited or graph[i][j]!='1':
                return

            visited.add((i,j))
            graph[i][j]='#'
            dfs(i+1,j)
            dfs(i,j+1)
            dfs(i-1,j)
            dfs(i,j-1)
        
        count=0
        for i in range(r):
            for j in range(c):
                if (i,j) not in visited and graph[i][j]=='1':
                    count+=1
                    dfs(i,j)
        
        return count



