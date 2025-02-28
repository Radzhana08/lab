if __name__ == "__main__":
    class Car:
        """Базовый класс Автомобиль.
        Содержит в себе информацию о бренде и модели автомобиля."""

        def __init__(self, brand: str, model: str):
            """Инициализация экземпляра класса.
            :param brand: Автомобильный бренд.
            :param model: Модель автомобиля."""
            self.brand = brand
            self.model = model

        def __str__(self):
            return f"Автомобиль {self.brand}. Модель {self.model}"

        def __repr__(self):
            return f"{self.__class__.__name__}(brand={self.brand}, model={self.model})"

        def recognition(self):
            """Метод выводит текстовое обозначение отношения к автомобилям."""
            print("Мне нравятся машины")

        def BrandName(self):
            """Метод выводит название бренда с использованием функции print"""
            print(f"{self.brand}")


    class Pickup(Car):
        """Дочерний класс Пикап.
        Помимо информации о бренде и модели автомобиля содержит в себе
        значение объёма багажника."""

        def __init__(self, brand: str, model: str, vol_bool: int):
            super().__init__(brand, model)
            self.vol_bool = vol_bool

            super().recognition(self)
            """Метод, унаследованный из основного класса.
            Его содержание не изменяется в дочерних классах."""

        def __str__(self):
            return f"Автомобиль {self.brand}. Модель {self.model}. Объём багажника {self.vol_bool}"

        def __repr__(self):
            return f"{self.__class__.__name__}(brand={self.brand}, model={self.model}, Объём багажника={self.vol_bool})"

        def BrandName(self):
            """Метод, перегруженный из базового класса.
            Это было введено для обозначения различий между экземплярами разных дочерних классов.
            Различные типы кузова имеют разные двигатели и выхлопные системы,
            поэтому издают разные звуки."""
            print(f"{self.brand} {self.model} is bib")



    pass
