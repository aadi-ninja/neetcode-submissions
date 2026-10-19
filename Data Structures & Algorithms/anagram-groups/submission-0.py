class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = {}
        for i in strs :
            s="".join(sorted(i))
            if s not in store :
                store[s]=[i]
            else:
                store[s].append(i)
        return list(store.values())

