import unittest
from Working_With_a_File import WorkingWithFile


class TestScript(unittest.TestCase):
    def setUp(self):
        self.file_action = WorkingWithFile('test_data.txt')
        # файл, для тестирования нахождения суммы, так как там результат выводится разный,
        # создал отдельный файл
        self.subtract_amount = WorkingWithFile('test_subtract_amount.txt')
        # несуществующий файл
        self.file_action_incorrect_filename = WorkingWithFile('test_data3.txt')

    # Если файл существует
    def test_check_file_correct(self):
        self.assertTrue(self.file_action._check_file())

    # Если файл не существует
    def test_check_file_incorrect(self):
        self.assertEqual(self.file_action_incorrect_filename._check_file(), 'Такого файла не существует!!')

    # Если действие указанно неверно
    def test_add(self):
        self.assertEqual(self.file_action.choosing_an_action('ошибочный текст', 'салат -- 30'),
                         'Такого действия нет!!')

    # Добавляем слово если файла не существует
    def test_add_2(self):
        self.assertEqual(self.file_action_incorrect_filename.add_text('слива - 40'),
                         'Такого файла не существует!!')

    # Если указанного слова или предложения не будет в списке
    def test_change_file_2(self):
        self.assertEqual(self.file_action.change_file('слива - 40', 'слива - 90'),
                         'Указанное слово не найдено!!')

    # Если указанного слова или предложения не будет при удалении
    def test_delete_text_2(self):
        self.assertEqual(self.file_action.delete_text('слива - 90'), 'Указанное слово не найдено!!')

    # Если тип слова или предложения не будет указан верно при удалении
    def test_check_type(self):
        self.assertEqual(self.file_action.delete_text(333), 'Разрешено только значение с типом "str" ')

    # Если тип слова или предложения не будет указан верно при Получении суммы и вычета его
    def test_check_type_amount(self):
        self.assertEqual(self.subtract_amount.subtract_amount('hello'),
                         'Разрешено только значение с типом "int" ')

    # Добавляем слово указывая 'actions'
    def test_add_considering_action(self):
        self.assertEqual(self.file_action.choosing_an_action('Добавить в список', 'салат -- 30'),
                         'Значение добавлено!!')

    # Изменяем слово или предложение
    def test_change_file(self):
        self.assertEqual(self.file_action.change_file('салат -- 30', 'слива - 90'), 'Значение обновлено!!')

    # Удаляем слово или предложение
    def test_delete_text(self):
        self.assertEqual(self.file_action.delete_text('слива - 90'), 'Значение обновлено!!')

    # Проверяем работает ли функция для вычета суммы
    def test_subtract_amount(self):
        self.assertEqual(self.subtract_amount.subtract_amount(300),
                         'Общая сумма в файле:500\n После совершения вычета:200')


if __name__ == "__main__":
    unittest.main()
