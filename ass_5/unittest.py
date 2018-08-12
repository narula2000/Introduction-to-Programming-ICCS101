#Assignment 05  
#Name: Vikrom Narula

#Time Spent: 5 min




import bell
import karma
import sgroup
import sleuth


assert(bell.loveTri(5)==[[1], [1, 2], [2, 3, 5], [5, 7, 10, 15], [15, 20, 27, 37, 52]])
assert(bell.loveTri(4)==[[1], [1, 2], [2, 3, 5], [5, 7, 10, 15]])
assert(bell.loveTri(3)==[[1], [1, 2], [2, 3, 5]])
assert(bell.loveTri(2)==[[1], [1, 2]])
assert(bell.loveTri(6)==[[1], [1, 2], [2, 3, 5], [5, 7, 10, 15], [15, 20, 27, 37, 52], [52, 67, 87, 114, 151, 203]])
assert(karma.keepTabs(["Jim++", "John--", "Jeff++", "Jim++", "John--", "John->Jeff", "Jeff--",
"June++", "Home->House"])=={'Jim': 2, 'Jeff': -2, 'June': 1})
assert(karma.keepTabs(["Jim++", "John--", "Jeff++", "Jim++", "John--", "John->Jeff", "Jeff--",
"June--", "Home->House"])=={'Jim': 2, 'Jeff': -2, 'June':-1})
assert(karma.keepTabs(["Jim++", "John--", "Jeff++", "Jim++", "John--", "John->Jeff",
"June++", "Home->House"])=={'Jim': 2, 'Jeff': -1, 'June': 1})
assert(sgroup.separate([1, 1.2, 4.5, 4.7, 9.1, 9.8, 9.9], 7)==[[1], [1.2], [4.5], [4.7], [9.1], [9.8], [9.9]])
assert(sgroup.separate([1, 1.2, 4.5, 4.7, 9.1, 9.8, 9.9], 6)==[[1], [1.2], [4.5], [4.7], [9.1], [9.8, 9.9]])
assert(sgroup.separate([1, 1.2, 4.5, 4.7, 9.1, 9.8, 9.9], 5)==[[1, 1.2], [4.5], [4.7], [9.1], [9.8, 9.9]])


