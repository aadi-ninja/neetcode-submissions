class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        ans=[]
        for i in nums:
            if i in d:
                d[i] +=1
            else:
                d[i]=1
        def get_count(pair):
            return pair[1]
        for i,count in sorted(d.items(),key=get_count,reverse= True):
            ans.append(i)
            if len(ans)==k:
                break
        return ans

