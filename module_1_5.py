immutable_var = 1, 2, "string", False, 5.0, [2, 'string', True, 4.9,]
print(immutable_var)
immutable_var[2] = 9

#В Pycharm появляется уведомление "Tuples don't support item assignment",
# он не изменяемый тип данных
#Кортеж хранит ссылку на список, а не сами данные в списке.

print(immutable_var)
mutable_list = ['String', True, 5, 6.7, [1, 3.5, False, "string"]]
mutable_list[0] = [True, False, "String", 7, 9]
mutable_list[1] = 8
mutable_list[2] = "String list"
mutable_list[3] = False
mutable_list[4] = 9.8
print(mutable_list)

