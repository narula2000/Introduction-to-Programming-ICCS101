# Assignment 05, Task 04
# Name: Vikrom Narula
# Time Spent: 0.5 hrs


def keepTabs(actions):
    table = dict()
    answer = dict()
    for names in actions:
        if '+' in names:
            name = names.split('++')[0]
            if name in table:
                table[name] += 1
            else:
                table[name] = 1
        if '--' in names:
            name = names.split('--')[0]
            if name in table:
                table[name] -= 1
            else:
                table[name] = -1
        if '->' in names:
            giver, taker = names.split('->')
            if giver in table and taker in table:
                table[taker] += table[giver]
                table[giver] = 0
            elif giver in table and taker not in table:
                table[taker] = table[giver]
                table[giver] = 0

    for key in table:
        if table[key] != 0:
            answer[key] = table[key]

    return answer
