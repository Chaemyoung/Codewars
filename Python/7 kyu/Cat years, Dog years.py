def human_years_cat_years_dog_years(human_years):
    catY = 0
    dogY = 0
    
    if human_years == 0:
        catY = 0
        dogY = 0
    elif human_years == 1:
        catY += 15
        dogY += 15
    elif human_years == 2:
        catY = 24
        dogY = 24
    elif human_years > 2:
        catY = 24 + ((human_years-2)*4)
        dogY = 24 + ((human_years-2)*5)
        
    return [human_years,catY,dogY]
  
  ### This one is actually 8 kyu
