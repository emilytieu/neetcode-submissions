class Solution:
    def numDecodings(self, s: str) -> int:
        var, var1 = 0, 1
        var2 = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == "0":
                var = 0
            else:
                var = var1
            if i+1 < len(s) and (s[i] == "1" or (s[i] == "2" and int(s[i+1]) < 7)):
                var += var2
            var, var1, var2 = 0, var, var1
        return var1