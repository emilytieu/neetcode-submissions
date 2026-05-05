class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for str in strs: # O(m)
            counts = [0] * 26
            for s in str:
                counts[ord(s) - ord('a')] += 1
            result[tuple(counts)].append(str)
        
        return list(result.values())