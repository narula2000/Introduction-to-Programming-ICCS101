def mealCal(meal, recipes, db):
    for m_meal in meal:
        for e_recipes in recipes:
            if m_meal in e_recipes:
                m, ingre= e_recipes.split(':')
                for cal in bd:
                    ingre1,calie= cal.split(':')
                    if ingre1 in ingre:   
