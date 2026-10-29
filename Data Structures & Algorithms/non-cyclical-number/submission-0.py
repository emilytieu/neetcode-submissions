class Solution:
    def isHappy(self, n: int) -> bool:
        def square(n):
            res = 0
            while n:
                digit = n % 10
                res += digit ** 2
                n //= 10
            return res
        
        slow, fast = n, square(n)
        while slow != fast:
            if fast == 1: return True
            slow = square(slow)
            fast = square(square(fast))
        
        return slow == 1