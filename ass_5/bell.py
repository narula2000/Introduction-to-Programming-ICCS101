# Assignment 05, Task 02
# Name: Vikrom Narula
# Time Spent: 1 hrs

def loveTri(n):
    old = [1]
    buffer = []
    answer = [old]
    for i in range(n - 1):
        buffer = [old[-1]]
        for j in range(len(old)):
            buffer.append(old[j] + buffer[j])
        answer.append(buffer)
        old = buffer
    return answer
