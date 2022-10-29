class WorkingWithFile:
    def __init__(self, file_name, actions):
        self.file_name = file_name
        self.actions = actions

    "Функция для проверки существует ли файл"

    def __check_file(self):
        try:
            with open(self.file_name) as file:
                file.read()
        except FileNotFoundError:
            return 'Такого файла не существует!!'

    "Функция для добавить в список"

    def add_text(self, text):
        check = self.__check_file()
        if check:
            print(check)
        else:
            with open(self.file_name, 'a') as file:
                file.write('\n{}\n'.format(text))

    "Функция для изменения записей в списке "

    def change_file(self, old_word, new_word):
        check = self.__check_file()
        if check:
            print(check)
        else:
            with open(self.file_name) as file:
                all_text = file.read()
            if old_word in all_text:
                new_data = all_text.replace(old_word, new_word)
                with open(self.file_name, 'w') as file:
                    file.write(new_data)
            else:
                return 'Указанное слово не найдено!!'

    "Функция для удаления указанного  текста из списка "

    def delete_text(self, del_text):
        self.change_file(del_text, '')


test = WorkingWithFile('neelds.txt', 'Добавить в список')

test.change_file('fff', ' ')
