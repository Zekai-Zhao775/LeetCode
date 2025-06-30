import os

count = -1
for item in os.listdir():
    if os.path.isfile(item):
        count += 1

print(f"I have solved: {count} LeetCode!")