# name = ['Kirill', 'Taalai', 'Turat', 'Umut', 'Daniayr']
#
# a = str(input('Enter the name:'))
# if a in name:
#     print('Вы ввели правильное имя')
# else:
#     print('Вы ввели неправильное имя')

name = ['Kirill', 'Taalai', 'Turat', 'Umut', 'Daniayr','Bogdan','Altynbek','Aleksandr','Adinai','Elvira']
a = input('Enter the name:')
while True:
    try:
        name.remove(a)
        print('Welcome')
        a = input('Enter the name:')
    except:
        print('Bye')
        break




        #break
#
