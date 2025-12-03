from src.order import Order


def test_order_product(order1) -> None:
    assert str(order1) == "заказ товара Samsung Galaxy S23 Ultra в количестве 10 шт., итоговая стоимость = 1800000.0"


# def test_order_add_product(order1, product_one) -> None:
#     order3 = Order("Samsung Galaxy S23 Ultra", 5, 20_000.0)
#     assert str(order3) == ('заказ товара Samsung Galaxy S23 Ultra в количестве 5 шт., итоговая стоимость = 100000.0')

    # assert str(order1.add_product(product_one)) == ('заказ товара Samsung Galaxy S23 Ultra в количестве 5 шт., итоговая стоимость = 100000.0')

    #
    #
    # try:
    #     order2= Order("Iphone 15", 10, 15_000.0)
    # except TypeError:
    #     print("Возникла ошибка TypeError при добавлении другого продукта в заказ")
    # else:
    #     print("Не возникла ошибка TypeError при добавлении другого продукта в заказ")
    #
    # order3 = Order("Samsung Galaxy S23 Ultra", 5, 20_000.0)
    # print(order3)
    #
    # order1.add_product(product1)
    #
    # print(order1)
    # try:
    #     order1.add_product(product2)
    # except TypeError:
    #     print("Возникла ошибка TypeError при добавлении другого продукта в заказ")
    # else:
    #     print("Не возникла ошибка TypeError при добавлении другого продукта в заказ")
