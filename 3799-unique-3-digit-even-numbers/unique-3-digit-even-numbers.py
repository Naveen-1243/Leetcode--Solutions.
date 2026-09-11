class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        n = len(digits)
        nums = set()

        for i in range(n):
            if digits[i] == 0:  # No leading zero
                continue

            for j in range(n):
                if j == i:
                    continue

                for k in range(n):
                    if k == i or k == j:
                        continue

                    if digits[k] % 2 != 0:  # Last digit must be even
                        continue

                    num = digits[i] * 100 + digits[j] * 10 + digits[k]
                    nums.add(num)

        return len(nums)