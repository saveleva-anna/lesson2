
age= input('введите ваш возраст')
age=int(age)

def mission (age):
  if age <=6:
    return('вы должны учиться в детском саду')
  elif 7 <= age <18:
    return('вы должны учиться в школе')
  elif  19<= age <=25:
    return('вы должны учиться в ВУЗе')
  else:  
    return('вы должны работать')   
  
print(mission(age))