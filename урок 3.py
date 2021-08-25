

# a=10
#
# other=[123,345,'djfg','ghg','ghj']
#
# b=[1,2,3]
#
# print(b[7:0:1])

# start:end:step

students1=['Sharip','Emirlan','Temirlan','Nurlan']
students=['Esenbek','Batyr','Bermet','Fatima','Bekbolsun']
students.extend(students1)
students.append('Adahan')
students.insert(2,'Islam')
print(students)
students[2]='Azamat'
students.remove('Nurlan')
# students.clear()
someone=students.pop(1)
# students.sort()
# students.reverse()
print(someone)
print(students)
