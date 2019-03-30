
# Assignment 07, Task 01
# Name: Vikrom Narula
# Collaborations:
# Time Spent: 0.75 hrs


def all_perm(n):
    if n < 1:
        return None
    if n == 1:
        return {(1,)}
    else:
        b = all_perm(n-1)
        a = []
        h = []
        for m in b:  # copy to a new list
            for l in m:
                h.append(l)
            a.append(h)
            h = []
        lst = []
        for i in range(len(b)):  # create list thats the set
            for j in range(n):
                a[i].insert(j, n)
                lst.append(a[i])
                a = []
                for m in b:  # create a
                    for l in m:
                        h.append(l)
                    a.append(h)
                    h = []

        return set(tuple(mn) for mn in lst)


print(all_perm(3))

# Assignment 07, Task 01
# Name: Vikrom Narula
# Collaborations:
# Time Spent: 0.75 hrs


def all_perm(n):
    if n < 1:
        return None
    if n == 1:
        return {(1,)}
    else:
        b = all_perm(n-1)
        a = []
        h = []
        for m in b:  # copy to a new list
            for l in m:
                h.append(l)
            a.append(h)
            h = []
        lst = []
        for i in range(len(b)):  # create list thats the set
            for j in range(n):
                a[i].insert(j, n)
                lst.append(a[i])
                a = []
                for m in b:  # create a
                    for l in m:
                        h.append(l)
                    a.append(h)
                    h = []

        return set(tuple(mn) for mn in lst)


print(all_perm(3))
