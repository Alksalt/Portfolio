class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        return [1] + digits

i = [9, 9, 9, 9, 9, 9]

o = 15 % 10
s = Solution()
print(s.plusOne(i))