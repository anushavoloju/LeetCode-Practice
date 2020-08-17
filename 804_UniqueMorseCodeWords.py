class Solution:
    def uniqueMorseRepresentations(self, words) -> int:
        alpha_morse_map = {
            'a': ".-", 'b': "-...", 'c': "-.-.", 'd': "-..", 'e': ".", 'f': "..-.", 'g': "--.", 'h': "....",
            'i': "..", 'j': ".---", 'k': "-.-", 'l': ".-..", 'm': "--", 'n': "-.", 'o': "---", 'p': ".--.",
            'q': "--.-",'r': ".-.", 's': "...", 't': "-", 'u': "..-", 'v': "...-",'w': ".--", 'x': "-..-", 'y': "-.--",
            'z': "--.."}
        word_morse_map = {}
        for word in words:
            transform = ''
            for c in word:
                transform = transform + alpha_morse_map.get(c)
            word_morse_map[word] = transform
        count = len(set(word_morse_map.values()))
        return count

        
s = Solution()
print(s.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))