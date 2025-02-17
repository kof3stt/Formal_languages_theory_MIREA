expression = input('Введите выражение в обратной польской записи: ') #ввод выражения, записанного в ОПЗ
funcs = {'*': lambda x, y: x * y, '/': lambda x, y: y / x, '+': lambda x, y: x + y, '-': lambda x, y: y - x} #словарь, содержащий операции в качестве ключей и функции, соответствующие этим операциям
my_stack = list() #"стек"
for i in expression:
    if i.isdigit(): #Если очередной символ входной строки - число, то кладем его в стек.
        my_stack.append(int(i))
    elif i in '*/+-': #Если очередной символ - знак операции
        my_stack.append(funcs[i](my_stack.pop(), my_stack.pop())) #извлекаем из стека два верхних числа, используем их в качестве операндов для этой операции, затем кладем результат обратно в стек
print(f'Значение выражения, записанного в обратной польской записи: {my_stack[0]}') #единственное число в стеке - результат
