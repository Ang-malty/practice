class Solution:
    def longest_common_prefix(self, strs) -> str:
        self.strs = strs
        return self.solve()

    def solve(self):
        common_prefix = strs[0]
        for string in self.strs:
            common_prefix = self.resize(common_prefix, string)
            for index, letter in enumerate(string):
                if len(common_prefix) == index or letter != common_prefix[index]:
                    common_prefix = common_prefix[:index]
                    break
        return common_prefix

    def resize(self, common_prefix, string):
        if len(common_prefix) > len(string):
            common_prefix = common_prefix[:len(string)]
        return common_prefix



strs = ["ab", "a"]
print(Solution().longest_common_prefix(strs))
