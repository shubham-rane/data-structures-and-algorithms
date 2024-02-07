class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq = {}
        for char in s1:
            if char in s1_freq:
                s1_freq[char] += 1
            else:
                s1_freq[char] = 1
        
        s2_freq = {}

        for char in s2[0: len(s1)]:
            if char in s2_freq:
                s2_freq[char] += 1
            else:
                s2_freq[char] = 1
        if s1_freq == s2_freq:
                return True
        
        n = len(s1)
        for i in range(n, len(s2)):
            char_to_remove = s2[i - n]
            char_to_add = s2[i]
            
            # Update frequency for the character going out of the window
            s2_freq[char_to_remove] -= 1
            if s2_freq[char_to_remove] == 0:
                del s2_freq[char_to_remove]
            
            # Update frequency for the character entering the window
            #s2_freq[char_to_add] = s2_freq.get(char_to_add, 0) + 1
            if char_to_add in s2_freq:
                s2_freq[char_to_add] += 1
            else:
                s2_freq[char_to_add] = 1
            
            if s1_freq == s2_freq:
                return True
        return False
            


        
        