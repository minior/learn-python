# goal: add 1+2+3+...+100 with both for & while
total = 0
for i in range (101):
    total = total + i
print(total)

total = 0
i = 1
while i < 101:
    total = total + i
    i = i+1
print(total)
import pyperclip