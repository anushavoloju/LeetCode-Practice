class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):

        def find_combinations(s, start):
            if len(s) == self.comb_length:
                self.result.append(s)
            else:
                for i in range(start, len(self.chars)):
                    find_combinations(s + self.chars[i], i + 1)

        self.chars = characters
        self.comb_length = combinationLength
        self.index = 0
        self.result = []
        find_combinations('', 0)
        

    def next(self) -> str:
        res = self.result[self.index]
        self.index += 1
        return res
        

    def hasNext(self) -> bool:
        if self.index < len(self.result):
            return True
        return False
        


# Your CombinationIterator object will be instantiated and called as such:
obj = CombinationIterator('abc', 2)
param_1 = obj.next()
print(param_1)
param_2 = obj.hasNext()
print(param_2)