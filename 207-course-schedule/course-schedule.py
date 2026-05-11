class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj=defaultdict(list)
        for u, v in prerequisites:
            adj[u].append(v)
        
        vis=set()
        path_vis=set()

        def has_cycle(node):
            if node in vis:
                return
            
            vis.add(node)
            path_vis.add(node)

            for child in adj[node]:
                if child not in vis:
                    if has_cycle(child):
                        return True
                elif child in path_vis:
                    return True
            
            path_vis.remove(node)

            return False


        for it in range(numCourses):
            if it not in vis:
                if has_cycle(it):
                    return False
            

        return True