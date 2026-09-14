class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)

        for s in strs:
            charArray = [0] * 26
            for i in range(len(s)):
                charArray[ord(s[i]) - ord('a')] += 1
            ans[tuple(charArray)].append(s)
        return ans.values()