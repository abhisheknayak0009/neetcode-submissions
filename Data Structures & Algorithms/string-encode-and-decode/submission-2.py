class Solution:
    
    def encode(self, strs):
        encoded_word = ''
        for word in strs:
            encoded_word += str(len(word)) + '#' + word
        return encoded_word

    def decode(self, s):
        i = 0
        decode_array = []
        while (i < len(s)):
            
            j = i
            while s[j] != '#':
                j += 1
            
            string_length = int(s[i:j])
            
            i = j + 1
            j = i + string_length

            decode_array.append(s[i:j])
            i = j

        return decode_array