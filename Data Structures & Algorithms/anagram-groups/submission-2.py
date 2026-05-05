class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) # map charCount to list of anagrams
            # defaultdict takes care of key errors when appending to non-existent key
            # list useful for grouping

        for s in strs: # O(m)
            count = [0] * 26 # a...z -> [0, 0, ..., 0]. O(26)
            for c in s: # O(n). Updates counts of each c in s. 
                count[ord(c) - ord('a')] += 1 # ASCII values. Add 1 to count of char c. 
                    # a = 97 -> 0, 97 - 97
                    # z = 122 -> 25, 122 - 97
            result[tuple(count)].append(s) # add s to sublist of result with same counts

        return list(result.values()) # returns list of values

                