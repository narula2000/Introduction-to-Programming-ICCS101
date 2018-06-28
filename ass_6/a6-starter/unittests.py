import diet
import eto
import findme
import passwd
import t2048


assert(eto.eto([1,2,3,4,5,6])==[2, 4, 6, 5, 3, 1])
assert(eto.eto([1,2,36,9,2,43,17])==[2, 36, 2, 17, 43, 9, 1])
assert(eto.eto([1,29,2,43,17])==[2, 17, 43, 29, 1])
assert(eto.eto([1,2,3896,9,2,3,17])==[2, 3896, 2, 17, 3, 9, 1])
assert(eto.eto([2,3,4,2,2,22,2,2,2])==[2, 4, 2, 2, 22, 2, 2, 2, 3])

assert(passwd.passwordOK('ABd1234@1')==True)
assert(passwd.passwordOK('f#9')==False)
assert(passwd.passwordOK('Abbc1$f')==False)
assert(passwd.passwordOK('bcb1$f%')==False)
assert(passwd.passwordOK('Abcb1$f%')==True)

assert(findme.findMe(9, [1,2,9,5,3,9])==2)
assert(findme.findMe(7, [1,2,3,4,9])==None)
assert(findme.findMe('nag',[1,2,3,'nag',4])==3)
assert(findme.findMe(5, [5,5,5,55,5,5])==0)
assert(findme.findMe('ng', ['ng','gn','ng'])==0)

