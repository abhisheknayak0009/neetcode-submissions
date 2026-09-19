class Solution:

    def encode(self, strs: List[str]) -> str:
        final_str = ""
        for s in strs:
            final_str += str(len(s)) + "#" + s
        return final_str
    def decode(self, s: str) -> List[str]:
        return_list = []
        i = 0
        while i < len(s):
            current_num = ""
            while s[i] != '#':
                current_num += s[i]
                i += 1
            digit = int(current_num)
            i += 1
            return_list.append(s[i: i + digit])
            i += digit
        return return_list