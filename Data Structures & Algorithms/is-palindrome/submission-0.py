class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s : "noon"; len(s) = 4 => 0[n] 1[o] 2[o] 3[n]
        left = 0
        right = len(s) - 1

        s = s.lower()
        while left < right:
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True