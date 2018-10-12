import reverse
import altsum
import aloud
import hidden
import jogging
import cipher
import pme

assert(reverse.rev_str("diordna")=='android')
assert(reverse.rev_str("samsung")=='gnusmas')
assert(reverse.rev_str("enohpi")=='iphone')
assert(reverse.rev_str("microsoftwindows")=='swodniwtfosorcim')
assert(reverse.rev_str("ecneicsretupmocforolhcab")=='bachlorofcomputerscience')
assert(altsum.altSum([5,12,24,30])== 23)
assert(altsum.altSum([25,50,75,100,575])== -475)
assert(altsum.altSum([2,6,18,24,60,7])== -39)
assert(altsum.altSum([7,12,5])== 14)
assert(altsum.altSum([5,30])== 35)
assert(aloud.readAloud([])==[])
assert(aloud.readAloud([5,5,5])==[3,5])
#assert(aloud.readAloud([1,4,6,8,4,6,9])==[1,1,2,4,2,6,1,8,1,9])
assert(aloud.readAloud([2,2,4,6,7,7,9])==[2,2,1,4,1,6,2,7,1,9])
assert(aloud.readAloud([5,5,6,6,6,7,9,11,11,11])==[2,5,3,6,1,7,1,9,3,11])
assert(hidden.is_hidden("Phonesarenowdramaticallysmarter","iPod")==False)
assert(hidden.is_hidden("Mymicrophoneisstillfunctional","remote")==False)
assert(hidden.is_hidden("Avengers","Marvel")==False)
assert(hidden.is_hidden("macoshighsierra","windowsten")==False)
assert(hidden.is_hidden("itstimetoyellatmymother","toyota")==False)

assert(cipher.enc("efg",2)=="egf")
assert(cipher.enc("misterrobotisback",6)=="mrsiobsbatocetkri")
assert(cipher.enc("howareyou",4)=="hruoewyao")
assert(cipher.enc("thesisstatement",8)=="tahteesmiesnstt")
assert(cipher.enc("iamaleader",5)=="ieaamdaelr")
assert(pme.primeMeatExtract(15)==True)
assert(pme.primeMeatExtract(22)==True)
assert(pme.primeMeatExtract(134)==True)
assert(pme.primeMeatExtract(12)==3)
assert(pme.primeMeatExtract(9082)==19)
print('Passed!')
