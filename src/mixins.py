class MixinPrint:

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', '{self.description}', {self.price}, {self.quantity})'"
        # return f'Класс {self.__class__.__name__}, Название категории: {self.name}, Описание товара: {self.description}, ' \
        #        f'Цена за единицу: {self.price}, Количество на складе: {self.quantity}!!!'
