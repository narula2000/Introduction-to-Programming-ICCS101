# Assignment 06, Task 01
# Name:Vikrom Narula
# Time: 5 min 

def passwordOK(p_str):
    lal='abcdefghijklmnopqrstuvwxzy'
    ual=lal.upper()
    num='0123456789'
    count=0
    for let in range(len(p_str)-1):
        if p_str[let]==p_str[let+1]:
            return False
    if 6<=len(p_str)<=12:
        for l in p_str:
            if l in lal:
                count+=1
            if l in ual:
                count+=1
            if l in num:
                count+=1
            if l in '$#@':
                count+=1
        if count>=4:
            return True
        else:
            return False
    else:
        return False

assert(passwordOK('ABd1234@1')==True)
assert(passwordOK('f#9')==False)
assert(passwordOK('Abbc1$f')==False)
assert(passwordOK('Abcb1$f')==True)
