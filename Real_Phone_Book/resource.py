##Alex Olhovskiy


menu=['Загрузить - нажмите 1',
      'Сохронить - нажмите 2',
      'Найти - нажмите 3',
      'Редактировать - нажмите 4',
      'Удалить - нажмите 5',
      'Добавить - нажмите 6',
      'Показать - нажмите 7',
      'Уйти - нажмите 8']

e_name='Введите имя'
e_com='Введите комментарий'
a_phone='Добавить номер телефона? y/n'
e_phone='Введите номер телефона'
e_ind='Введите индекс контакта'
e_any='Введите что хотите найти'
e_choise='Делайте выбор'
menu_s='Menu'

def Del(i):
    return 'Вы точно хотите удалить контакт {} y/n'.format(i)

def Change_name(i):
    return 'Вы точно хотите изменить имя контакта {} y/n'.format(i)

def Change_comm(i):
    return 'Вы точно хотите изменить комментарий к контакту {} y/n'.format(i)

def Change_phones(i):
    return 'Вы точно хотите изменить номера телефонов контакта {} y/n'.format(i)