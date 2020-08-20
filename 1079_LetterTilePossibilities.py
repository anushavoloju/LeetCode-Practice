class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        self.paths = set()
        self.traverse('',tiles)
        return len(self.paths)

    def traverse(self, path, t):
        if path:
            self.paths.add(path)
        for i in range(len(t)):
            self.traverse(path + t[i], t[:i] + t[i+1:])


        
s = Solution()
print(s.numTilePossibilities("AAB"))