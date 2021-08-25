
student={
    'name':'Adilet',
    'age':23,
    'city':"Bishkek",
    'height':1.70,
    'physic passed':False,

}

if not student['height'] >=1.80 and not student['physic passed']==True:
    print('no',student['name'],"не прошел")
else:
    print('ok', student['name'], "куттуктайм сени ,аскер ")


print(student['name'])
print(student['age'])
print(student['city'])



student['city']='Moscow'
print(student)

student['height']=1.75
print(student)
del student['age']
print(student)



