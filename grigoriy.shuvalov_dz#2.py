a = 5 * 3
b = 15 / 3
c = 15 // 2
d = 15 ** 2
print(type(a), type(b), type(c), type(d))



my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
my_list.insert(1, '"'), my_list.insert(3, '"'), my_list.insert(5, '"'), my_list.insert(7, '"'),my_list.insert(-1, '"'),
my_list.insert(-3, '"')
num1 = 5
num2 = 17
num3 = +5
my_list = f'в "{num1:02d}" часов "17" минут температурв воздуха была "+{num3:02d}" градусов'
print(my_list)


my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

print('Привет' + my_list[0][-6:].title(), 'Привет' + my_list[1][-7:].title(), 'Привет' + my_list[2][-8:].title(),
      'Привет' + my_list[3][-7:].title())