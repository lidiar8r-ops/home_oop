from src.product import Product


def test_product(protuct_one):
    assert protuct_one.name == "Samsung Galaxy S23 Ultra"
    assert protuct_one.description == "256GB, Серый цвет, 200MP камера"
    assert protuct_one.price == 180000.0
    assert protuct_one.quantity == 5


def test_product_new_product():
    new_product = Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
         "quantity": 5})
    assert new_product.name == "Samsung Galaxy S23 Ultra"
    assert new_product.description == "256GB, Серый цвет, 200MP камера"
    assert new_product.price == 180000.0
    assert new_product.quantity == 5

def test_product_price_update(capsys, protuct_one):
    protuct_one.price = 0
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"

    protuct_one.price = -100
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"
    assert product_one.price == 180000.0

    product_one.price = 180001
