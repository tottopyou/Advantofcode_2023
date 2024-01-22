from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keys = {'1': '0', '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        res = []
        for i, num in enumerate(digits):
            if i < len(digits) - 1:  # Check if not the last digit
                for val in keys[num]:
                    for next_val in keys[digits[i+1]]:
                        res.append(val + next_val)
            elif len(digits) == 1:
                for val in keys[num]:
                    res.append(val)
        return res

solution = Solution()
result = solution.letterCombinations("23")
print(result)
