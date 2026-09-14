class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_s1 = {}
        count_s2 = {}
        s1_len = len(s1)
        s2_len = len(s2)

        if(s2_len < s1_len):
            return False
        
        for i in range(s1_len):
            count_s1[s1[i]] = count_s1.get(s1[i], 0) + 1
        
        for j in range(s1_len):
            count_s2[s2[j]] = count_s2.get(s2[j], 0) + 1
        
        if count_s1 == count_s2:
            return True
        
        l = 0
        for r in range(len(s1), len(s2)):
            count_s2[s2[l]] = count_s2.get(s2[l]) - 1
            count_s2[s2[r]] = count_s2.get(s2[r], 0) + 1
            if count_s2[s2[l]] == 0:
                del count_s2[s2[l]]
            l += 1
            print(count_s2)

            if count_s1 == count_s2:
                return True
        return False