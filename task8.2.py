taalai = ['VScode', 'PUBG', 'YouTube', 'Discord']
umut = ['SublimeText', 'Telegram', 'WhatsApp', 'Gmail']
aito = ['PyCharm', 'Instagram', 'CSGO']
taalaicode = ['Taxa', 'Tatu', 'Taku']
umutcode = ['umka', 'umut', 'dayana']
aitocode = ['aitoo', 'guru', 'minimaster']
password = {654:'umut', 1234:'taalai', 885:'aito'}

passwrd = int(input('Введите ваш пароль:'))
code = input('Введите код:')

s = ''

try:
    s = password[passwrd]
    if s == 'umut':
        if code in umutcode:
            print(umut)
        else:
            print('Wrong code')
    elif s == 'taalai':
        if code in taalaicode:
            print(taalai)
        else:
            print('Wrong code')
    else:
        if code in aitocode:
            print(aito)
        else:
            print('Wrong code')
except:
    print('Wrong password!')