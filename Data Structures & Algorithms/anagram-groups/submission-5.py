class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #dictionary keys must be hashable, and for an object to be hashable its value must not change in a way that changes its hash while it is being used as a key
        hash_anagram = {}
        for s in strs:
            count = [0] * 26
            for ch in s:
                count[ord(ch) - ord('a')] += 1
            if tuple(count) in hash_anagram:
                hash_anagram[tuple(count)].append(s)
            else:
                hash_anagram[tuple(count)] = [s]
        return list(hash_anagram.values())