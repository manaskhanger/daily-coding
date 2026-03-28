import os
from datetime import date
import random

today = str(date.today())

os.makedirs("problems", exist_ok=True)
os.makedirs("solutions", exist_ok=True)

# Count existing problems
existing = len(os.listdir("problems")) + 1

# Difficulty progression
if existing <= 10:
    difficulty = "Easy"
elif existing <= 30:
    difficulty = "Medium"
else:
    difficulty = "Hard"

# Problem bank
problems = {
    "Easy": [
        ("Two Sum", "Find two indices such that their sum equals the target."),
        ("Palindrome Check", "Check if a string is a palindrome."),
        ("Valid Parentheses", "Check if parentheses are valid."),
    ],
    "Medium": [
        ("Longest Substring Without Repeating Characters", "Find length of longest substring without repeating characters."),
        ("3Sum", "Find all unique triplets that sum to zero."),
        ("Search in Rotated Sorted Array", "Search target in rotated sorted array."),
    ],
    "Hard": [
        ("Median of Two Sorted Arrays", "Find median of two sorted arrays."),
        ("Merge k Sorted Lists", "Merge k sorted linked lists."),
        ("Trapping Rain Water", "Calculate trapped rain water."),
    ]
}

title, desc = random.choice(problems[difficulty])

# Save problem
with open(f"problems/{today}.md", "w") as f:
    f.write(f"# {title} ({difficulty})\n\n{desc}\n")

# Solutions
solutions = {
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
            l = max(l, seen[s[r]] + 1)
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

solution_code = solutions.get(title, "print('Solution coming soon')")

with open(f"solutions/{today}.py", "w") as f:
    f.write(f"# {title} ({difficulty})\n\n{solution_code}")

# Update README (clean + human)
total = len(os.listdir("problems"))

readme = f"""# 📅 Daily DSA Grind

Consistent daily practice of data structures and algorithms.

## 📊 Progress
- Total Problems Solved: {total}
- Current Focus: {difficulty}

## 📂 Repository Structure
- problems/ → problem statements
- solutions/ → implementations

## 🎯 Objective
Building strong problem-solving skills through daily practice.
"""

with open("README.md", "w") as f:
    f.write(readme)
