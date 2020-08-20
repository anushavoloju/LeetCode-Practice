import collections
class Solution:
    def findAndReplacePattern(self, words, pattern: str):
        result = []
        pattern_chars = collections.Counter(pattern)
        pattern_chars_values = list(pattern_chars.values())
        for word in words:
            word_chars = collections.Counter(word)
            word_chars_values = list(word_chars.values())
            if word_chars_values == pattern_chars_values:
                result.append(word)
            else:
                continue
        return result
    
    def findAndReplacePattern2(self, words, pattern: str):
        #result = []
        pattern_encode = self.encode_word(pattern)
        print(pattern_encode)

    def encode_word(self, word):
        res = []
        i = 1
        res.append(word[0])
        count = 1
        while i < len(word):
            if word[i-1] != word[i]:
                res.append(count)
                res.append(word[i])
                count = 1
            else:
                count = count + 1
            if i == len(word) - 1:
                res.append(count)
                i = i + 1
            else:
                i = i + 1
        return res

    def findAndReplacePattern3(self, words, pattern: str):
        result = []
        for word in words:
            res = self.match_pattern(word,pattern)
            if res:
                result.append(word)
        return result


    def match_pattern(self, word, pattern):
        wd = {}
        pd = {}
        for w,p in zip(word,pattern):
            if wd.get(w, -1) == -1:
                wd[w] = p
            if pd.get(p, -1) == -1:
                pd[p] = w
            if wd[w] != p or pd[p] != w:
                return False
        return True





        
s = Solution()
print(s.findAndReplacePattern3(["abc","deq","mee","aqq","dkd","ccc"], "abb"))
print(s.findAndReplacePattern3(["badc","abab","dddd","dede","yyxx"], "baba"))