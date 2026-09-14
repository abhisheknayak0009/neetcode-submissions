class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final_anagram = []
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