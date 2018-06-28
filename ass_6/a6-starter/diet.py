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


meal = ["T-Bone", "T-Bone", "Green Salad1"]
recipes = ["Pork Stew:Cabbage*5,Carrot*1,Fatty Pork*10",
"Green Salad1:Cabbage*10,Carrot*2,Pineapple*5",
"T-Bone:Carrot*2,Steak Meat*1"]
db = ["Cabbage:4,2,0", "Carrot:9,1,5", "Fatty Pork:431,1,5",
"Pineapple:7,1,0", "Steak Meat:5,20,10", "Rabbit Meat:7,2,20"]
print(mealCal(meal, recipes, db))                