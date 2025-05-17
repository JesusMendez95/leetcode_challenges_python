"""
14. Longest Common Prefix
Solved
Easy
Topics
Companies
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.
"""
# submission: https://leetcode.com/problems/longest-common-prefix/submissions/1635875369

import time
from statistics import mean, stdev
from typing import List, Tuple

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return "" 
        lcp = []
        for tuple_char in zip(*strs):
            if len(set(tuple_char)) == 1:
                lcp.append(tuple_char[0])
            else:
                break
        return "".join(lcp)

class Solution2:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        """
        Alternative solution using the first string as reference.
        Time Complexity: O(S) where S is the sum of all characters in all strings
        Space Complexity: O(1)
        """
        if not strs:
            return ""
        
        # Use the first string as reference
        first = strs[0]
        
        # Find the minimum length among all strings
        min_len = min(len(s) for s in strs)
        
        # Compare each character position
        for i in range(min_len):
            char = first[i]
            # Check if all other strings have the same character at this position
            if any(s[i] != char for s in strs[1:]):
                return first[:i]
        
        # If we get here, the entire first string (up to min_len) is the common prefix
        return first[:min_len]

class Solution3:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        """
        Alternative solution using binary search approach.
        Time Complexity: O(S * log M) where S is the sum of all characters and M is the length of the shortest string
        Space Complexity: O(1)
        """
        if not strs:
            return ""
            
        def is_common_prefix(length: int) -> bool:
            # Get the prefix of the first string
            prefix = strs[0][:length]
            # Check if all other strings start with this prefix
            return all(s.startswith(prefix) for s in strs[1:])
        
        # Find the minimum length among all strings
        min_len = min(len(s) for s in strs)
        
        # Binary search for the longest common prefix
        left, right = 0, min_len
        
        while left < right:
            mid = (left + right + 1) // 2
            if is_common_prefix(mid):
                left = mid
            else:
                right = mid - 1
                
        return strs[0][:left]

def measure_performance(solution, test_cases: List[Tuple[List[str], str]], iterations: int = 1000) -> Tuple[float, float]:
    """
    Measure the performance of a solution over multiple iterations.
    Returns (mean_time, std_dev) in microseconds.
    """
    times = []
    
    for _ in range(iterations):
        for input_strs, _ in test_cases:
            start_time = time.perf_counter()
            solution.longestCommonPrefix(input_strs)
            end_time = time.perf_counter()
            times.append((end_time - start_time) * 1_000_000)  # Convert to microseconds
    
    return mean(times), stdev(times)

def run_tests():
    solutions = [Solution(), Solution2(), Solution3()]
    solution_names = ["Zip-based Solution", "First String Reference Solution", "Binary Search Solution"]
    
    # Test cases
    test_cases = [
        # Basic cases
        (["flower", "flow", "flight"], "fl"),
        (["dog", "racecar", "car"], ""),
        
        # Edge cases
        ([], ""),  # Empty array
        ([""], ""),  # Single empty string
        (["a"], "a"),  # Single character
        (["", ""], ""),  # Multiple empty strings
        
        # Same strings
        (["hello", "hello", "hello"], "hello"),
        
        # Common prefix at different lengths
        (["interspecies", "interstellar", "interstate"], "inters"),
        (["prefix", "pre", "premature"], "pre"),
        
        # No common prefix
        (["abc", "def", "ghi"], ""),
        
        # Mixed lengths
        (["a", "ab", "abc"], "a"),
        (["ab", "a", "abc"], "a"),
        
        # Special cases
        (["aaa", "aa", "aaa"], "aa"),
        (["aa", "a"], "a"),
        
        # Long strings
        (["a" * 200, "a" * 200, "a" * 200], "a" * 200),
        
        # Different first characters
        (["flower", "blow", "clow"], ""),
        
        # Common prefix in middle
        (["flower", "flow", "flight", "fling"], "fl"),

        # Additional test cases
        # Single character variations
        (["a", "b", "c"], ""),
        (["a", "a", "a"], "a"),
        (["a", "aa", "aaa"], "a"),
        
        # Numbers and special characters (if allowed by constraints)
        (["123", "1234", "12345"], "123"),
        (["!@#", "!@#$", "!@#$%"], "!@#"),
        
        # Very short strings
        (["a", "b"], ""),
        (["ab", "ac"], "a"),
        (["ab", "ab"], "ab"),
        
        # Maximum array length (200 strings)
        (["test"] * 200, "test"),
        
        # Mixed case scenarios
        (["flower", "flow", "fl", "fling"], "fl"),
        (["flower", "flow", "fl", "fling", "flip"], "fl"),
        
        # Common prefix at start and end
        (["prefix", "pre", "premature", "prem"], "pre"),
        (["suffix", "suf", "suffer", "suf"], "suf"),
        
        # Alternating patterns
        (["abab", "ababab", "abababab"], "abab"),
        (["abcabc", "abc", "abcabcabc"], "abc"),
        
        # One character difference
        (["abcd", "abce", "abcf"], "abc"),
        (["abcd", "abce", "abcf", "abcg"], "abc"),
        
        # Common prefix with different lengths
        (["a", "aa", "aaa", "aaaa"], "a"),
        (["ab", "abc", "abcd", "abcde"], "ab"),
        
        # Stress test with maximum length strings
        (["a" * 200, "a" * 199 + "b", "a" * 198 + "bc"], "a" * 198),
        
        # Common prefix in all positions
        (["prefix", "pre", "premature", "prem", "pre"], "pre"),
        
        # No common prefix but similar patterns
        (["abc", "bcd", "cde"], ""),
        (["abc", "bcd", "cde", "def"], ""),
        
        # Common prefix with spaces
        (["hello world", "hello there", "hello you"], "hello "),
        
        # Common prefix with repeated characters
        (["aaa", "aaaa", "aaaaa"], "aaa"),
        (["aaa", "aaaa", "aaaaa", "aaaaaa"], "aaa"),
        
        # Common prefix with mixed patterns
        (["abc", "abcd", "abcde", "abcdef"], "abc"),
        (["xyz", "xyza", "xyzab", "xyzabc"], "xyz"),
    ]
    
    # First verify correctness
    print("Verifying correctness of all solutions...")
    for solution_idx, solution in enumerate(solutions, 1):
        print(f"\nTesting Solution {solution_idx} ({solution_names[solution_idx-1]}):")
        print("=" * 50)
        
        for i, (input_strs, expected) in enumerate(test_cases, 1):
            result = solution.longestCommonPrefix(input_strs)
            print(f"Test {i}:")
            print(f"Input: {input_strs}")
            print(f"Expected: '{expected}'")
            print(f"Got: '{result}'")
            print(f"Passed: {result == expected}")
            print("-" * 50)
    
    # Then measure performance
    print("\nMeasuring performance (1000 iterations per test case)...")
    print("=" * 50)
    
    for solution_idx, solution in enumerate(solutions, 1):
        mean_time, std_dev = measure_performance(solution, test_cases)
        print(f"\nSolution {solution_idx} ({solution_names[solution_idx-1]}):")
        print(f"Average time: {mean_time:.2f} ± {std_dev:.2f} microseconds")
        print(f"Average time per test case: {mean_time/len(test_cases):.2f} microseconds")

if __name__ == "__main__":
    run_tests()


