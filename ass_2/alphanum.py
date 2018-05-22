# Assignment 02, Task 02
# Name: Vikrom Narula
# Collaborators: Aj. Sunsern, Sukhcott Pruthi, Yves Ramon Hager
# TimeSpent: 1:30 hrs

a='2'
b='3'
c='4'
d='5'
e='6'
f='7'
g='8'
h='9'
def sev(word):
    if word[6]in'ABCabc':
        return a
    if word[6]in'DEFdef':
        return b
    if word[6]in 'GHIghi':
        return c
    if word[6]in 'JKLjkl':
        return d
    if word[6]in 'MNOmno':
        return e
    if word[6]in 'PQRSpqrs':
        return f
    if word[6]in 'TUVtuv':
        return g
    if word[6]in 'WXYZwxyz':
        return h
    
def six(word):
    if word[5]in'ABCabc':
        return a
    if word[5]in'DEFdef':
        return b
    if word[5]in 'GHIghi':
        return c
    if word[5]in 'JKLjkl':
        return d
    if word[5]in 'MNOmno':
        return e
    if word[5]in 'PQRSpqrs':
        return f
    if word[5]in 'TUVtuv':
        return g
    if word[5]in 'WXYZwxyz':
        return h
def five(word):
    if word[4]in'ABCabc':
        return a
    if word[4]in'DEFdef':
        return b
    if word[4]in 'GHIghi':
        return c
    if word[4]in 'JKLjkl':
        return d
    if word[4]in 'MNOmno':
        return e
    if word[4]in 'PQRSpqrs':
        return f
    if word[4]in 'TUVtuv':
        return g
    if word[4]in 'WXYZwxyz':
        return h

def four(word):
    if word[3]in'ABCabc':
        return a
    if word[3]in'DEFdef':
        return b
    if word[3]in 'GHIghi':
        return c
    if word[3]in 'JKLjkl':
        return d
    if word[3]in 'MNOmno':
        return e
    if word[3]in 'PQRSpqrs':
        return f
    if word[3]in 'TUVtuv':
        return g
    if word[3]in 'WXYZwxyz':
        return h
def thir(word):
    if word[2]in'ABCabc':
        return a
    if word[2]in'DEFdef':
        return b
    if word[2]in 'GHIghi':
        return c
    if word[2]in 'JKLjkl':
        return d
    if word[2]in 'MNOmno':
        return e
    if word[2]in 'PQRSpqrs':
        return f
    if word[2]in 'TUVtuv':
        return g
    if word[2]in 'WXYZwxyz':
        return h
def se(word):
    if word[1]in'ABCabc':
        return a
    if word[1]in'DEFdef':
        return b
    if word[1]in 'GHIghi':
        return c
    if word[1]in 'JKLjkl':
        return d
    if word[1]in 'MNOmno':
        return e
    if word[1]in 'PQRSpqrs':
        return f
    if word[1]in 'TUVtuv':
        return g
    if word[1]in 'WXYZwxyz':
        return h
def fi(word):
    if word[0]in'ABCabc':
        return a
    if word[0]in'DEFdef':
        return b
    if word[0]in 'GHIghi':
        return c
    if word[0]in 'JKLjkl':
        return d
    if word[0]in 'MNOmno':
        return e
    if word[0]in 'PQRSpqrs':
        return f
    if word[0]in 'TUVtuv':
        return g
    if word[0]in 'WXYZwxyz':
        return h




def phoneWord2Num(word):
    """
    >>> phoneWord2Num("PrOGrAM")
    7764726

    >>> phoneWord2Num("FLOWERS")
    3569377

    >>> phoneWord2Num("Battery")
    2288379
    """
    return int(fi(word)+se(word)+thir(word)+four(word)+five(word)+six(word)+sev(word))
          
        
      
    
    
    
     
    


###########################################################################
# Please don't mind me living down here. I provide some initial testing for
# your code. Run me (e.g., using the run button in Spyder).
###########################################################################
# Simple Tests
###########################################################################
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
###########################################################################
