from src.category import ProductIterator


def test_category(category_one, product_two, product_three):
    assert category_one.name == "Смартфоны"
    assert (
        category_one.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert len(category_one.products) == 95
    assert category_one.category_count == 1
    assert category_one.product_count == 2

    category_one.add_product(product_two)
    assert category_one.product_count == 2

    category_one.add_product(product_three)
    assert category_one.product_count == 3


def test_category_str(category_one):
    assert str(category_one) == "Смартфоны, количество продуктов: 13 шт."

def test_product_iterator(product_iterator):
    iter(product_iterator)
    assert product_iterator.index == 0
    assert next(product_iterator).name == 1