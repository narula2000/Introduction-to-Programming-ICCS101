import allodd
import happy
import avgno

#Assert_Test
assert(allodd.is_all_odd([2,4,5])==False)
assert(allodd.is_all_odd([2,3,7])==False)
assert(allodd.is_all_odd([1,3,5])==True)
assert(allodd.is_all_odd([4,7,5])==False)
assert(happy.sumOfDigitsSquared([15])==26)
assert(happy.sumOfDigitsSquared([100])==1)
assert(happy.sumOfDigitsSquared([234])==38)
assert(happy.sumOfDigitsSquared([532])==36)
assert(happy.sumOfDigitsSquared([689])==181)
assert(happy.isHappy(154)==False)
assert(happy.isHappy(637)==True)
assert(happy.isHappy(702)==False)
assert(happy.isHappy(39)==False)
assert(happy.isHappy(1003)==True)
assert(happy.kThHappy(3)==10)
assert(happy.kThHappy(15)==82)
assert(happy.kThHappy(30)==190)
assert(happy.kThHappy(12)==68)
assert(happy.kThHappy(44)==293)
assert(round(avgno.robust_avg([1,4,6,11,13,15,2]),4)==7.2)
assert(round(avgno.robust_avg([2,8,12,20,5,11,9]),4)==9.0)
