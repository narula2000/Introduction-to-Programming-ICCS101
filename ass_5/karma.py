# Assignment 05, Task 04
# Name: Vikrom Narula
# Time Spent: 0.5 hrs


def keepTabs(actions):
    table = dict()
    r_table = dict()
    for names in actions:
        if '+' in names:
            a, v = names.split('++')
            if a in table:
                table[a] += 1
            else:
                table[a] = 1
        if '--' in names:
            a, v = names.split('--')
            if a in table:
                table[a] -= 1
            else:
                table[a] = -1
        if '->' in names:
            a, v = names.split('->')
            if a in table and v in table:
                table[v] += table[a]
                table[a] = 0
            elif a in table and v not in table:
                table[v] = table[a]
                table[a] = 0
    for key in table:
        if table[key] != 0:
            r_table[key] = table[key]

    return r_table
