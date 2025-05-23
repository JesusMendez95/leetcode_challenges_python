"""
2239. Find Closest Number to Zero
Easy
Topics
Companies
Hint
Given an integer array nums of size n, return the number with the value closest to 0 in nums.
 If there are multiple answers, return the number with the largest value.

Example 1:

Input: nums = [-4,-2,1,4,8]
Output: 1
Explanation:
The distance from -4 to 0 is |-4| = 4.
The distance from -2 to 0 is |-2| = 2.
The distance from 1 to 0 is |1| = 1.
The distance from 4 to 0 is |4| = 4.
The distance from 8 to 0 is |8| = 8.
Thus, the closest number to 0 in the array is 1.
Example 2:

Input: nums = [2,-1,1]
Output: 1
Explanation: 1 and -1 are both the closest numbers to 0, so 1 being larger is returned.

Constraints:

1 <= n <= 1000
-105 <= nums[i] <= 105
Accepted
142.3K
Submissions
304.3K
Acceptance Rate
46.8%
"""

# submittion: https://leetcode.com/problems/find-closest-number-to-zero/solutions/6341832/python-intuitive-solution-by-dvlsfdxunt-qlh8


class Solution:
    def findClosestNumber(self, nums: list[int]) -> int:
        closest_to_zero = nums[0]
        for num in nums[1:]:
            if num == 0:
                closest_to_zero = num
                break
            elif abs(num) < abs(closest_to_zero):
                closest_to_zero = num
                next
            elif abs(num) == abs(closest_to_zero):
                closest_to_zero = max(num, closest_to_zero)
        return closest_to_zero


solution = Solution()
print(solution.findClosestNumber(nums=[1, 2, 3, 4, -2, -1, 0]))
