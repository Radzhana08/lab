# TODO Написать 3 класса с документацией и аннотацией типов
class Tree:
    """
    Документация на класс Tree.
    Класс описывает модель дерева.
    """
    def __init__(self, age: int, fruits: int):
        """
        Иницилизация экземпляра класса.

        :param age: Возраст дерева.
        :param fruits: Количество фруктов

        Пример:
        >>> pear_three = Tree(15,20) # Инициализация экземпляра класса
        """
        self.age = age
        if age <=0:
            raise ValueError ("Возраст дерева не может быть отрицательным числом")

        self.fruits = fruits
        if not isinstance(fruits, int):
            raise TypeError("Количество фруктов должно быть типа int")


    def calc_age(self) -> int:
        """Метод увеличивает возраст дерева."""
        ...
    def calc_fruits(self, pick_act: int) -> int:
        """
        Метод суммирует собранные фрукты.
        :param pick_act: Количество уже собранных фруктов

        Пример:
        >>> pear_three = Tree (30, 18)
        >>> pear_three.pick_fruits(22)

        """
        ...
class AudioPlayer:
    """
    Класс AudioPlayer нужен для вопроизведения музыки из файла
    """
    def __init__(self, file_extension: str):
        """
        Создание и подготовка к работе объекта "AudioPlayer"
        :param file_extension: Расширение файла
        """
        if not isinstance(file_extension, str):
            raise TypeError("Расширение файла должно быть типа str")
        self.type = file_extension
        self.filename = None

    def open(self, file)->None:
        """
        Метод отркывает файл
        Добавляет новый атрибут к экземпляру
        :param file: Название файла
        :return:
        """
        setattr(self, 'filename', file)
    def play(self):
        """
        Метод воспроизводит музыку

        """

class Vase:
    """
    Документация на класс Vase.
    Класс описывает вид вазы.
    """
    def __init__(self, vase_form: str, vase_volume: int):
        """
        :param vase_form: Форма вазы
        :param vase_volume: Объем вазы
        """
        self.vase_form = vase_form
        if not isinstance(vase_form, str):
            raise TypeError('Форма вазы должна быть str')

        self.vase_volume = vase_volume
        if vase_volume <= 0:
            raise ValueError("Объем вазы не может быть отрицательным")

    def rename_form(self) -> str:
        """Метод изменяет форму вазы"""
        ...
    def mod_vol(self) -> int:
        """Метод изменяет объем вазы"""
        ...







if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    import doctest
    doctest.testmod()
    pass
