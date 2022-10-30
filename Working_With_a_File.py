import os.path
import re


class WorkingWithFile:
    def __init__(self, file_name):
        self.file_name = file_name

    "Функция для проверки, существует ли файл"

    def _check_file(self):
        if os.path.exists(self.file_name):
            return True
        else:
            return 'Такого файла не существует!!'

    "Функция для добавления в список"

    def add_text(self, text):
        check = self._check_file()
        if check is True:
            with open(self.file_name, 'a') as file:
                file.write('{}\n'.format(text))
            return 'Значение добавлено!!'
        else:
            return check

    "Функция для изменения записей в списке "

    def change_file(self, old_word, new_word):
        # Проверяем перед изменением списка, существует ли указанный файл
        check = self._check_file()
        if check is True:
            with open(self.file_name) as file:
                all_text = file.read()
            if old_word in all_text:
                new_data = all_text.replace(old_word, new_word)
                with open(self.file_name, 'w') as file:
                    file.write(new_data)
                return 'Значение обновлено!!'
            else:
                return 'Указанное слово не найдено!!'
        else:
            return check

    "Функция для удаления указанного текста из списка "

    def delete_text(self, del_text):
        if type(del_text) is int:
            return 'Разрешено только значение с типом "str" '
        else:
            return self.change_file(del_text + '\n', '')

    "Функция для вычета общей суммы"

    # Я не совсем понял, от чего нужно вычитать, но предположил, что от вводимого значения
    def subtract_amount(self, amount):
        if type(amount) is not int:
            return 'Разрешено только значение с типом "int" '
        else:
            check = self._check_file()
            if check is True:
                with open(self.file_name) as file:
                    all_text = file.read()
                # через цикл перебираем список и используя регулярки получем все числа
                lst = [int(num) for num in re.findall(r'[+-]?\d+', all_text)]
                result = sum(lst) - amount
                return 'Общая сумма в файле:{}\n После совершения вычета:{}'.format(sum(lst), result)
            else:
                return check

    """Функция для запуска методов относительно 'actions' """

    def choosing_an_action(self, actions, value, new_word=None):
        if actions == 'Добавить в список':
            return self.add_text(value)
        elif actions == 'Изменить запись в списке':
            return self.change_file(value, new_word)
        elif actions == 'Удалить из списка':
            return self.delete_text(value)
        elif actions == 'Вычесть общую сумму':
            return self.subtract_amount(value)
        else:
            return 'Такого действия нет!!'


