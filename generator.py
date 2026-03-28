from datetime import date
import os
import random

today = str(date.today())

os.makedirs("problems", exist_ok=True)
os.makedirs("solutions", exist_ok=True)

problems = [
    ("Two Sum", "Find two numbers that add up to target."),
    ("Palindrome", "Check if string is palindrome."),
    ("Fibonacci", "Return nth Fibonacci number."),
]

p = random.choice(problems)

with open(f"problems/{today}.md", "w") as f:
    f.write(f"# {p[0]}\n\n{p[1]}")

with open(f"solutions/{today}.py", "w") as f:
    f.write(f"# Solution for {p[0]}\nprint('Solved')")
