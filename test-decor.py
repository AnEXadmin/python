from functools import wraps


#самый простой:
def type_int(a: int)->str:
    return str(a)
x = 90

print("int->str:",type_int(x))

def str_to_list(s: str)->list:
    l = []
    for i in s:
        l.append(i)
    return l
ss= "12jh1j3vhgv5h46h45ch233jhb"
print('str->list:', 'str:',ss, '\noutput:', str_to_list(ss))

# принимаем  функцию
def decor(func):
    @wraps(func)
    #обертывание функции в "системный декоратор" который позволяет передавать метаданные декорироемых функций, с возможностью использования аргументов вне локальной области функции
    def wrapper(*args,**kwargs):
        #создаем функцию внутри  обертки для работы с агрументами
        return func(*args,**kwargs)
        # возвращаем  в обернутую функцию которую принимали аргументы
    return wrapper
        #возврат  обертки с полученной функцией и аргументами

def decor_upper(func):                                                      #create decor
    def wrapper():                                                          #start modify
        f_data = func()                                                     #take func as data
        up_symbols = f_data.upper()                                         #replace lower symbols to upper(modify original data)
        drop_symbols = '0123456789'                                         #prepare to drop
        du_data = ''.join(i for i in up_symbols if i not in drop_symbols)   #do drop
        return du_data                                                      #return modifed data
    return wrapper                                                          #end modify and return result

@decor_upper                                                                #use decor for func
def ininin():                                                               #func by decor
    n = input('enter any symbols I make from str -> list all symbols by UPPER : ')
    return n
print(str_to_list(ininin()))
