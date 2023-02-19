# pattern 3 (Right Downward Triangle)
"""
* * * * *
* * * *
* * *
* *
*
"""
for i in range(5):
    for j in range(5-i):
        print("*",end=" ")
    print()