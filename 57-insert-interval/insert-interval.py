class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
#Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
        
        result=[]
        n=len(intervals)
        i=0
        #left side
        while i<n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i+=1
        
        while i<n and intervals[i][0] <= newInterval[1]:
            #merge it
            newInterval[0]=min(newInterval[0],intervals[i][0])
            newInterval[1]=max(newInterval[1],intervals[i][1])
            i+=1
        result.append(newInterval)

        #right side
        while i<n:
            result.append(intervals[i])
            i+=1
        
        return result

        