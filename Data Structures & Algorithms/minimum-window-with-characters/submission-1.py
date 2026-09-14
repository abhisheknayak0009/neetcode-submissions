class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        final_str = ""
        if(len(s) < len(t)):
            return final_str

        count_s, count_t = {}, {}

        for i in range(len(t)):
            count_t[t[i]] = count_t.get(t[i], 0) + 1
        
        have, need = 0, len(count_t)
        
        len_str = float("inf")
        l = 0

        for r in range(len(s)):
            count_s[s[r]] = count_s.get(s[r], 0) + 1
            
            if s[r] in count_t and count_s[s[r]] == count_t[s[r]]:
                have += 1
            
            while have == need:
                curr_str = r - l + 1
                if(curr_str < len_str):
                    final_str = s[l:r + 1]

                count_s[s[l]] = count_s.get(s[l], 0) - 1
                if s[l] in count_t and count_s[s[l]] < count_t[s[l]]:
                    have -= 1
                
                l += 1
        
        return final_str