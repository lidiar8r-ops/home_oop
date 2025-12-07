class MixinPrint:
    def __repr__(self) -> str:
        # Получаем атрибуты с проверкой на существование
        name = getattr(self, "name", "N/A")
        description = getattr(self, "description", "N/A")
        price = getattr(self, "price", "N/A")
        quantity = getattr(self, "quantity", "N/A")

        return f"{self.__class__.__name__}('{name}', '{description}', {price}, {quantity})"
