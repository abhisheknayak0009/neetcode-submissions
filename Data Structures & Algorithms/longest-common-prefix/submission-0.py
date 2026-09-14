class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # take any word and check
        final_str = ""
        cur_str = strs[0]
        for i in range(len(cur_str)):
            for s in strs:
                if i == len(s) or s[i] != cur_str[i]:
                    return final_str
            final_str += cur_str[i]
        return final_str