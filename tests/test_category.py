def test_category(category_one):
    assert category_one.name == "Смартфоны"
    assert (
        category_one.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert len(category_one.products) == 2
    assert category_one.category_count == 1
    assert category_one.product_count == 2
