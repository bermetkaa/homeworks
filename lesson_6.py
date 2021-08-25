
def plus(a, b=3):
    return a + b
print(plus(2))

def double(b, c):
    return b * c
print(double(plus(1, 2), 3))

double_lambda = lambda a, b=3: a * b
print(double_lambda(2,7))

a = lambda a, b: a + b
print(a(2, 3))

my_list=[1,5,4,6,8,11,3,12]
new_list=list(filter(lambda x:(x%2!=0),my_list))
print(new_list)

my_list=[1,5,4,6,8,11,3,12]
new_list=list(map(lambda x:x*2,my_list))
print(new_list)








