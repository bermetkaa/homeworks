# list_1=[1,2,3,'abcd',1,2,3,'abcd']
#
# dict_1={
#     'a':1,
#     'b':2,
#
# }
# set_1={}
# set_1=set(list_1)
# print(dict_1['a'])
# print(set_1)



vuz=[]
sred=[]

students=[
    {
       'name':'Batyr',
        'ort':200,
        'student':False
    },
    {
        'name':'Askar',
        'ort':100,
        'student':False


    },
    {
        'name':'Askar',
        'ort':46,
        'student':False
    }
]

def selection(data):
    for i in data:
        if i['ort'] >= 110:
            vuz.append(i)
        elif i['ort']<=110:
            sred.append(i)
            i['student']=True



selection(students)
print(sred)
print(vuz)
print(students)