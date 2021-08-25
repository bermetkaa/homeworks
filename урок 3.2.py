
some_list=[1,2,3]

dictionary={
    'key':'value',
    '13':some_list,
    'home':'дом',
    'some':'value',
    13:'тринадцать',

}
# dictionary['addres']='aaa'
# dictionary[12]='twelve'
# print(dictionary)
# print(dictionary.values())
# print(dictionary.itens())

student={
    'name':'Ivan',
    'age':23,
    'city':"Bishkek",
    'password':123456,
    'password_confirm':123456

}
password_input=int(input('Enter your password'))
password_counfirm_input=int(input('Enter your password again!'))
if password_input==student['password']:
    print('Enter,ok')
else:
    print('password is wrong,no')