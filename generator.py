import os
from datetime import date
import random

today = str(date.today())

os.makedirs("problems", exist_ok=True)
os.makedirs("solutions", exist_ok=True)

# Difficulty progression based on day number
day_number = len(os.listdir("problems")) + 1

if day_number <= 10:
    difficulty = "Easy"
elif day_number <= 30:
    difficulty = "Medium"
else:
    difficulty = "Hard"

# Real DSA-style problems
problem_bank = {
    "Easy": [
        ("Two Sum", "Given an array nums and target, return indices of two numbers such that they add up to target."),
        ("Palindrome Check", "Check if a string is a palindrome."),
        ("Valid Parentheses", "Determine if input string has valid parentheses."),
    ],
    "Medium": [
        ("Longest Substring Without Repeating Characters", "Find length of longest substring without repeating characters."),
        ("3Sum", "Find all unique triplets that sum to zero."),
        ("Search in Rotated Sorted Array", "Search target in rotated sorted array."),
    ],
    "Hard": [
        ("Median of Two Sorted Arrays", "Find median of two sorted arrays in O(log n)."),
        ("Merge k Sorted Lists", "Merge k sorted linked lists."),
        ("Trapping Rain Water", "Compute trapped rainwater."),
    ]
}

problem = random.choice(problem_bank[difficulty])
title, desc = problem

# Save problem
with open(f"problems/{today}.md", "w") as f:
    f.write(f"# {title} ({difficulty})\n\n{desc}\n")

# Optimal solutions (basic but real)
solutions_map = {
    "Two Sum": """def two_sum(nums, target):
    d = {}
    for i, num in enumerate(nums):
        if target - num in d:
            return [d[target - num], i]
        d[num] = i""",

    "Palindrome Check": """def is_palindrome(s):
    return s == s[::-1]""",

    "Valid Parentheses": """def is_valid(s):
    stack = []
    m = {')':'(', '}':'{', ']':'['}
    for c in s:
        if c in m.values():
            stack.append(c)
        elif c in m:
            if not stack or stack.pop() != m[c]:
                return False
    return not stack""",

    "Longest Substring Without Repeating Characters": """def longest_substring(s):
    seen = {}
    l = res = 0
    for r in range(len(s)):
        if s[r] in seen:
            l = max(seen[s[r]] + 1, l)
        seen[s[r]] = r
        res = max(res, r - l + 1)
    return res""",

    "3Sum": """def three_sum(nums):
    nums.sort()
    res = []
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        l, r = i+1, len(nums)-1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s == 0:
                res.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
            elif s < 0:
                l += 1
            else:
                r -= 1
    return res""",

    "Median of Two Sorted Arrays": """def find_median(a, b):
    nums = sorted(a + b)
    n = len(nums)
    if n % 2:
        return nums[n//2]
    return (nums[n//2 - 1] + nums[n//2]) / 2"""
}

solution_code = solutions_map.get(title, "print('Solution coming soon')")

with open(f"solutions/{today}.py", "w") as f:
    f.write(f"# {title} ({difficulty})\n\n{solution_code}")

# Update README stats
total = len(os.listdir("problems"))

readme_content = f"""# 📅 Daily DSA Grind

🔥 Auto-generated coding problems + solutions

## 📊 Stats
- Total Problems Solved: {total}
- Current Difficulty: {difficulty}

## 📂 Structure
- problems/ → problem statements
- solutions/ → optimal code

## 🚀 Goal
Consistent daily DSA practice for placements
"""

with open("README.md", "w") as f:
    f.write(readme_content)
