# Assignment 06, Task 0
# Name:Vikrom Narula
# Time:  45:00 min

def t_cal(db):
    d=dict()
    for ing in db:
        name, cal = ing.split(':')
        Cr, Pr, Ft= cal.split(',')
        d[name]=(float(Cr)*4)+(float(Pr)*4)+(float(Ft)*9)
    return d

def mealCal(meal, recipes, db):
    tcal=t_cal(db)
    cal=0
    for food in meal:
        for how in recipes:
            if food in how:
                name, ing= how.split(':')
                for way in ing.split(','):
                    ing1, quan= way.split('*')
                    cal=cal+tcal[ing1]*float(quan)
    return cal

