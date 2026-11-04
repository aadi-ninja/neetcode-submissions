class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1={}
        for i in s1:
            if i in freq1:
                freq1[i]+=1
            else:
                freq1[i]=1
        maxwin=len(s1)
        freq2={}
        l=0
        for r in range(len(s2)):
            freq2[s2[r]]=1+freq2.get(s2[r],0)
            if (r-l+1)>maxwin:
                freq2[s2[l]]-=1
                if freq2[s2[l]] == 0:
                    del freq2[s2[l]]
                l+=1
            if freq1 == freq2:
                return True
        return False

