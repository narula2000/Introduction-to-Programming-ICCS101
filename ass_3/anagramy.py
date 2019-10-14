def Anagramy(w1, w2):
    if len(w1) != len(w2):
        return False
    c = 0
    for w in w1:
        for j in w2:
            if j == w:
                c += 1
                break
    if c == len(w1)
    return True


print(Anagramy("agree", "eager"), Anagramy("angel", "glean"))
