a=open('text.txt','a+',encoding='UTF-8')
print(a.write('это наш гимн'))
a.close()

a=open('text1.txt','w',encoding='UTF-8')
print(a.write('gugjhjhhj'))
a.close()

with open('text.txt','r',encoding='UTF-8') as file:
        print(file.read())

# import random
#
#
# first=(random.randint(1,6))
# second=(random.randint(1,6))
